# Requirements

## Introduction

A product recommendation system in the stock investment domain is designed to help customers discover new investment opportunities that align with their preferences and investment strategies. This system aims to provide personalized recommendations for stocks, bonds, and derivative futures based on advanced machine learning algorithms and customer data analysis.

The primary goal of the recommendation system is to enhance the investment experience by offering tailored suggestions that match each customer's risk tolerance, trading strategy, investment history, and preferences. This helps customers make informed decisions and optimize their investment portfolios.

## Functional Requirements

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

## Non-Functional Requirements

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

## Business model requirements

### Cross-selling

**Feature Description**: Recommend bonds, stocks, and portfolios to customers within the customer’s asset page or after they place an order.
**Functionalities**:
- Display recommendations based on the type of security purchased and the stock symbol
- Utilize phrases like "Investors like you often buy…" or "Investors who bought this stock also bought…"
- Integrate recommendations within the order confirmation page and follow-up emails.

| **Features**                                                                                            | **Where**                                             | **When**                                                             | **Type of display** | **Text**                                                                                                                                                                                                                 | **Notes**                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Suggest to optimize money with PineB when customer want to withdraw money                               | "Withdraw money" Screen                               | When Customers want to withdraw money                                | Pop up + email      | Instead of withdrawing your money from our securities account, you can choose to optimize your idle money with our PineB product, to earn a maximum … % per annum.  <br>Click on the link below to explore your options. | Email is considered to send later (send at the end of the day when customers have idle cash on account.)                                                                                      |
| Suggest to buy Pinefolio if customers buy a stock included in such portfolio.                           | Order Screen                                          | After a successful order is placed for a stock included in Pinefolio | Pop up + email      | Our …. Pinefolio, which outperforms VNIndex by …. percent, includes stock ……  <br>Click on the link below to explore …. Pinefolio and other investment portfolios from Pinetree.                                         | If stock X is included in both Pinefolio A and B, given that A performs better than B, A will be recommended  <br>  <br>Email is considered to send later (send when the order is completed.) |
| Suggest to register for Margin after buying a marginable stock (but not using margin)                   | Order Screen                                          | After a successful order is placed for a marginable stock            | Pop up              | … % of our customers who invest in stock ….use margin to maximize return on such stock.  <br>Please explore our margin program here                                                                                      |                                                                                                                                                                                               |
| Suggest to register for Derivatives after registerring for Margin successfully or buy a -CW successully | CW Order Screen or Margin Account Registration Screen | After successful registration of Margin account                      | Pop up + email      | … % of our customers who use margin also trade derivatives to maximize their return.  <br>Please explore our derivatives program here                                                                                    | Email is considered to send later (send at the end of the day customers successfully register for a Derivative)                                                                               |
### Upselling

**Feature Description**:  Recommend similar stocks to customers after they buy a different stock.
**Functionalities**:
- Identify stocks that similar to the one purchased.
- Suggest stocks that fit within the customer’s investment portfolio or confirmation screen after they place an order.
- Utilize phrases like "Investors like you often buy…" or "Investors who bought this stock also bought…"
- Highlight these recommendations on the purchase confirmation screen and within the app’s main feed

| **Features**                                          | **Where**    | **When**                                                                                                                                                                                    | **Type of display** | **Text**                                                                                                                          | **Priority** | **Notes**                                                                                                                                                                                                            |
| ----------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommend similar stocks based on performance         | Order screen | After an order is placed successfully  <br>Or after an order fails because of the lack of buying power  <br>(In the second case, recommmend stock that match the buying power of Customers) | Pop up              | Order Success!  <br>Investors who bought this stock also bought… because they have similar performance in the last 5 trading days | 1st          | If the stock price decrease in the last 5 trading days  <br>-> recommend based on investment patterns  <br>-> If there is no suitable investment patterns (ex, 1st time trading stocks), recommend based on industry |
| Recommend similar stocks based on industry            | Order screen | After an order is placed successfully  <br>Or after an order fails because of the lack of buying power  <br>(In the second case, recommmend stock that match the buying power of Customers) | Pop up              | Order Success!  <br>Investors who bought this stock also bought… because they are all in the …. industry                          | 3rd          | If the stock price decrease in the last 5 trading days  <br>-> recommend based on investment patterns  <br>-> If there is no suitable investment patterns (ex, 1st time trading stocks), recommend based on industry |
| Recommend similar stocks based on investment patterns | Order screen | After an order is placed successfully  <br>Or after an order fails because of the lack of buying power  <br>(In the second case, recommmend stock that match the buying power of Customers) | Pop up              | Order Success!  <br>Investors who bought this stock also bought…                                                                  | 2nd          | If the stock price decrease in the last 5 trading days  <br>-> recommend based on investment patterns  <br>-> If there is no suitable investment patterns (ex, 1st time trading stocks), recommend based on industry |
### Related Securities Recommendations

