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


## **Danh sách model**
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
- Model chấm điểm khách hàng với sector #
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

### Model phân loại trạng thái khách hàng (#M1)

Phân loại khách hàng thành các nhóm:
- Khách hàng `inactive`
- Khách hàng `active`
- Khách hàng mới `new`
- Khác hàng sắp rời bỏ `re-activated`
- Khách hàng sắp rời bỏ `churn`

### Model phân tích đặc điểm khách hàng (#M2)
- Mức độ biến động danh mục
- Thời gian nắm giữ
- Đa dạng hoá danh mục
- Mức độ phổ biến danh mục
- Tỷ lệ sử dụng đòn bẩy
- Chỉ số tài chính cá nhân:
	- Khả năng chấp nhận rủi ro (risk tolerance)
	- Giá trị danh mục (portfolio value) 
	- Dòng tiền (cash flow).

**Sử dụng kỹ thuật phân tích thời gian nắm giữ nâng cao**: Sử dụng survival analysis hoặc time-to-event modeling để dự đoán thời gian khách hàng nắm giữ các loại tài sản.
**Tích hợp học sâu**: Dùng mô hình deep learning hoặc autoencoder để tìm các biểu hiện tiềm ẩn (latent features) về đặc điểm tài chính của khách hàng.

### Model phân tích sản phẩm (#M3)

Đặc điểm phân tích:
- Có phải là sản phẩm mới ? (Stock mới list sàn, chứng quyền mới list, bond mới phát hành, ETF mới, hợp đồng phái sinh. )
- Mức độ phổ biến - được giao dịch nhiều : top những mã được giao dịch nhiều, thanh khoản lớn, được đầu tư nhiều,...
- ...

- **Sử dụng kỹ thuật embedding**: Tạo ra embedding cho sản phẩm để có thể đo độ tương đồng giữa các sản phẩm dựa trên tính năng hoặc hành vi giao dịch. Mô hình này có thể học từ các yếu tố như loại tài sản, biến động giá, thanh khoản.
- **Tích hợp các chỉ số ngoại biên**: Như tin tức, sentiment analysis từ dữ liệu ngoài (báo cáo tài chính, tin tức thị trường, mạng xã hội) để phân tích mức độ phổ biến thực sự của sản phẩm.
- **Phân tích chu kỳ thị trường**: Đưa vào các yếu tố như chu kỳ ngành nghề, hoặc xu hướng kinh tế vĩ mô để dự đoán sản phẩm nào có thể nổi bật trong giai đoạn sắp tới.

### Model chấm điểm khách hàng với sector 

- **Kết hợp sector preference với các chỉ số khác**: Sử dụng kỹ thuật collaborative filtering để dự đoán các ngành mà khách hàng có thể quan tâm dựa trên sự tương đồng với các khách hàng khác.
- **Phân tích cảm xúc với từng sector**: Áp dụng NLP vào các bản tin hoặc báo cáo liên quan đến các ngành nghề để xem xét cảm xúc thị trường.

### Model gom nhóm sản phẩm (#M4)

- **Sử dụng k-means hoặc hierarchical clustering cho các loại sản phẩm**: Phân loại sản phẩm dựa trên đặc điểm và hiệu suất. Có thể dùng embedding của sản phẩm để đo khoảng cách.
- **Tích hợp thêm thông tin về xu hướng thị trường**: Gom nhóm sản phẩm không chỉ dựa trên đặc tính mà còn dựa vào việc chúng phù hợp với xu hướng thị trường hiện tại như thế nào.

### Model gom nhóm khách hàng (#M5)

- **Sử dụng phân cụm đa chiều (multidimensional clustering)**: Gom nhóm khách hàng dựa trên nhiều yếu tố như hành vi giao dịch, khả năng chịu rủi ro, thời gian giao dịch và tài sản sở hữu.
- **Áp dụng clustering động**: Sử dụng mô hình clustering theo thời gian (time-dependent clustering) để theo dõi sự thay đổi trong hành vi khách hàng và cập nhật mô hình phân cụm.

