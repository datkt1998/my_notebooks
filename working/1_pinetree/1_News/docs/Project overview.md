  
# 1. Structure  
  
Version control: Pinetree Bitbucket  
  
Branch `ducpx_webservice`  and `web-crawler-server` seems contain **up-to-date** files.  
  
# 2. Flow  
  
## 2.1. Crawler get news by  
  
* by stock code  
* by source news  
  
## 2.2. Classifier: classify news by  
  
* based on daily news model  
* based on morning brief model  
  
## 2.3. Summarizer: summary news by  
  
* by TextRank  
* with limited words  
* detect stock code in news  
  
## 2.4. Ranking: rank news based on  
  
* by TF-based  
* by Rule-based  
  
## 2.5. Update database (mongoDB)  
  
then from Database we can either:  
  
* Display result to Web Application  
* Review news manually to fine tune models (include: Daily news models, Morning brief models, Ranking rules)  
  ![[Pasted image 20240130152835.png]]

>Review news manually? How it works? On interactions of users in Web (only Daily News page has, or manually input file  
> train/test??)  

# 3. Web Crawler Module  
  
**Logic:**  
  
* crawl data by source  
* crawl data by stock symbol in VN30 (annully update)  
  
Run bash file (batch job), each source = one bash job. Cách nhau 2 tiếng. (so each source run once per day?)  
  
```bash  
news/  
├── spiders # thư mục chứa các spider cho từng sites  
│ ├── __init__.py  
│ ├── bidv_spider.py  
│ ├── cafef_spider.py  
│ ├── finance_vietstock_spider.py  
│ ├── forbesvietnam.py  
│ ├── kenh14_spider.py  
│ ├── ndh_spider.py  
│ ├── qandme.py  
│ ├── sbv_spider.py  
│ ├── stockbizvn_spider.py  
│ ├── tinnhanhchungkhoan_spider.py  
│ ├── vcb_spider.py  
│ ├── vietinbank_spider.py  
│ ├── vietnambiz_spider.py  
│ ├── vietstock_spider.py  
│ ├── vingroup_spider.py  
│ ├── vpbank_spider.py  
│ └── zingnews_spider.py  
├── __init__.py  
├── items.py # nơi định nghĩa các trường dữ liệu cần lưu vào db  
├── loader.py # nơi xử lý, chuẩn hóa dữ liệu  
├── middlewares.py # middlewares file  
├── pipelines.py # nơi xử lý các item trích xuất được và lưu vào db  
└── settings.py # cấu hình thêm các phần mở rộng (middlewares) và các thông số cấu hình khác  
```  
  
`news/pipelines.py` : **ai-news pipeline executed here**. (classify, summary, rank → write to mongoDB, object  
MongoPipeline )  
  
**Lib**: `scrapy`  
  
_Some sites require simulation with selenium (therefore require driver-path)_  
  
**Two types of news:**  
  
* Important daily news: Macro news, International news, VN stock market  
* Morning brief news - VN30 news: 7 pre-defined categories of stocks in VN30 basket  
  
# 4. Summarizer module  
  
```bash  
summarizer/  
├── vncorenlp/models/wordsegmenter # model of VnCoreNLP  
├── ViTextRank.py # TextRank-based  
├── BertParent.py # cluster-based  
├── ClusterFeatures.py # cluster-based  
├── model_processors.py # cluster-based  
└── vi_stopwords.txt # stop-word for pre-processing data  
├── __init__.py  
```  
  
**Summary news using 2 algorithm:**  
  
* TextRank-based  
* Clustering-based  
  
_**Summary rate = 10%**_  
  
> **For Morning Brief <= 40 words**, both algorithms include:  
>  
>* Input: content of news  
>* Output: summarized content  
  
**`Example:`**  
  
```python  
from summarizer import Summarizer  
from summarizer.ViTextRank import ViTextRank  
  
# Clustering-based model  
summarizer = Summarizer(model='vinai/phobert-base',    hidden=-2, reduce_option='mean')
summarized_doc = summarizer(doc, ratio=0.25, max_words=40)  
  
# TextRank-based model  
text_rank = ViTextRank()  
summarized_doc = text_rank.run(doc, ratio=0.1, max_words=40)  
```  
  
