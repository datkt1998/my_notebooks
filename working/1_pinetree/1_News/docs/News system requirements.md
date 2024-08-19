# 1 News Crawler Requirements

## 1.1 **Introduction**

News crawler gather and collect relevant news articles and information from various news sources. The news crawler is designed to search and index news content based on specific keywords, topics, or categories. This process allows the news recommendation system to provide users with personalized and up-to-date news articles that align with their interests and preferences. By continuously crawling and analyzing news data, the recommendation system can offer a curated selection of articles that are most likely to be of interest to the user, enhancing their overall news reading experience.

## 1.2 **Functional Requirements**

Functional requirements of news crawler system outline the features and functionalities necessary for the crawler to effectively gather, process, and manage news articles from various online sources. These requirements include tasks such as Data collection, Content filtering, Dynamic pipeline operations, Monitoring, Search and retrieval, Security, scalability, and compliance with legal and ethical standards.
### 1.2.1 **Data Collection**
- **Web crawling**: The crawler should be able to navigate through web pages, following links to discover and retrieve news articles from designated sources.
	- Get content from API message.
	- Get content from URL.
	- Get content from web crawling response.
- **Content Extraction**: The crawler shall be able to extract relevant information such as the article title, author, publication date, content, and URL.

### 1.2.2 **Content Filtering**
- The system shall provide options to filter news articles based on predefined criteria such as keywords, categories, or publication dates.
### 1.2.3 **Dynamic pipeline operations**
- **Automation** | **Manual pipeline**: The system shall have scheduling capabilities to automate/or manual the crawling process at predefined intervals.
- **Performance Optimization**: The crawler should be optimized for performance to handle a high volume of concurrent crawling requests efficiently
- **Error Handling**: It should incorporate mechanisms for handling errors gracefully, including retrying failed crawling tasks and logging error messages for troubleshooting.
### 1.2.4 **Monitoring**
- System captures various events, activities, and messages generated during the crawling process: 
	- Start and end times of crawling tasks
	- URLs visited and crawled
	- Success or failure of each crawling attempt
	- Errors encountered during crawling
	- Resource consumption metrics (e.g., memory usage, CPU utilization)
	- Relevant metadata of crawled content (e.g., publication date, author)
- It shall provide monitoring tools to track the status of crawling tasks and detect any failures or issues.
### 1.2.5 **Security**
- The system should implement authentication and authorization mechanisms to restrict access to authorized users and protect sensitive data.

## 1.3 **Non-Functional Requirements**

Non-functional requirements (NFRs) of a news crawler refer to the characteristics and constraints that govern the system's operation and performance, rather than specific features or functionalities. These requirements describe how the system should behave, perform, and interact with its environment.
### 1.3.1 **Performance**
- The system shall be capable of handling a high volume of concurrent crawling requests efficiently by multi-processing or multi-thearding.
- It shall have low latency for both crawling and retrieval operations.
### 1.3.2 **Scalability**
- The system architecture shall be designed to scale horizontally to accommodate increased workload and data volume.
- It shall support distributed processing and storage to distribute the load across multiple nodes.
### 1.3.3 **Reliability**
- The system shall be robust and resilient to handle failures gracefully.
- It shall incorporate mechanisms for retrying failed crawling tasks and recovering from errors.
### 1.3.4 **Maintainability**
- The system shall be modular and well-documented to facilitate ease of maintenance and future enhancements.
- It shall support version control and automated testing for codebase stability.
	Unit-test + integration test → test coverage >80%
### 1.3.5 **Compliance**
- The crawler should comply with copyright laws and terms of service of crawled websites to ensure legal and ethical use of content.
- System shall not violate any content usage policies or regulations.

## 1.4 **Cloud Platform Requirements** 

### 1.4.1 **Compute Engine:**
- Provision virtual machines to host the crawler service.
- Ensure sufficient CPU and memory resources to handle crawling tasks efficiently.
### 1.4.2 **Storage**
- Utilize Google Cloud Storage (GCS) / BigQuery for storing crawled data, logs, and configuration files.
### 1.4.3 **Networking**
- Configure Virtual Private Cloud (VPC) networks to secure communication between components.
### 1.4.4 **Identity and Access Management (IAM)**
- Define IAM roles and permissions to control access to GCP resources.
- Implement least privilege principles to restrict access to sensitive data and services.
### 1.4.5 **Monitoring and Logging**
- Write log to BigQuery datatable and use Locker with dashboard to track
- ~~Utilize Stackdriver Monitoring to track resource usage, performance metrics, and health checks.~~
- ~~Configure Stackdriver Logging to capture logs and events generated by the crawler service.~~
### 1.4.6 **Security**
- Enable VPC Service Controls to restrict data access within specified geographical boundaries.
- ~~Implement Firewall Rules and Security Groups to control inbound and outbound traffic.~~
### 1.4.7 **Deployment and Orchestration**
- Use Google Kubernetes Engine (GKE) to deploy and manage containerized crawler applications.
- ~~Leverage Cloud Build for continuous integration and deployment pipelines.~~
### 1.4.8 **Data Processing**
- Utilize Google Cloud Dataflow for stream and batch processing of crawled data.
- Integrate with BigQuery for data warehousing and analytics capabilities.
### 1.4.9 **Scalability**
- Configure autoscaling policies to automatically adjust compute resources based on workload demand.
- ~~Utilize managed services like Memorystore for Redis to handle caching and improve performance.~~
### 1.4.10 **Cost Management**
- Implement budget alerts and billing reports to monitor and control costs.
- Utilize pricing calculators to estimate the cost of running the crawler service based on resource usage.
### 1.4.11 **Integration and APIs**
- Integrate with Google Cloud APIs for services like Cloud Storage, Pub/Sub, and BigQuery.
- Leverage third-party APIs for additional functionality such as text analysis or content enrichment.
## 1.5 **Assumptions and Dependencies**