### Model đề xuất sản phẩm phổ biến (#M6)

- **Sử dụng collaborative filtering nâng cao**: Kết hợp thêm với các kỹ thuật implicit feedback từ hành vi giao dịch, như hành động xem, tìm kiếm nhưng không mua.
- **Sử dụng reinforcement learning**: Để liên tục cập nhật danh sách sản phẩm dựa trên phản hồi của khách hàng sau mỗi gợi ý.

### Model đề xuất sản phẩm mới (#M7)


- **Dự đoán sự quan tâm sản phẩm mới**: Sử dụng mô hình time series để dự đoán sản phẩm nào sẽ có sự gia tăng quan tâm trong tương lai. Áp dụng các mô hình ARIMA, Prophet hoặc LSTM.
- **Phân tích thị trường cho sản phẩm mới**: Tích hợp thông tin từ bên ngoài như tin tức, đánh giá của các chuyên gia để dự đoán xu hướng của sản phẩm mới.

### Model đề xuất sản phẩm tương tự với danh mục hiện tại (#M8)


- **Tạo vector embedding danh mục đầu tư**: Sử dụng phương pháp matrix factorization hoặc neural collaborative filtering để biểu diễn danh mục đầu tư dưới dạng vector, và tìm các sản phẩm tương đồng trong không gian này.
- **Kết hợp với kỹ thuật diversification**: Không chỉ đề xuất sản phẩm tương tự mà còn đề xuất sản phẩm giúp đa dạng hóa rủi ro cho danh mục của khách hàng.

### 10. Model đề xuất theo dữ liệu trạng thái (#M9)


- **Deep Learning với embedding cho từng khách hàng và sản phẩm**: Sử dụng mạng deep neural network để học các biểu diễn tiềm ẩn từ dữ liệu trạng thái của khách hàng.
- **Contextual Bandit**: Kết hợp thêm reinforcement learning để tối ưu hóa việc lựa chọn sản phẩm theo thời gian dựa trên trạng thái và phản hồi của khách hàng.

### 11. Model đề xuất theo chuỗi hành vi (SASRec) (#M10)


- **Sử dụng Transformer-based model**: SASRec là một mô hình mạnh, tuy nhiên có thể cải thiện bằng cách áp dụng Transformer với attention mechanism tốt hơn để phân tích chuỗi hành vi dài.
- **Áp dụng thêm layer về temporal patterns**: Thêm các layers để phát hiện xu hướng ngắn hạn và dài hạn trong hành vi của khách hàng.

### 12. Model hybrid recommend (#M11)


- **Kết hợp nhiều chiến lược**: Thay vì chỉ sử dụng #M1 để phân loại, có thể kết hợp nhiều mô hình như #M5 (phân nhóm khách hàng) và #M2 (đặc điểm cá nhân hóa) để tạo ra các gợi ý có độ chính xác cao hơn.
- **Meta-learning**: Áp dụng meta-learning để tự động học cách kết hợp nhiều mô hình recommendation sao cho hiệu quả nhất, tùy thuộc vào từng khách hàng và trạng thái thị trường.
- **Ensemble models**: Xây dựng các mô hình ensemble (bagging, boosting) để tổng hợp kết quả từ nhiều mô hình khác nhau, giúp tăng độ chính xác và tính đa dạng của gợi ý.

### **1. Quy trình kết hợp các mô hình:**

#### **Bước 1: Phân loại khách hàng (M1)**

- **Input**: Dữ liệu hồ sơ khách hàng (demographic data), trạng thái tài khoản (account status), hành vi sử dụng app.
- **Output**: Phân loại khách hàng thành `inactive`, `active`, `new`, `reactivated`, `churn`.
- **Tác động**: Dữ liệu từ model này sẽ giúp chọn chiến lược gợi ý phù hợp cho từng loại khách hàng. Ví dụ:
    - Khách hàng `inactive` có thể nhận các gợi ý tập trung vào sản phẩm mới, sản phẩm phổ biến.
    - Khách hàng `active` sẽ nhận được gợi ý đa dạng hơn như các sản phẩm tương tự hoặc tùy chỉnh sâu hơn.