**Feature Description**: Show related stocks or securities that customers might be interested in when they view the details of another stock.
**Functionalities**:
- Analyze and display stocks with similar profiles, industry, or market performance.
- Include a “Related Stocks” section on the stock detail page.
- Provide information on why these stocks are related (e.g., same industry, high performance, similar investment patterns).

| **Features**                                          | **Where**           | **When**                                  | **Type of display**                                             | **Text**                                                                                                      | **Priority** | **Notes**                                                                                                                                                                                                            |
|:----------------------------------------------------- | ------------------- | ----------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Recommend similar stocks based on performance         | Stock Detail Screen | When Customers view the detail of a stock | Scrolling text, keep on the top even when customers scroll down | Investors who bought this stock also bought… because they have similar performance in the last 5 trading days | 1st          | If the stock price decrease in the last 5 trading days  <br>-> recommend based on investment patterns  <br>-> If there is no suitable investment patterns (ex, 1st time trading stocks), recommend based on industry |
| Recommend similar stocks based on industry            | Stock Detail Screen | When Customers view the detail of a stock | Scrolling text, keep on the top even when customers scroll down | Investors who bought this stock also bought… because they are all in the …. industry                          | 3rd          | If the stock price decrease in the last 5 trading days  <br>-> recommend based on investment patterns  <br>-> If there is no suitable investment patterns (ex, 1st time trading stocks), recommend based on industry |
| Recommend similar stocks based on investment patterns | Stock Detail Screen | When Customers view the detail of a stock | Scrolling text, keep on the top even when customers scroll down | % Investors (*) who bought this stock also bought…                                                            | 2nd          | If the stock price decrease in the last 5 trading days  <br>-> recommend based on investment patterns  <br>-> If there is no suitable investment patterns (ex, 1st time trading stocks), recommend based on industry |
### Personalized News Recommendations

**Feature Description**: Recommend news articles related to stocks, bonds, companies, and industries of interest to the customer.
**Functionalities**:
- Analyze customer’s past transactions, search history, watchlist, and portfolio to determine interests.
- Display relevant news articles on the app’s homepage and news section.
- Allow customers to provide feedback (like, dislike) to improve future recommendations.


| **Features**                                                                           | **Where**          | **When**                      | **Type of display**                                                 | **Text**                                                                                                                               | **Notes**                                                           |
| -------------------------------------------------------------------------------------- | ------------------ | ----------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Suggest news on customers's interest based on search history and watchlist             | Price Board + News | When logging into price board | - Scrolling text on Price Board  <br>Or  <br>- Sending notification | - Scrolling text: News summary content  <br>- Notification: News summary content                                                       | Max 5 news, News listed based on which interest Customers the most) |
| Allow customers to provide feedback (like, dislike) to improve future recommendations. | Price Board        | Whenever Customers want       | Button Like/Dislike under each news                                 | “Thank you for your detailed feedback. We truly appreciate the time you took to share your thoughts and the insights you’ve provided.” | Appear after the feedback is received                               |
# Model design and workflows

## Model design

![model_design](Model-design.drawio.svg)

### **User Data**
- **#U01: Customer Status Classification**: Phân loại trạng thái khách hàng thành các nhóm. Thông tin này giúp xác định các loại recommendation phù hợp cho từng nhóm khách hàng.:
    - Churn (rời bỏ), Inactive (không hoạt động), New (mới).
    - Active (hoạt động)
    - Reactive (tái kích hoạt). 
- **#U02: User Labeling Analysis**: Phân tích dữ liệu nhãn của người dùng, dựa trên hành vi sử dụng hoặc các thông tin có sẵn để cung cấp các yếu tố đầu vào cho các bước xử lý tiếp theo.
- **#U03: User-Item Rating**: Người dùng được đánh giá mức độ tương tác hoặc quan tâm đến các sản phẩm tài chính (Item) để hiểu rõ sự ưa thích của họ đối với từng loại sản phẩm.
- **#U04: User-Security Type Rating**: Xếp hạng mức độ quan tâm của người dùng đối với từng loại sản phẩm chứng khoán cụ thể như cổ phiếu, trái phiếu, hoặc các loại hình đầu tư khác.
- **#U05: User Similarity Scoring**: Tính toán điểm tương đồng giữa người dùng với nhau dựa trên các tiêu chí như lịch sử giao dịch, sở thích đầu tư nhằm gợi ý các sản phẩm mà những người dùng tương tự đã quan tâm.
### **Item Data**
- **#I01: Item Labeling Analysis**: Phân tích nhãn cho các sản phẩm tài chính dựa trên các yếu tố như khối lượng giao dịch, tính phổ biến, và loại ngành nghề (sector).
- **#I02: Portfolio Detection by Characteristics**: Xác định 1 danh mục đại diện cho một yếu tố nào đó:
    - High performance (hiệu suất cao)
    - Popular (phổ biến)
    - Sector-specific (theo ngành)
    - New Items (sản phẩm mới)