# 5. Classifier module  
  
```bash  
classifier/  
├── README.md # file README cho Classifier  
├── __init__.py  
├── classifier.py # Classifier Algorithm  
└── utils.py # Pre-processing data before classifier  
└── train.py  
```  
  
### 5.1.1. Categorize news based on two models:  
  
**1. Important news**  
  
* macro news  
* international news  
* VN stock market  
  
**2. Morning brief news**  
  
* banking  
* real estate  
* oil and gas  
* vingroup  
* food and drink  
* others  
* social trend  
  
### 5.1.2. Model preparation steps  
  
#### 5.1.2.1. Step 1: Prepare the data  
  
Prepare the dataset (as of csv files), includes:  
  
* title  
* brief_content  
* content  
* label  
  
_(as in MongoDB, result of Crawler module)_  
  
#### 5.1.2.2. Step 2: Train model  
  
**Input** is combination of `title` and `brief_content`. **Output** is a pretrained model: `best_model.model`(_zip file  
format_)  
  
```python  
from classifier import Classifier  
  
classifier = Classifier(pretrained='vinai/phobert-base')  
classifier.train(  
    train_path='./data/news/trains.csv',    test_path='./data/news/test.csv',    text_col='text',    label_col='category',    bs=16,    epochs=1,    lr=1e-5,    is_normalize=True,    name='best_model')  
```  
  
**→ output is a pretrained model**: `best_model.model` in zip file format.  
  
#### 5.1.2.3. Step 3: Predict classification of a news  
  
We use result of step 2 to predict the category of each news.  
  
* input: title and brief_content of each news  
* output: category of that news  
  
```python  
from classifier import Classifier  
  
classifier = Classifier(model_path='./model/phobert_epoch_1.model')  
pred = classifier.predict(sample='GDP tháng này tăng mạnh...')  
print(pred)  
  
>> > {'class': macro_news, 'score': 0.9999}  
```  
  
Ranking module  
  
```bash  
ranking/  
├── README.md # file README cho Ranking  
├── __init__.py  
├── ranking.py # file chứa thuật toán Ranking  
├── utils.py # file chứa các hàm xử lý phụ trợ  
├──config_ranking.yaml # file chứa các keywords được define cho các category và rank tương ứng  
└── stock_code.yaml  
```  
  
**Auto rank news based on pre-defined criteria.**  
  
Pre-defined criteria is in `config_ranking.yaml` which contains rank of each keyword/group of keywords by news  
category (  
category is labeled in Classifier module)  
  
Pre-requisite for Ranking module:  
  
* Ranking algorithm  
* Pre-defined criteria for each News Category (yaml config file)  
  
How ranking module works:  
  
* Access to MongoDB → get title, brief_content, content (??)  
* Calculate score for each news based on definition in file config_ranking.yaml and Ranking algorithm  
* Sort news based on calculated score  
  This works within each category.  
  
Each category has different number of ranking group.  
  
News displayed in Homepage based on `rank` and `rank_score` in each category. By rank > within rank 1 (example) sorted  
based  
on `rank_score`.  
  
**Ranking algorithm has two approaches:**  
  
* Rule-based ranking  
* TF-based (Term Frequency-based) ranking  
  
Output: For each news:  
  
* Rank of this news  
* Score of this news  
* Name rank  
  
> TFRanking >> better than RuleRanking  
  
##### 5.1.2.3.1. RuleRanking  
  
Scan content of the news and get matching keywords in configuration file.  
  
* Input: title, content  
* Output: dictionary {’rank’: int, ‘score’: float, ‘name_rank’: str}  
  
```python  
from ranking import RuleRanking  
  
sample = "blahblahblah"  
ranking = RuleRanking(config_file='./config_ranking.yaml')  
out = ranking.get_rank(sample=sample, prior_category='macro_news')  
  
>> > {'rank': 3, 'score': 1.0. 'name_rank': 'gpd'}  
```  
  
##### 5.1.2.3.2. TFRanking  
  