#### **Bước 2: Phân tích đặc điểm khách hàng (M2)**

- **Input**: Dữ liệu giao dịch, danh mục đầu tư, thông tin tài chính cá nhân.
- **Output**: Các chỉ số như độ biến động danh mục, mức độ đa dạng hóa, thời gian nắm giữ, tỷ lệ đòn bẩy.
- **Tác động**: Cung cấp thông tin chi tiết về khách hàng giúp tinh chỉnh các gợi ý. Ví dụ:
    - Khách hàng có tỷ lệ sử dụng đòn bẩy cao sẽ nhận được gợi ý về các sản phẩm có tính đòn bẩy hoặc sản phẩm bảo vệ rủi ro (hedging).

#### **Bước 3: Phân tích sản phẩm (M3)**

- **Input**: Dữ liệu sản phẩm (cổ phiếu, trái phiếu, ETF, chứng quyền,...), biến động giá, thanh khoản, mức độ phổ biến.
- **Output**: Phân loại sản phẩm (mới, phổ biến, thanh khoản cao,...).
- **Tác động**: Kết hợp với M2 để tìm ra sản phẩm phù hợp với đặc điểm khách hàng. Ví dụ:
    - Khách hàng ưa thích sản phẩm phổ biến sẽ nhận được các gợi ý từ danh sách sản phẩm hot, thanh khoản cao.

#### **Bước 4: Gom nhóm khách hàng và sản phẩm (M4, M5)**

- **Input**: Dữ liệu lịch sử giao dịch của khách hàng, danh mục đầu tư, và phân tích sản phẩm.
- **Output**: Gom nhóm khách hàng có hành vi giao dịch tương đồng và gom nhóm sản phẩm dựa trên đặc điểm.
- **Tác động**: Kết hợp các nhóm khách hàng với nhóm sản phẩm phù hợp. Ví dụ:
    - Khách hàng trong một nhóm cụ thể sẽ được gợi ý sản phẩm mà các khách hàng trong cùng nhóm đã đầu tư.

#### **Bước 5: Đề xuất sản phẩm phổ biến và mới (M6, M7)**

- **Input**: Kết quả từ M1, M2 và M3.
- **Output**: Gợi ý sản phẩm phổ biến và sản phẩm mới dựa trên hành vi và đặc điểm của khách hàng.
- **Tác động**: Ví dụ, khách hàng mới có thể nhận gợi ý sản phẩm phổ biến để khởi đầu, trong khi khách hàng lâu năm có thể nhận gợi ý sản phẩm mới để khám phá.

#### **Bước 6: Đề xuất sản phẩm tương tự với danh mục hiện tại (M8)**

- **Input**: Danh mục đầu tư hiện tại của khách hàng, embedding của sản phẩm.
- **Output**: Gợi ý các sản phẩm tương tự dựa trên danh mục hiện tại của khách hàng.
- **Tác động**: Khuyến nghị các sản phẩm có tính chất tương tự để giúp khách hàng tiếp tục đầu tư trong các lĩnh vực họ quen thuộc.

#### **Bước 7: Đề xuất theo dữ liệu trạng thái (M9) và chuỗi hành vi (M10)**

- **Input**: Lịch sử tương tác của khách hàng trên ứng dụng, trạng thái tài khoản.
- **Output**: Gợi ý dựa trên các hành vi sử dụng gần đây, ví dụ: các sản phẩm mà khách hàng đã tìm kiếm, xem nhưng chưa mua.
- **Tác động**: Cập nhật gợi ý theo thời gian thực để tăng tính cá nhân hóa dựa trên hành vi.

#### **Bước 8: Hybrid Recommendation (M11)**