- **#I03: Item Similarity Scoring**: Tính điểm tương đồng giữa các sản phẩm tài chính dựa trên các yếu tố như hiệu suất, loại hình đầu tư và các yếu tố khác.
### **News Data**
- **#N01: News Labeling Analysis**: Phân tích và gắn nhãn cho các bài báo, tin tức dựa trên các tiêu chí như ngành nghề, cảm xúc, chủ đề, và các nhãn liên quan đến mã chứng khoán (symbol tags).
- **#N02: News Similarity Scoring**: Tính điểm tương đồng giữa các tin tức, giúp gợi ý các bài viết có nội dung tương tự cho người dùng.
- **#N03: Related News to Items**: Liên kết tin tức phù hợp với các sản phẩm tài chính, từ đó cung cấp tin tức có liên quan đến từng loại chứng khoán cụ thể mà người dùng đang quan tâm.
### **Hệ thống recommendation**
- **Base-models:**
    - **#R01:** **Popularity Portfolio Recommendation (In-active + New)**: Gợi ý các danh mục đầu tư phổ biến.
    - **#R02: High Performance Portfolio Recommendation** **(In-active + New)**: Gợi ý các danh mục có hiệu suất cao.
    - **#R03: Similar User Recommendation (Active + Re-active)**: Gợi ý các sản phẩm mà những người dùng có điểm tương đồng với người dùng hiện tại đã quan tâm.
    - **#R04: Preference Sector Recommendation (Active + Re-active)**: Đề xuất sản phẩm thuộc cùng ngành với những sản phẩm mà người dùng đã đầu tư hoặc quan tâm.
    - **#R05: New Items Recommendation (Active + Re-active)**: Gợi ý các sản phẩm mới.
    - **#R06: Similar Items Recommendation (Active + Re-active)**: Đề xuất các sản phẩm tương tự dựa trên các yếu tố như loại sản phẩm, hiệu suất đầu tư.
    - **#R07: User Profile Info. Rec. (Wide & Deep Learning) (Active)**: Sử dụng mô hình học sâu để phân tích thông tin chi tiết hồ sơ người dùng, từ đó đưa ra các gợi ý cá nhân hóa.
    - **#R08: Recent Behavior Rec. (SASRec) (Active)**: Dựa vào các hành vi gần đây để gợi ý các item có khả năng người dùng đang quan tâm.

- **Meta-models:**
    - **#M01: Up-sell Recommendation**: Đề xuất các sản phẩm cùng loại.
    - **#M02: Cross-sell Recommendation**: Đề xuất các sản phẩm khác loại (cross-sell) dựa trên mức độ phù hợp với các loại hình đầu tư mà người dùng có thể quan tâm.
    - **#M03: Related Securities Recommendation**: Đề xuất các sản phẩm chứng khoán có liên quan đến item cụ thể.
    - **#M04: News Recommendation to User**: Gợi ý các bài báo phù hợp với sở thích và hành vi của người dùng. Tin tức phải gần với thời gian thực để đảm bảo tính cập nhật.
    - **#M05: News Recommendation to Item**: Đề xuất các tin tức liên quan đến sản phẩm tài chính mà người dùng đã hoặc đang quan tâm.
## Workflows

![model_wf](ML-system-architecture.drawio.svg)
## Monitoring

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
# Appendix

## Recommendation Algorithms Research

### Algorithms research

#### Content-based Filtering

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
### ML Algorithms comparation

