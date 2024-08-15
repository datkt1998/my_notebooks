
# 1. Overview

## 1.1. AI Workflow

![](https://cloud.google.com/static/vertex-ai/generative-ai/docs/images/generative-ai-workflow.png)

- **Promt** is a request that instructs the model how to respond back. Depending on the model, **promt** can be `text`, `images`, `videos`, `audio`, `documents` or even `multimodal`
	See  [prompt design](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/introduction-prompt-design) : the way to trial and error the prompt design principles and strategies

- **Foundation models**: List of foundation model: 
	- **Google models**: model do google phát triển
		- **Gemini API:** Advanced reasoning, multiturn chat, code generation, and multimodal prompts.
		- **Imagen API:** Image generation, image editing, and visual captioning.
		- **MedLM**: Medical question answering and summarization. (**Private GA**)
	- **Tunned models**: model được [customize](https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models) lại từ ***Google models*** thay vì phải sử dụng các complex prompt (giảm chi phí , giảm độ trễ của model do chỉ cần thiết kế simple prompt) 
		Vertex AI also offers [model evaluation tools](https://cloud.google.com/vertex-ai/generative-ai/docs/models/evaluate-models) to help you evaluate the performance of your tuned model. After your tuned model is production-ready, you can [deploy it to an endpoint](https://cloud.google.com/vertex-ai/docs/general/deployment) and monitor performance like in standard MLOps workflows.
	- **Partner models**: model do các bên partner của google phát triển
	- **Open models**: Open-source model từ các source: hugging face, ...

	The models differ in size, modality, and cost. You can explore Google models, as well as open models and models from Google partners, in [Model Garden](https://cloud.google.com/vertex-ai/docs/start/explore-models).
	--> Mô hình text sử dụng `gemini-1.0-pro-xxx` (xxx lớn nhất, tức là mới nhất, bản stable) 
	
- **Request augmentation**: give the model access to external APIs and real-time information.
	- **[Grounding](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview):** Connects model responses to a source of truth, such as your own data or web search, helping to reduce hallucinations.
	- **[RAG](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/rag):** Connects models to external knowledge sources, such as documents and databases, to generate more accurate and informative responses.
	- **[Function calling](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling):** Lets the model interact with external APIs to get real-time information and perform real-world tasks.

- **Citation check**: check xem reponse có cần đưa trích dẫn nguồn hay không (có nếu đa phần thông tin đến từ 1 nguồn)

- **Responsible AI and safety**: 
	- Check prompt and response text qua 1 lớp [safety filters](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai#safety_filters_and_attributes). If the threshold is exceed for one or more categories, the response is blocked and Vertex AI returns a [fallback response](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai#fallback_responses).

- **Response**: the response is returned all at once. However, you can also receive responses progressively as it generates by enabling [streaming](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/streaming).

## 1.2. [Generative AI APIs and models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview#genai-models)

- Gemini API
	- **Gemini 1.0 Pro**: natural language tasks, multiturn text and code chat, and code generation
	- **Gemini 1.0 Pro Vision**: multimodal prompts. You can include text, images, video, and PDFs in your prompt requests and get text or code responses.
	- **Gemini 1.5 Pro** ([Preview](https://cloud.google.com/products#product-launch-stages)) large than **Gemini 1.0 Pro Vision**
- PaLM API
	- **PaLM API for text** is fine-tuned for language tasks such as classification, summarization, and entity extraction.
	- **PaLM API for chat** is fine-tuned for multi-turn chat, where the model keeps track of previous messages in the chat and uses it as context for generating new responses.
	- [Other Generative AI offerings](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview#other-genai)

# 2. Model APIs

Vertex AI has the following **foundation model APIs**:

- Gemini API (Multimodal text, image, audio, video, PDF, code, and chat): [Gemini model summary](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models)
- PaLM API (Text, chat, and embeddings): [PaLM model summary](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#palm-models)
- Codey APIs (Code generation, code chat, and code completion)
- Imagen API (Image generation, image editing, image captioning, visual question answering, and multimodal embedding)

Discover all model in [Model Garden](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
## 2.1. [Gemini API](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview)

### 2.1.1. Safety attributes

**Options to blocks unsafe content base on a list of unsafe attributes and their blocking thresholds.**

| **Safety Attribute** | **Definition**                                                                       | **Nội dung**                                   |
| -------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------- |
| Hate Speech          | Negative or harmful comments targeting identity and/or protected attributes.         | nhận xét tiêu cực đến một chủ thể đặc biệt     |
| Harassment           | Malicious, intimidating, bullying, or abusive comments targeting another individual. | Bình luận ác ý, tiêu cực, lăng mạ cá nhân khác |
| Sexually Explicit    | Contains references to sexual acts or other lewd content.                            | Nội dung tình dục, khiêu dâm                   |
| Dangerous Content    | Promotes or enables access to harmful goods, services, and activities.               | Quảng bá buôn bá hàng cấm, chất kích thích     |
**Detect Unsafe content base on probabilities of safety attribute**

| **Probability** | **Description**                                       | **Nội dung**                                    |
| --------------- | ----------------------------------------------------- | ----------------------------------------------- |
| `NEGLIGIBLE`    | Content has a negligible probability of being unsafe. | Xác suất chứa thông tin unsafe gần như không có |
| `LOW`           | Content has a low probability of being unsafe.        | Xác suất unsafe ít                              |
| `MEDIUM`        | Content has a medium probability of being unsafe.     | Xác suất unsafe trung bình                      |
| `HIGH`          | Content has a high probability of being unsafe.       | Xác suất unsafe nhiều                           |
**Detect Unsafe content base on severity of safety attribute**

| **Probability** | **Description**                                       | **Nội dung**                         |
| --------------- | ----------------------------------------------------- | ------------------------------------ |
| `NEGLIGIBLE`    | Content has a negligible probability of being unsafe. | mức độ nghiêm trọng gần như không có |
| `LOW`           | Content has a low probability of being unsafe.        | mức độ nghiêm trọng ít               |
| `MEDIUM`        | Content has a medium probability of being unsafe.     | mức độ nghiêm trọng trung bình       |
| `HIGH`          | Content has a high probability of being unsafe.       | mức độ nghiêm trọng nhiều            |
**Threshold**

| **Threshold (Studio)** | **Threshold (API)**                | **Threshold (Description)**                              |
| ---------------------- | ---------------------------------- | -------------------------------------------------------- |
|                        | `BLOCK_NONE` (Restricted)          | Always show regardless of probability of unsafe content. |
| Block few              | `BLOCK_ONLY_HIGH`                  | Block when high probability of unsafe content.           |
| Block some (Default)   | `BLOCK_MEDIUM_AND_ABOVE` (Default) | Block when medium or high probability of unsafe content. |
| Block most             | `BLOCK_LOW_AND_ABOVE`              | Block when medium or high probability of unsafe content. |
|                        | `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Threshold is unspecified, block using default threshold. |
### 2.1.2. Function calling

FC enabling models to delegate certain data processing tasks to custom functions, which are predefined and provided as part of a structured data output, allows model to access the real-time data and interact with various services.
	Bởi vì Generative AI được học bởi outdated data nên sẽ trả lời thông tin bị out of date, do đó thông qua FC, sẽ lấy được thông tin qua các API realtime để bổ sung infomation cho result của model

#### 2.1.2.1. Use case
1. [**Extract Entities from Natural Language Stories**](https://ai.google.dev/tutorials/structured_data_extraction): Function calling can help extract lists of characters, relationships, things, and places from a story.
2. [**Query and Understand SQL Databases Using Natural Language**](https://www.googlecloudcommunity.com/gc/Community-Blogs/Building-an-AI-powered-BigQuery-Data-Exploration-App-using): Models can convert natural language questions into SQL queries and execute functions to interact with databases such as BigQuery.
3. [**Help Customers Interact with Businesses**](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb): Functions can be created to connect to a business' API and provide accurate responses to customer queries like product availability or store locations.
4. [**Build Generative AI Applications by Connecting to Public APIs**](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/function-calling/intro_function_calling.ipynb): Functions enable querying public APIs for tasks like currency conversion, obtaining weather information, or converting addresses to coordinates

#### 2.1.2.2. Create FC

##### 2.1.2.2.1. Define and describe a set of available functions

The application must be define a set of functions that the model can use to process the query. Function declaration: `function_name`, `function_parameters` and `function_description` (optional).

1. **Function name**
2. **Function parameters**: must be provided in a format that's compatible with the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schema):
	- supported: 
		- `type`
		- `nullable`
		- `required`
		- `format`
		- `description`
		- `properties`
		- `items`
		- `enum` ( [string] ) : List of string values to be used if the substitution options are from a limited set
	- not supported: `default`, `optional`, `maximum`, `oneOf`.
3. **Function description**: Nên viết rõ các parameters cần có trong function, phục vụ mục đích gì 

==Example==
```python
get_current_weather_func = FunctionDeclaration(    
   name="get_current_weather",
   description="Get the current weather in a given location",    
   parameters={        
	   "type": "object",        
	   "properties": {
		   "location": {
			   "type": "string", 
			   "description": "The city name of the location for which to get the weather."
			   }
		   },    
	   },
   )
```

```python
extract_sale_records_func = FunctionDeclaration(   
	name="extract_sale_records",   
	description="Extract sale records from a document.",   
	parameters={       
		"type": "object",       
		"properties": {           
			"records": {               
				"type": "array",               
				"description": "A list of sale records",               
				"items": {                   
					"description": "Data for a sale record",                   
					"type": "object",                   
					"properties": {                
						"id": {
							"type": "integer", 
							"description": "The unique id of the sale."
							},                       
						"date": {
							"type": "string", 
							"description": "Date of the sale, in the format of MMDDYY, e.g., 031023"
							},                       
						"total_amount": {
							"type": "number", 
							"description": "The total amount of the sale."
							},                       
						"customer_name": {
							"type": "string", 
							"description": "The name of the customer, including first name and last name."
							},                       
						"customer_contact": {
							"type": "string", 
							"description": "The phone number of the customer, e.g., 650-123-4567."
							},                   
						},                   
					"required": ["id", "date", "total_amount"],               
					},           
				},       
			},       
		"required": ["records"],   
		},
	)
```

```python
extract_news_records_func = FunctionDeclaration(   
	name="extract_news",   
	description="Extract AI news analysis from an article.",   
	parameters={       
		"type": "object",       
		"properties": {           
			"companies": {               
				"type": "array",               
				"description": "A list of companies that mention in article",               
				"items": {                   
					"description": "Company was mentioned in article",                   
					"type": "object",                   
					"properties": {                
						"company_name": {
							"type": "string", 
							"description": "Thefull name of the company."
							},                       
						"stock_symbol": {
							"type": "string", 
							"description": "The symbols used to identify specific publicly traded companies and the securities they issue"
							},                       
						"company_sentiment": {
							"type": "string", 
							"description": "The sentiment towards the company in a news article"
							},       
						},                   
					"required": ["company_name"],
					},           
				},       
			},
			"sentiments":{
				"type": "string",
				"description": "The sentiment classification of the news: positive, neutral, negative",
				"enum": ["positive", "neutral", "negative"],
				"nullable": false
			},
			"sector":{
				"type": "string",
				"description": "The main sector mentioned in the article",
			},
			"summary":{
				"type": "string",
				"description": "The short summary of the article's content. Maximum 60 words."
			},
#			"keywords":  
		"required": ["sentiments",'summary'],   
		},
	)
```

##### 2.1.2.2.2. The Query

When the user provides a prompt, the application must provide the model with the _user prompt_ and the _function declarations_. 
- To configure how the model generates results, the application can provide the model with a _generation configuration_. 
- To configure how the model uses the function declarations, the application can provide the model with a _tool configuration_.

1. **User prompt**: Cần có
	- Additional context: `You are a financial  investor and need to classify the news.`
	- Details or instructions on **how** and **when** to use the functions: 
	- Instructions to ask clarifying questions if user queries are ambiguous: `Kết quả là câu trả lời theo đúng cấu trúc định trước, không sử dụng câu hỏi`

	Example:`You are a financial investor and need to analysis the news article from the article content input and return it as a structured JSON`
	
1. **Generation configuration**: For the `temperature` parameter, use `0` or another low value. This instructs the model to generate more confident results and reduces hallucinations.

|Mode|Description|
|---|---|
|AUTO|The default model behavior. The model decides whether to predict a function call or a natural language response.|
|ANY|The model must predict only function calls. To limit the model to a subset of functions, define the allowed function names in `allowed_function_names`.|
|NONE|The model must not predict function calls. This behaviour is equivalent to a model request without any associated function declarations.|

> The tool configuration's `ANY` mode is a [Preview](https://cloud.google.com/products#product-launch-stages) feature. It is supported for `Gemini 1.5 Pro` models only.

3. **Invoke an external API**: If the model proposes the invocation of a function that would send an order, update a database, or otherwise have significant consequences, validate the function call with the user before executing it.
> If the application receives a function name and parameter values from the model, the application must connect to an external API and call the function.
#### 2.1.2.3. Pricing