- **Input**: Tất cả các output từ M1 đến M10.
- **Output**: Tổng hợp kết quả từ các mô hình trên để đưa ra danh sách sản phẩm cuối cùng.
- **Tác động**: Đưa ra các gợi ý cân bằng giữa sự phổ biến, sự tương đồng với danh mục hiện tại và các sản phẩm mới phù hợp với sở thích cá nhân.

```plaintext
                          ┌─────────────────────┐
                          │ Khách hàng & dữ liệu│
                          └─────────────────────┘
                                   │
                                   ▼
                      ┌────────────────────────────┐
                      │ Model phân loại khách hàng │ (#M1)
                      └────────────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────┬──────────────────────────────┐
        ▼                              ▼                              ▼
 ┌────────────────┐            ┌────────────────┐             ┌───────────────────┐
 │ Phân tích đặc  │            │ Phân tích sản  │             │ Gom nhóm khách    │
 │ điểm khách hàng│ (#M2)      │ phẩm (#M3)     │             │ hàng và sản phẩm  │ (#M5)
 └────────────────┘            └────────────────┘             └───────────────────┘
        │                              │                              │
        ▼                              ▼                              ▼
 ┌──────────────────────────┐   ┌────────────────────┐     ┌────────────────────────┐
 │ Phân tích tương đồng và  │   │ Đề xuất sản phẩm    │     │ Đề xuất sản phẩm       │
 │ gợi ý theo danh mục hiện │   │ phổ biến & sản phẩm │     │ tương tự (#M8)         │
 │ tại (#M8)                │   │ mới (#M6, #M7)      │     └────────────────────────┘
 └──────────────────────────┘   └────────────────────┘
         │                              │
         ▼                              ▼
  ┌────────────────────────────┐    ┌────────────────────────────┐
  │ Gợi ý theo chuỗi hành vi   │    │ Gợi ý theo dữ liệu trạng    │
  │ (#M10 - SASRec)            │    │ thái (#M9)                  │
  └────────────────────────────┘    └────────────────────────────┘
                   │                               │
                   ▼                               ▼
        ┌───────────────────────────────────────────────────────┐
        │              Model hybrid recommendation (#M11)        │
        └───────────────────────────────────────────────────────┘
                                   │
                                   ▼
                          ┌───────────────────────┐
                          │  Danh sách gợi ý cuối │
                          │     cho khách hàng    │
                          └───────────────────────┘

```
### **Giải thích chi tiết về flowchart:**

1. **Input từ dữ liệu khách hàng**: Dữ liệu về hành vi, danh mục đầu tư, trạng thái tài khoản của khách hàng sẽ được đưa vào model **phân loại khách hàng (M1)** để xác định khách hàng thuộc nhóm nào.
    
2. **Phân tích đặc điểm khách hàng (M2)** và **phân tích sản phẩm (M3)** sẽ được áp dụng để hiểu sâu hơn về khách hàng và các sản phẩm tiềm năng.
    
3. **Gom nhóm khách hàng và sản phẩm (M5)** sẽ được sử dụng để nhóm các khách hàng có đặc điểm tương tự và cung cấp gợi ý theo nhóm.
    
4. **Đề xuất sản phẩm phổ biến (M6)** và **mới (M7)** sẽ đưa ra các sản phẩm phù hợp với từng khách hàng dựa trên xu hướng và sở thích.
    
5. **Gợi ý sản phẩm tương tự (M8)** sẽ tạo ra gợi ý dựa trên danh mục hiện tại của khách hàng.
    
6. **Mô hình theo chuỗi hành vi (M10)** và **trạng thái tài khoản (M9)** sẽ giúp gợi ý sản phẩm theo hành vi và ngữ cảnh sử dụng app gần đây.
    
7. **Cuối cùng, mô hình Hybrid (M11)** sẽ kết hợp tất cả các output từ các mô hình trên để đưa ra danh sách gợi ý cuối cùng, mang tính toàn diện và cá nhân hóa nhất cho khách hàng.



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