| Algorithms     | Collaborative filtering                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Content-based filtering                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Hybrid Recommender                                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| How it works ? | Use clustering models, user-based k-nearest neighbors, matrix factorization, and Bayesian networks to group customer or items into groups with the same interaction.![[Pasted image 20240531130725.png]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Considers the item's characteristics, such as price, volume, sector, group defined by assigned keywords and tags, then group items to group with the same characteristics.![[Pasted image 20240531131409.png]]                                                                                                                                                                                                                                                                        | Combining collaborative and content-based filtering scoring with the difference weighting, depends on each different group. |
| Sub-model      | **Item-base** and **User-base**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Item characteristics and Demographics user                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                             |
| Prods          | **Extremely accurate** and provide effective suggestions, especially when relying on context-aware filtering.<br><br>**Predict customers' interest** in a product they didn't know existed by observing what caught the attention of similar users.<br><br>**No need to understanding the nature of each item**, which eliminates the need for detailed product descriptions.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Handle the new items with no interaction yet<br><br>Apply for recommendation use for searching by text/ characteristic                                                                                                                                                                                                                                                                                                                                                                | Enhance recommendation systems' performance.                                                                                |
| Cons           | **Cold start problem:** providing valuable suggestions to new users with no purchase history can be challenging considering the only available parameters (gender, age, etc.).<br><br>**Scalability:** using this algorithm to search for purchase patterns among a growing number of customers and products requires significant computational power.<br><br>**Rich-get-richer effect:** algorithms generally recommend products with many excellent reviews, increasing their popularity at the expense of new items.<br><br>**Data sparsity:** in cases with a large product catalog, each item may not have a sufficient number of user reviews to analyze, reducing the recommendations' accuracy.<br><br>**Shilling attacks:** new products are vulnerable to rating manipulations (such as negative reviews from competitors). | The tagging procedure implies a massive workload, especially on large platforms or marketplaces.<br><br>The cold start issue of collaborative filtering is still there, although less critical than in collaborative filtering, as the historical data associated with new customers is very limited.<br><br>Algorithms can be rather conservative, recommending categories of products and content already purchased by a user and avoiding new, potentially interesting categories. | Merging both mechanisms into a single system requires more complex architectures and superior computing power.              |

### Advanced feature (planned for development)
- Session-Based Recommendation : hệ thống recommendation chứa yếu tố time session
- Thuật toán LSTM dự đoán sản phẩm có khả năng mua tiếp theo của khách hàng dựa vào lịch sử mua sắm.
- Sử dụng các thuật toán NLP (Natural language processing - Xử lý ngôn ngữ tự nhiên) để phân tích các thông tin như phần tên sản phẩm, mô tả sản phẩm, comment khách hàng về sản phẩm để tìm ra sản phẩm tương đồng.
- Sử dụng AutoEncoder để tìm kiếm sản phẩm tương đồng, khách hàng tương đồng. Về auto encoder có thể xem thêm tại [Bài 3 - Mô hình Word2Vec](https://phamdinhkhanh.github.io/2019/04/29/ModelWord2Vec.html).
- Các hệ thống search engine dựa trên hình ảnh của sản phẩm.
- Sử dụng reignforcement learning để recommend sản phẩm dựa trên các dự báo về hành vi tiếp theo của khách hàng.
- Sử dụng [LDA](https://phamdinhkhanh.github.io/2019/09/08/LDATopicModel.html) để clustering các nhóm sản phẩm có chung đặc điểm và có thể thay thế được cho nhau.
- Thuật toán association để tìm các sản phẩm hoặc nhóm khách hàng có mối liên hệ trong hành vi mua sắm thông qua một chỉ số là levarage.

## Data collection

### Customer data
#### Customer Demographics
- Customer ID
- Age
- Gender
- Location
- Income level
- Occupation
- Segmentation
- Balance Status
#### Behavioral Data
- Purchase history (stocks bought, quantities, and dates)
- Browsing history (stocks viewed, search terms used)
- Interaction history (clicks, likes, comments, shares)
- Trading patterns (frequency, volume, type of trades, orders history)
- App usage patterns (login, screen)
#### Financial Data
- Portfolio holdings
- Account balance
- Transaction history
- Risk tolerance
### Product information
#### Stock
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
#### Bond
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
#### Derivative
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
### Market data
#### Market Indicators
- Stock market indices (e.g., VN30, VNINDEX)
- Interest rates
- Inflation rates
- Economic indicators (e.g., GDP, unemployment rates)
#### Market Trends
- Sector performance trends
- Industry performance trends
- Global market conditions
- Regulatory changes

## Schema Design

### Table schema

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

### Data Storage Strategy
- Denormalization: denormalize the data by embedding frequently accessed metadata within the recommendation table.
- Partitioning by `timestamp`
- Clustering by `user_id`
- Partition Expiration:
```sql
ALTER TABLE `project_id.dataset_id.user_product_recommendations` SET OPTIONS ( expiration_timestamp = TIMESTAMP "2025-01-01 00:00:00 UTC" )
```


# Refs
1. https://www.itransition.com/machine-learning/recommendation-systems
2. https://phamdinhkhanh.github.io/2019/11/04/Recommendation_Compound_Part1.html
3. https://phamdinhkhanh.github.io/2019/12/26/Sorfmax_Recommendation_Neural_Network.html
4. https://phamdinhkhanh.github.io/2020/02/11/NARSyscom2015.html
5. https://neptune.ai/blog/recommender-systems-lessons-from-building-and-deployment

# # Timeline

[Product_Recommendation_Plan.xlsx](https://hftvietnam.sharepoint.com/:x:/s/da/EW5NW6zOj_tJgmC0wq7fHAMB-lqcxi7Pn5Z0UWw77Mgn7w?e=49nkct&nav=MTVfezgxMjU0ODlDLUE5OUItNDI1Ny04QUE2LTVEODNFQ0NBQjBEQn0)