**_Pre-requisite_**: Still need keywords for each rank in each category.  
  
`TFRanking` calculate frequency of keyword in content of the news. This algorithm is currently in use:  
  
* Input: title, content  
* Output: dictionary {’rank’: int, ‘score’: float, ‘name_rank’: str}  
  
```python  
from ranking import TFRanking  
  
sample = 'blah blah'  
ranking = TFRanking(config_file='./config_ranking.yaml')  
out = ranking.get_rank(sample=sample, prior_category='macro_news')  
  
print(out)  
  
>> > {'rank': 3, 'score': 0.215053, 'name_rank': 'gpd'}  
```  
  
##### 5.1.2.3.3. Keywords File  
  
This file defines keyword and its ranking (priority) in each news, by category.  
  ![[Pasted image 20240130153017.png]]
Yaml file.  
  
# 6. Web Application module  
  
```bash  
web-demo  
├── static  
│ ├── css # folder chứa css  
│ ├── images # folder chứa images  
│ └── js # folder chứa js  
├── routes # folder xử lý các pages  
│ ├── __init__.py  
│ ├── accounts.py  
│ ├── daily_news.py  
│ ├── morning_brief.py  
│ └── vn_30.py  
├── templates # folder chứa html  
│ ├── daily_news.html  
│ ├── login.html  
│ ├── main.html  
│ ├── morning_brief.html  
│ ├── register.html  
│ └── vn_30.html  
├── AIapp.pem  
├── config.py # file setup các biến khai báo để đọc ra dùng global  
├── helpers.py # file chứa hàm để query data  
├── main.py # file chứa hàm xử lý trang main và liên kết với các phần trong routes  
├── paginate.py # file chứa hàm xử lý để phân trang  
├── requirements.txt # requirements cho module  
└── vn30.json # file dữ liệu lưu trữ thông tin của VN30  
```  
  
**How to train model**  
_(Daily news, Morning brief is similar)_  
  
1. **Step 1**: Get trained model from train and test dataset  
  
`example code`  
```python  
from classifer import Classifier  
  
classifier = Classifier(pretrained='vinai/phobert-base')  
  
classifier.train(train_path='./data/daily_news/train.csv', test_path='./data/daily_news/test.csv', text_col='text',  
label_col='category', bs=16, epochs=15, lr=1e-5, is_normalize=True, name='dailynews_best_model'  
)  
$ cd ai-news/train_classify  
$ python train.py  
--train_path './data/daily_v2_train.csv'  
--test_path './data/daily_v2_test.csv'  
--epochs 15  
--lr 1e-5  
--bs 16  
--name dailynews_best_model  
  
$ cp dailynews_best_model news_system/crawler/scraper/classifier/model/.from ranking import TFRanking  
  
sample = 'blah blah'  
ranking = TFRanking(config_file='./config_ranking.yaml')  
out = ranking.get_rank(sample=sample, prior_category='macro_news')  
  
print(out)  
  
>>> {'rank': 3, 'score': 0.215053, 'name_rank': 'gpd'}  
  
```  
>New trained model then be copied to classifier/model/.  
  
2. **Step 2**: Using trained model to generate label for data.  
  
3. **Step 3**: Fine-tune model  
  
Must have somewhere to write reviewed data??  
```python  
from classifier import Classifier  
  
classifier = Classifier(pretrained='vinai/phobert-base')  
classifier.fine_tuning(model_path='./data/models/daily_news_best.model',  
data_path='./data/news/reviewed_daily_news.csv', text_col='text', label_col='label', bs=16, epochs=1, lr=1e-5,  
is_normalize=True  
)  
$ cd ai-news  
  
$ python news_system/crawler/scraper/classifier/train.py  
–from-pretrained news_system/crawler/scraper/classifier/model/dailynews_best_model  
--train_path './data/daily_v2_train.csv'  
--test_path './data/daily_v2_test.csv'  
--epochs 15  
--lr 1e-5  
--bs 16  
--name dailynews_best_model  
  
$ cp dailynews_best_model news_system/crawler/scraper/classifier/model/.  
```