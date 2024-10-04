# 1. Requirements

## 1.1. Introduction

A product recommendation system in the stock investment domain is designed to help customers discover new investment opportunities that align with their preferences and investment strategies. This system aims to provide personalized recommendations for stocks, bonds, and derivative futures based on advanced machine learning algorithms and customer data analysis.

The primary goal of the recommendation system is to enhance the investment experience by offering tailored suggestions that match each customer's risk tolerance, trading strategy, investment history, and preferences. This helps customers make informed decisions and optimize their investment portfolios.

## 1.2. Functional Requirements

1. **User Authentication and Authorization**
    - Secure user login and role-based access control.
2. **Data Ingestion and Processing**
    - Collect and preprocess data from various sources including: Customer data, Product data, Market data (see [[#3.2. Data collection]] )
    - Batch processing of historical data:
	    - Preprocessing: Involves cleaning, normalizing, and encoding the data to prepare it for analysis.
	    - Feature enginerring: 
		    - Customer Features: Such as risk tolerance, investment patterns, and sector preferences.
		    - Product Features: Including financial ratios, bond ratings, and derivative contract specifics.
    - Handle frequency of data updates:
	    - (Phase 1) Daily updates.
	    - (Phase 2) Real-time updates.
3. **Recommendation Algorithms**
    - (Phase 1) Hybrid ML algorithms for recommendation: [Collaborative filtering + Content-based filtering](https://phamdinhkhanh.github.io/2019/11/04/Recommendation_Compound_Part1.html)
	    - **Collaborative filtering**: Base on user's interaction, then:
			- *User-based Collaborative filtering*: Recommends items based on similar users' preferences.
			- *Item-Based Collaborative Filtering*: Recommends items similar to those the user has interacted with, base on item's interaction.
		- **Content-Based Filtering:** Recommends items similar to those the user has interacted with, based on item features.
	- (Phase 2) Neural Network Recommendation: [Fully connected layer](https://phamdinhkhanh.github.io/2019/12/26/Sorfmax_Recommendation_Neural_Network.html)
	- (Phase 3) Advanced feature for recommendation (see [[#3.1.2. Advanced feature (planned for development)]])
4. **Recommendation strategies**
	- User-driven strategies:
		- For new customer / Inactive customer: the most popular products (stable in time for everyone)
		- For long-time customer: based on user affinity with certain categories of merchandise (customize for each customer)
	- Page context-driven strategies:
		- Home pages: most popular / outstanding
		- Product pages: similar product, pinefolio.
1. **Recommendation Generation**
	- Output model is the matching score of each product for each user.
    - Generate a list ( TOP 10 highest score ) of recommended stocks, bonds, and derivative futures for each user.
    - Frequuency of update recommendations:
	    - (Phase 1): Daily running model with updated data
	    - (Phase 2) Update recommendations in real-time based on new interactions and market data.
2. **Deployment**
	- Integration: Embedding the recommendation system into the existing trading platform.
	- API Endpoints: Developing APIs for real-time recommendations.
	- Feedback Loop: Collecting user feedback to refine and improve the system continuously.
3. **Recommendation Delivery**
	1. **User Interface**
	    - Provide an intuitive dashboard for users to view and interact with recommendations.
	    - Allow users to filter recommendations based on criteria such as risk level, sector, and investment type.
	    - Suggest similar products in product screen, search screen,...
	2. **Alerts and Notifications**
	    - Send notifications and alerts to users about new recommendations, market changes, and relevant investment opportunities.
	3. **Chatbot Integration** 
		- AI-driven tools that provide recommendations in response to user queries or interactions.
	4. **Feedback Loop**
	    - Collect user feedback on recommendations to improve the accuracy of the models by action:
		    - Click view
		    - Add to favorite
		    - Buy/Sell
4. **Performance Monitoring and Reporting**
    - Track performance metrics such as:
	    - Click-through rate (CTR)
		- Conversion rate
		- User satisfaction.
    - Generate reports and analytics on system performance and user engagement.
    -  A/B Testing: Comparing different recommendation strategies to optimize performance.

## 1.3. Non-Functional Requirements

1. **Scalability**
    - The system must handle increasing numbers of users and data volume efficiently.
2. **Performance**
    - Provide fast response times for generating recommendations and updating the user interface.
3. **Reliability and Availability**
    - Ensure high availability and reliability of the recommendation system with minimal downtime.
4. **Security**
    - Implement robust security measures to protect user data and ensure privacy.
5. **Usability**
    - Design the user interface to be user-friendly and accessible, ensuring a seamless user experience.
6. **Maintainability**
    - Ensure that the system is maintainable and easy to update with new features and improvements.
7. **Compliance**
    - Adhere to relevant financial regulations and data protection laws.

## 1.4. GCP Service Requirements

1. **Data Storage and Management**
    - **BigQuery:** For managing and querying large datasets efficiently.
    - ~~**GCS:** storage file~~
2. **Data Processing**
    - **Cloud Dataflow:** For real-time and batch data processing.
    - **Cloud Dataprep:** For data cleaning and transformation.
3. **Machine Learning**
    - **Vertex AI:** For training, deploying, and managing machine learning models.
    - ~~**BigQuery ML:** For running machine learning models directly on BigQuery data.~~
4. **Compute**
    - **Compute Engine:** For scalable virtual machines to run applications and algorithms.
    - **Kubernetes Engine:** For containerized application deployment and orchestration.
5. **Storage and Databases**
    - **Cloud SQL / Firestore:** For relational and NoSQL database management.
    - **Cloud Spanner:** For horizontally scalable, strongly consistent relational database.
6. **APIs and Microservices**
    - **Cloud Functions:** For serverless functions to handle real-time data processing and trigger workflows.
    - **Cloud Endpoints:** For managing and deploying APIs securely.
7. **Security**
    - **Cloud IAM:** For managing access control and permissions.
    - **VPC Service Controls:** For defining security perimeters around GCP resources.
8. **Monitoring and Logging**
    - **Stackdriver Monitoring and Logging:** For performance monitoring, logging, and alerts.
    - **Cloud Trace and Cloud Debugger:** For tracing and debugging applications.
9. **Networking**
    - **Cloud CDN:** For content delivery to ensure fast load times.
    - **Cloud Load Balancing:** For distributing incoming traffic across multiple instances.
# 2. Timeline

[Product_Recommendation_Plan.xlsx](https://hftvietnam.sharepoint.com/:x:/s/da/EW5NW6zOj_tJgmC0wq7fHAMB-lqcxi7Pn5Z0UWw77Mgn7w?e=49nkct&nav=MTVfezgxMjU0ODlDLUE5OUItNDI1Ny04QUE2LTVEODNFQ0NBQjBEQn0)

# 3. Thiết kế hệ thống


## **Danhh sách model**
- Model phân loại trạng thái khách hàng #M1
	- Khách hàng `inactive`
	- Khách hàng `active`
	- Khách hàng mới `new`
- Model phân tích đặc điểm khách hàng #M2
	- Mức độ biến động danh mục
	- Thời gian nắm giữ
	- Đa dạng hoá danh mục
	- Mức độ phổ biến danh mục
	- Tỷ lệ sử dụng đòn bẩy
- Model phân tích sản phẩm #M3
	- Có phải là sản phẩm mới ? (Stock mới list sàn, chứng quyền mới list, bond mới phát hành, ETF mới, hợp đồng phái sinh. )
	- Mức độ phổ biến - được giao dịch nhiều : top những mã được giao dịch nhiều, thanh khoản lớn, được đầu tư nhiều,...
	- ...
- Model chấm điểm khách hàng với sector
- Model gom nhóm sản phẩm #M4
- Model gom nhóm khách hàng #M5
- Model đề xuất sản phẩm phổ biến #M6
- Model đề xuất sản phẩm mới #M7
- Model đề xuất sản phẩm tương tự với danh mục hiện tại #M8
- Model đề xuất theo dữ liệu trạng thái (wide & deep learning) #M9
- Model đề xuất theo chuỗi hành vi (SASRec) #M10
- Model hybrid recommend (kết hợp nhiều loại model) #M11
	- Sử dụng #M1 để phân loại 

- **Explainability (Giải thích gợi ý)**: Để tăng độ tin cậy và sự minh bạch, tích hợp thêm các công cụ giúp giải thích rõ ràng tại sao một sản phẩm được đề xuất. Các mô hình như SHAP hoặc LIME có thể hữu ích trong việc này.
    
- **Dynamic Context-aware Recommendation**: Hệ thống gợi ý nên có khả năng cập nhật theo thời gian thực dựa trên các sự kiện ngắn hạn hoặc biến động thị trường. Ví dụ: Nếu có tin tức đột xuất về một cổ phiếu, các khuyến nghị liên quan đến cổ phiếu đó sẽ được ưu tiên.
## **Yêu cầu monitoring**

### Trạng thái model hiện tại
- Thông tin về model
	- Status:
		- Running (green) : The engine is running and uses the newest data
		- Suspended (green) : The engine is suspended because it wasn’t used in the last 14 days
		- Limited (orange) : The engine is running but is not trained on the latest data. In the case of the Advanced model, one of the underlying engines isn’t working properly or isn’t trained on the latest data
		- Pending (yellow) : Engine is waiting to be trained. The saved engine should be available within 24h
		- Failed (red) : The engine failed to be created or is unavailable (technical problem)
		- Inactive (gray) : Engine was disabled or deleted
		- Unknown (gray) : We were unable to detect the state of the engine
		- Draft (blank) : The engine was not saved yet
	- Ngày deploy cuối cùng
	- Model version
- Danh sách các model sử dụng hiện tại + luồng đi pipeline + tỷ trọng model / cách combine cho từng case của KH
- Performance của model ( Sau khi train vs Hiện tại (dựa trên feedback của KH) )
	- 
	- 
### Trạng thái dữ liệu
- Trạng thái khách hàng và items:
	- Số lượng khách hàng theo từng loại: active , inactive, KH mới
	- Số lượng item: stock, bond, cw, etf, derivative, và đếm số lượng item mới theo từng loại
- Trạng thái data pipeline: Thống kê các nguồn data đang active và inactive
- Data/feature drift

### Trạng thái recommendation items
- Customer Flow per Model: Số lượng khách hàng đi qua mỗi luồng mô hình cụ thể
- CTR (Click-Through Rate - Tỷ lệ nhấp chuột): Tỷ lệ số lần khách hàng nhấp vào một sản phẩm được gợi ý trên tổng số lần hiển thị gợi ý.
- Conversion Rate (Tỷ lệ chuyển đổi): Tỷ lệ KH thực hiện giao dịch items/read news các item trong recommendation list
- Tổng số lượng recommendation items:
	- Số lượng items được lặp lại
	- Số lượng recommendation items mới
- Danh mục item phổ biến hiện tại
- Danh mục item mới hiện tại
### Vận hành hệ thống
- log run daily
	- Count số lượng fail pipeline
	- Trạng thái thành công pipeline:
		- Thời điểm bắt đầu, thời gian hoàn thành
		- 





# 4. Appendix

## 3.1. Recommendation Algorithms Research

### 3.1.1. Algorithms research

#### 3.1.1.1. Content-based Filtering

Về phương pháp của content-based filtering đã được trình bày rất chi tiết tại [Bài 23: Content-based Recommendation Systems](https://machinelearningcoban.com/2017/05/17/contentbasedrecommendersys/). Tôi sẽ giới thiệu khái quát nhất về thuật toán này.

Đối với mỗi một item chúng ta sẽ tìm cách khởi tạo một item profile bằng cách thu thập các trường thông tin liên quan đến item. Mỗi một item profile được đại diện bởi một véc tơ đặc trưng 𝑥. Gọi 𝑆𝑖 là tập hợp các sản phẩm mà khách hàng 𝑖 đã rating và giá trị rating là véc tơ 𝑦𝑖. Khi đó chúng ta cần tìm hệ số 𝑤𝑖 là véc tơ cột chứa các hệ số hồi qui thể hiện mức độ yêu thích của khách hàng 𝑖 đối với mỗi một chiều của sản phẩm.

Hàm loss function đối với những sản phẩm mà khách hàng 𝑖 đã rating sẽ có dạng:

$$ \mathcal{L_i}(\mathbf{x_j}; \mathbf{y_i}| j \in S_{i}) = \frac{1}{2 s_i} \sum_{j \in S_i}{(\mathbf{x_jw_i} + b_i - y_{ij})^{2}} $$
Trong đó 𝑦𝑖𝑗 là một phần tử của véc tơ 𝑦𝑖, 𝑏𝑖 là hệ số tự do trong phương trình hồi qui tuyến tính và 𝑠𝑖 là số lượng sản phẩm mà khách hàng 𝑖 đã đánh giá.

Nếu ta trích xuất ra ma trận con 𝑋𝑖 gồm những sản phẩm mà khách hàng 𝑖 đã rating. Mỗi dòng của ma trận là một véc tơ các đặc trưng tương ứng với một sản phẩm. Khi đó hàm loss function có thể được viết gọn lại thành:

$$\mathcal{L_i}(\mathbf{X_i}; \mathbf{y_i}) = \frac{1}{2 s_i}{||\mathbf{X_iw_i} + b_i \mathbf{e_i} - \mathbf{y_i}||_2^{2}}$$

Với 𝑒𝑖 là véc tơ cột gồm 𝑠𝑖 phần từ bằng 1.

Để rút gọn hơn nữa hàm loss function ta biểu diễn nó đưới dạng phương trình của ma trận mở rộng:

$$𝐿𝑖(𝑋𝑖;𝑦𝑖)=12𝑠𝑖||𝑋𝑖¯𝑤𝑖¯−𝑦𝑖||22$$

Ở đây ma trận 𝑋𝑖¯ là ma trận mở rộng của 𝑋𝑖 bằng cách thêm một véc tơ cột bằng 1 ở cuối. 𝑤𝑖¯ cũng là véc tơ mở rộng của 𝑤𝑖 khi thêm phần tử 1 ở cuối.

Đây là một phương trình hồi qui tuyến tính quen thuộc nên việc giải nó khá dễ. Trong một số trường hợp để giảm overfiting thì ta sẽ thêm thành phần kiểm soát (regularization term) theo norm chuẩn bậc 2 của 𝑤𝑖 với trọng số là 𝜆 (thường có giá trị rất nhỏ). Hàm loss function với thành phần kiểm soát sẽ như sau:

$$𝐿𝑖(𝑋𝑖;𝑦𝑖)=12𝑠𝑖||𝑋𝑖¯𝑤𝑖¯−𝑦𝑖||22+𝜆2𝑠𝑖||𝑤𝑖¯||22$$

Ưu điểm của phương pháp này là việc phân loại hoặc dự báo rating của các user sẽ độc lập nhau. Điểm rating của một khách hàng A lên sản phẩm P sẽ không bị phụ thuộc bởi những user khác mà chỉ phụ thuộc vào các đặc điểm liên quan đến sản phẩm P. Do đó chất lượng dự báo sẽ được tăng lên khi dữ liệu được thu thập về sản phẩm là những trường có quan trọng ảnh hưởng đến sở thích của khách hàng.
### 3.1.2. ML Algorithms comparation

| Algorithms     | Collaborative filtering                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Content-based filtering                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Hybrid Recommender                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| How it works ? | Use clustering models, user-based k-nearest neighbors, matrix factorization, and Bayesian networks to group customer or items into groups with the same interaction.![[Pasted image 20240531130725.png]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Considers the item's characteristics, such as price, volume, sector, group defined by assigned keywords and tags, then group items to group with the same characteristics.![[Pasted image 20240531131409.png]]                                                                                                                                                                                                                                                                        | Combining collaborative and content-based filtering scoring with the difference weighting, depends on each different group. |
| Sub-model      | **Item-base** and **User-base**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Item characteristics and Demographics user                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                             |
| Prods          | **Extremely accurate** and provide effective suggestions, especially when relying on context-aware filtering.<br><br>**Predict customers' interest** in a product they didn't know existed by observing what caught the attention of similar users.<br><br>**No need to understanding the nature of each item**, which eliminates the need for detailed product descriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Handle the new items with no interaction yet<br><br>Apply for recommendation use for searching by text/ characteristic                                                                                                                                                                                                                                                                                                                                                                | Enhance recommendation systems' performance.                                                                                |
| Cons           | **Cold start problem:** providing valuable suggestions to new users with no purchase history can be challenging considering the only available parameters (gender, age, etc.).<br><br>**Scalability:** using this algorithm to search for purchase patterns among a growing number of customers and products requires significant computational power.<br><br>**Rich-get-richer effect:** algorithms generally recommend products with many excellent reviews, increasing their popularity at the expense of new items.<br><br>**Data sparsity:** in cases with a large product catalog, each item may not have a sufficient number of user reviews to analyze, reducing the recommendations' accuracy.<br><br>**Shilling attacks:** new products are vulnerable to rating manipulations (such as negative reviews from competitors). | The tagging procedure implies a massive workload, especially on large platforms or marketplaces.<br><br>The cold start issue of collaborative filtering is still there, although less critical than in collaborative filtering, as the historical data associated with new customers is very limited.<br><br>Algorithms can be rather conservative, recommending categories of products and content already purchased by a user and avoiding new, potentially interesting categories. | Merging both mechanisms into a single system requires more complex architectures and superior computing power.              |

### 3.1.3. Advanced feature (planned for development)
- Session-Based Recommendation : hệ thống recommendation chứa yếu tố time session
- Thuật toán LSTM dự đoán sản phẩm có khả năng mua tiếp theo của khách hàng dựa vào lịch sử mua sắm.
- Sử dụng các thuật toán NLP (Natural language processing - Xử lý ngôn ngữ tự nhiên) để phân tích các thông tin như phần tên sản phẩm, mô tả sản phẩm, comment khách hàng về sản phẩm để tìm ra sản phẩm tương đồng.
- Sử dụng AutoEncoder để tìm kiếm sản phẩm tương đồng, khách hàng tương đồng. Về auto encoder có thể xem thêm tại [Bài 3 - Mô hình Word2Vec](https://phamdinhkhanh.github.io/2019/04/29/ModelWord2Vec.html).
- Các hệ thống search engine dựa trên hình ảnh của sản phẩm.
- Sử dụng reignforcement learning để recommend sản phẩm dựa trên các dự báo về hành vi tiếp theo của khách hàng.
- Sử dụng [LDA](https://phamdinhkhanh.github.io/2019/09/08/LDATopicModel.html) để clustering các nhóm sản phẩm có chung đặc điểm và có thể thay thế được cho nhau.
- Thuật toán association để tìm các sản phẩm hoặc nhóm khách hàng có mối liên hệ trong hành vi mua sắm thông qua một chỉ số là levarage.

## 3.2. Data collection

### 3.2.1. Customer data
#### 3.2.1.1. Customer Demographics
- Customer ID
- Age
- Gender
- Location
- Income level
- Occupation
- Segmentation
- Balance Status
#### 3.2.1.2. Behavioral Data
- Purchase history (stocks bought, quantities, and dates)
- Browsing history (stocks viewed, search terms used)
- Interaction history (clicks, likes, comments, shares)
- Trading patterns (frequency, volume, type of trades, orders history)
- App usage patterns (login, screen)
#### 3.2.1.3. Financial Data
- Portfolio holdings
- Account balance
- Transaction history
- Risk tolerance
### 3.2.2. Product information
#### 3.2.2.1. Stock
- **Stock Attributes:**
	- Stock ID
	- Stock name
	- Sector
	- Industry
	- Market capitalization
	- Label in market: VN30, VN100, ...
- **Price-volume index:**
	- Historical price-volume data
	- Technical indicators: EMA, MA, RSI, BB,...
	- Volatility
	- Dividend yield
	- Popularity Score
	- Leverage level
	- Liquidity
- **Fundametal index:**
	- Balance sheet, Financial Statement,...
	- Company Index: P/E, EPS,...
- **News/Social media Sentiments Analysis:**
	- Count recent news
	- Sentiments of news
- **Relationship data:**
	- Competitors: counts, average return competitor index
	- Partner: counts, average return index
- **Transaction data:**
	- Historical stock transaction in Pinetree
	- Return of stock in each customer
#### 3.2.2.2. Bond
- **Identification**:
	- Bond ID (unique identifier)
	- Issuer (the entity issuing the bond)
	- Issuer type (e.g., government, corporation)
	- Industry/sector (for corporate issuers)
	- Creditworthiness
- **Basic Attributes:**
	- Bond name
	- Issue date
	- Maturity date
	- Coupon rate (interest rate paid by the bond)
	- Coupon frequency (e.g., annually, semi-annually)
	- Principal amount (face value of the bond)
	- Type of bond (e.g., corporate, municipal, government, convertible)
- **Pricing and Yield:**
	- Current price
	- Yield to maturity (YTM)
	- Yield to call (if callable)
	- Coupon payment dates
	- Duration
	- Convexity
- **Risk and Ratings:**
	- Credit rating (from agencies like Moody's, S&P, Fitch)
	- Default risk
	- Historical volatility
- **Special Features:**
	- Callable/Puttable (whether the bond can be redeemed early by the issuer or holder)
	- Convertible (whether the bond can be converted into equity)
	- Floating rate (if the coupon rate is variable)
- **Transaction Attributes:**
	- Transaction ID
	- Bond ID
	- Transaction date
	- Transaction price
	- Transaction volume
	- Buyer and seller IDs (if available)
	- Popularity
#### 3.2.2.3. Derivative
- **Identification**:
	- Contract ID (unique identifier)
	- Index name
	- Ticker symbol
	- Exchange (e.g., Ho Chi Minh Stock Exchange (HOSE), Hanoi Stock Exchange (HNX))
- **Contract Specifications:**
	- Contract size (number of units of the underlying asset per contract)
	- Contract months (e.g., March, June, September, December)
	- Tick size (minimum price movement)
	- Trading hours
	- Last trading day
- **Pricing and Valuation:**
	- Settlement price
	- Daily high, low, open, and close prices
	- Volume traded
	- Open interest (number of outstanding contracts)
- **Margin and Leverage:**
	- Initial margin requirement
	- Maintenance margin requirement
	- Leverage ratio
- **Underlying asset:**
	- Index name
	- Index composition (constituent stocks and their weights)
	- Historical index values
	- Dividend yields
	- Sector breakdown
- **Transaction Attributes:**
	- Transaction ID
	- Contract ID
	- Transaction date
	- Transaction price
	- Transaction volume
	- Buyer and seller IDs (if available)
	- Popularity
### 3.2.3. Market data
#### 3.2.3.1. Market Indicators
- Stock market indices (e.g., VN30, VNINDEX)
- Interest rates
- Inflation rates
- Economic indicators (e.g., GDP, unemployment rates)
#### 3.2.3.2. Market Trends
- Sector performance trends
- Industry performance trends
- Global market conditions
- Regulatory changes

## 3.3. Schema Design

### 3.3.1. Table schema

**User-Product Recommendations**: the recommended products for each user.
```sql
CREATE TABLE `project_id.dataset_id.user_product_recommendations` (
    user_id STRING,
    product_id STRING,
    recommendation_score FLOAT,
    timestamp TIMESTAMP
)
PARTITION BY DATE(timestamp)
CLUSTER BY user_id
```


**Product Metadata**: additional information about products that might be useful for filtering and analysis.
```sql
CREATE TABLE `project_id.dataset_id.product_metadata` (
    product_id STRING,
    product_name STRING,
    category STRING,
    sector STRING,
    description STRING,
    PRIMARY KEY (product_id)
)
```


**User Metadata**: additional information about users for personalized recommendations and analysis.
```sql
CREATE TABLE `project_id.dataset_id.user_metadata` (
    user_id STRING,
    age INT,
    gender STRING,
    risk_tolerance STRING,
    investment_style STRING,
    PRIMARY KEY (user_id)
)
```

### 3.3.2. Data Storage Strategy
- Denormalization: denormalize the data by embedding frequently accessed metadata within the recommendation table.
- Partitioning by `timestamp`
- Clustering by `user_id`
- Partition Expiration:
```sql
ALTER TABLE `project_id.dataset_id.user_product_recommendations` SET OPTIONS ( expiration_timestamp = TIMESTAMP "2025-01-01 00:00:00 UTC" )
```


# 5. Refs
1. https://www.itransition.com/machine-learning/recommendation-systems
2. https://phamdinhkhanh.github.io/2019/11/04/Recommendation_Compound_Part1.html
3. https://phamdinhkhanh.github.io/2019/12/26/Sorfmax_Recommendation_Neural_Network.html
4. https://phamdinhkhanh.github.io/2020/02/11/NARSyscom2015.html
5. https://neptune.ai/blog/recommender-systems-lessons-from-building-and-deployment