### 1.5.1 **Internet Connectivity**

- The system assumes a stable internet connection for accessing and crawling online news sources.
- It may be affected by network latency and bandwidth limitations.
### 1.5.2 **Third-Party Dependencies**

- The system may depend on third-party libraries or APIs for certain functionalities such as HTML parsing or text extraction.
- It shall manage dependencies and ensure compatibility and version constantly with external services.
## 1.6 **Data sources Information requirements**

**Table config**

| **Requirement**          | **Description**                                                                               | **Example**                                                                                |
| ------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Source ID                | Create ID source to identify the source config                                                | cafef_01                                                                                   |
| Source Name              | The name of source ID                                                                         | CafeF kinh doanh                                                                           |
| Source URL               | The URL of the news source website or RSS feed.                                               | [https://cafef.vn/thi-truong-chung-khoan.chn](https://cafef.vn/thi-truong-chung-khoan.chn) |
| Trust score              | The news site's trust score                                                                   | 10                                                                                         |
| Source Type              | Specify if the source is a website, RSS feed, social media platform, etc.                     | Website                                                                                    |
| Content Categories       | List of categories or topics covered by the news source (e.g., politics, sports).             | Market, Trading, Macro                                                                     |
| Language                 | Language(s) in which the news articles are published.                                         | Vietnamese,                                                                                |
| Geographic Region        | The region or country covered by the news source.                                             | Viet Nam                                                                                   |
| Update Frequency         | How often the news source publishes new articles (e.g., hourly, daily).                       | Daily at 6AM                                                                               |
| Access Restrictions      | Any access restrictions or subscription requirements for accessing the source.                | None                                                                                       |
| Data Format              | Format of the data provided by the source (e.g., HTML, XML, JSON).                            | HTML                                                                                       |
| Content Extraction Rules | Rules or patterns for extracting relevant information from the source’s content.              | Headline: `<h1>`, Article Body: `<p>`                                                      |
| Authentication           | Authentication method required to access the source (e.g., API key, OAuth).                   | API Key                                                                                    |
| Pagination               | If the source paginates its content, specify pagination rules for retrieving articles.        | Pagination parameter: page=1                                                               |
| Filtering Options        | Any options for filtering articles based on criteria such as keywords or dates.               | Keywords: “COVID-19”, Date Range: 2022-01-01 to 2022-12-31                                 |
| Timeout                  | Specifies the maximum time allowed for a request to the source before timing out              | 30                                                                                         |
| Error Handling           | Procedures for handling errors or failed requests when accessing the source.                  | Retry 3 times, log errors                                                                  |
| Headers                  | Additional HTTP headers to include in requests to the source.                                 | text/html                                                                                  |
| Proxy Settings           | Configuration for using proxies to access the source.                                         | [http://proxy.example.com](http://proxy.example.com/)                                      |
| Encoding                 | Specifies the character encoding used for the source's content.                               | UTF-8                                                                                      |
| Max Depth                | Maximum depth of nested links to follow during crawling.                                      | 3                                                                                          |
| Rate Limiting            | Limits the number of requests per unit time to the source to avoid overloading it.            | 30 minutes                                                                                 |
| Crawl Delay              | Specifies a delay between successive requests to the source to avoid being blocked.           | 5                                                                                          |
| Data Transformation      | Rules or scripts for transforming or cleaning the extracted data.                             | clean_html                                                                                 |
| Metadata Extraction      | Rules for extracting metadata such as author, publication date, and article category.         | True                                                                                       |
| Content Filtering        | Additional filtering options such as content length, readability, or sentiment analysis.      | Length = 100                                                                               |
| Content Enrichment       | Integration with external services or APIs to enrich the content with additional information. | API key : Sentiment Analysis API                                                           |

**Json config:**

```yaml
source_config:
  - name: "Example News"
    url: "[https://www.example.com/news](https://www.example.com/news)"
    type: "Website"
    score: 10
    categories:
      - "Politics"
      - "Business"
      - "Technology"
    language: "English"
    region: "United States"
    update_frequency: "Daily"
    access_restrictions: "None"
    data_format: "HTML"
    extraction_rules:
      - field: "Headline"
        pattern: "<h1>(.*?)<\/h1>"
      - field: "Article Body"
        pattern: "<p>(.*?)<\/p>"
    authentication: "API Key"
    pagination:
      parameter: "page"
      value: "1"
    filters:
      - type: "Keywords"
        keywords: ["COVID-19", "pandemic"]
      - type: "Date Range"
        start_date: "2022-01-01"
        end_date: "2022-12-31"
    error_handling:
      retries: 3
      log_errors: true
    timeout: 30
    user_agent: "MyCrawler/1.0"
    headers:
      - name: "Accept"
        value: "text/html"
    proxy_settings:
      use_proxy: true
      proxy_url: "[http://proxy.example.com](http://proxy.example.com/)"
    encoding: "UTF-8"
    max_depth: 3
    rate_limiting:
      requests_per_minute: 100
    crawl_delay: 5
    geolocation: "US"
    ssl_verification: true
    data_transformation: "clean_html"
    metadata_extraction: true
    content_filtering:
      - type: "Content Length"
        min_length: 100
    content_enrichment:
      - service: "Sentiment Analysis API"
        api_key: "API_KEY"
```

# 2 News classification requirements

Develop and deploy a news classification system on GCP that categorizes news articles based on category, sector, and sentiment. 
- Develop a robust news classification model capable of categorizing news articles by category, sector, and sentiment.
- Deploy the model on GCP to ensure scalability, reliability, and accessibility.
- Implement an API for seamless interaction with the model, allowing users to input news articles and receive classification results.
- Enable performance tracking, operational monitoring, and batch tuning functionalities to continuously improve the model over time.
## 2.1 **Architecture:**

- **Data Preparation:** Gather a diverse dataset of labeled news articles including various categories, sectors, and sentiment labels. The system will accept input consisting of the article's title, content, brief summary, tags, topic, and keywords.
	-   Acquire a dataset of news articles with labels for category, sector, and sentiment.
- **Preprocessing:** Clean and preprocess the input data, including text normalization, tokenization, stop word removal, and lemmatization.
	- Preprocess the data to clean and tokenize the text, remove stop words, and perform text normalization.
- **Feature Extraction:** Extract features from the preprocessed text data using techniques like TF-IDF, word embeddings (e.g., Word2Vec, GloVe), and contextual embeddings (e.g., BERT).
- **Model Selection:** Train and deploy multiple classification models such as SVM, Random Forest, and deep learning models like CNNs or RNNs for category, sector, and sentiment classification.
- **Model Deployment:** Deploy the trained models on Google Cloud Platform using services like AI Platform or Kubernetes Engine for efficient scaling and management.
	- Containerize the APIs using Docker for deployment on GCP.
- **API Deployment:** Deploy the trained models on GCP using services like Google Kubernetes Engine (GKE) or Cloud Run to create APIs for real-time inference.
	- Develop APIs using Flask or FastAPI to accept news article inputs and return classification results.
    - Deploy the containerized APIs on GCP, either using Google Kubernetes Engine (GKE) or Cloud Run for scalable and efficient inference.
- **Monitoring and Logging:** Implement monitoring and logging mechanisms using Google Cloud Monitoring and Logging to track model performance, operation, and system health.
    - Implement monitoring and logging using Google Cloud Monitoring and Logging to track model performance metrics, system health, and operation.
    - Set up alerts for detecting anomalies or performance degradation.
- **Model Evaluation**:
	- Conduct rigorous evaluation of the deployed models using a combination of validation datasets and real-world news articles.
	- Measure the accuracy, precision, recall, and F1-score of each classification task to assess the model's performance.
	- Gather feedback from users and stakeholders to identify areas for improvement and fine-tuning.
- **Batch Tuning:** Set up a pipeline for batch tuning the models periodically using GCP's AI Platform for retraining on updated data and improving performance over time.
    - Create a pipeline for periodic batch tuning of the models using GCP's AI Platform.
    - Schedule batch jobs to retrain the models on updated data at regular intervals.
    - Monitor the performance improvements and update the deployed models accordingly.
## 2.2 **Security and Compliance:**

- Ensure data security and compliance with regulations such as GDPR by implementing appropriate access controls and encryption mechanisms.
- Regularly audit and review the system for compliance with security best practices.

## 2.3 **Documentation and Training:**

- Document the entire project including data sources, preprocessing steps, model architecture, deployment procedures, and monitoring/logging setup.
- Provide training to stakeholders on using the deployed system and interpreting classification results.
- Establish a maintenance plan for ongoing support and updates to the deployed system.

## 2.4 **Future Enhancements:**

- Explore advanced natural language processing techniques such as BERT or Transformer models for more accurate sentiment analysis and content understanding.
- Incorporate user feedback mechanisms to dynamically adjust model predictions based on user interactions and preferences.
- Expand the scope of classification to include additional dimensions.