
# 1. Ref
- https://cloudonair.withgoogle.com/events/deploy-ml-vertex-ai
- https://cloud.google.com/vertex-ai/pricing#instances
- https://towardsdatascience.com/choosing-between-tensorflow-keras-bigquery-ml-and-automl-natural-language-for-text-classification-6b1c9fc21013
- https://www.spiceworks.com/tech/artificial-intelligence/articles/google-cloud-ai-vs-vertex-ai/
- https://www.cloudskillsboost.google/course_templates/684/labs/452134
- https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main
- https://cloud.google.com/vertex-ai/docs/training/configure-compute#create_custom_job_machine_types-console
- https://cloud.google.com/vertex-ai/docs/predictions/configure-compute
- https://cloud.google.com/vertex-ai/docs/start/training-methods
- https://cloud.google.com/vertex-ai/docs/start/introduction-unified-platform
- https://cloud.google.com/vertex-ai/docs/training/overview#load_and_prepare_training_data
- https://cloud.google.com/vertex-ai/docs?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_sar_aiml_vertexio_&utm_content=-
- https://codelabs.developers.google.com/vertex_custom_training_prediction#0
- https://www.cloudskillsboost.google/course_templates/684/labs/452134
# 2. Cost Estimation
## 2.1. Pricing for Custom models

## 2.2. Pricing for AutoML models

For Vertex AI AutoML models, you pay for three main activities (info from google cloud official website) :

- Training the model
- Deploying the model to an endpoint
- Using the model to make predictions

Find the complete Vertex AI Pricing List [here](https://cloud.google.com/vertex-ai/pricing#text-data).

## 2.3. Estimation 

(Text classification)

| **Stage**                           | **Step**                      | **Service option 1**                                                                                 |                                   |          | **Service option 2**                                                                    |                                                                                                                                                                                  |                                                                              | **Service option 3**                                                 |            |          |
| ----------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------- | -------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------- | ---------- | -------- |
|                                     |                               | **Name**                                                                                             | **Detail**                        | **Cost** | **Name**                                                                                | **Detail**                                                                                                                                                                       | **Cost**                                                                     | **Name**                                                             | **Detail** | **Cost** |
| ***Storage***                       | *Data*                        |                                                                                                      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Feature*                     |                                                                                                      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Label*                       |                                                                                                      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Model*                       |                                                                                                      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
| ***Data preparation & processing*** | *EDA*                         | [Vertex AI Workbench notebooks](https://cloud.google.com/vertex-ai/docs/workbench/introduction)      | for small and medium size dataset |          | [Dataproc Serverless Spark](https://cloud.google.com/dataproc-serverless/docs/overview) | For large datasets                                                                                                                                                               |                                                                              |                                                                      |            |          |
|                                     | *Feature engineering*         | [Vertex AI managed dataset](https://cloud.google.com/vertex-ai/docs/training/using-managed-datasets) |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Feature store  & selection*  |                                                                                                      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Labeling*                    |                                                                                                      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
| ***Model training***                | *Training method*             | Custom training                                                                                      |                                   |          | AutoML                                                                                  | $3.30 per hour<br>(Estimate 10h training )                                                                                                                                       | $3.3 * 10 = $33 /train time                                                  | [BigQuery ML](https://cloud.google.com/vertex-ai/docs/beginner/bqml) |            |          |
|                                     | *Model tunning & experiments* | Custom tunning job                                                                                   |                                   |          | Vertex AI Experiments                                                                   |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Model evaluation*            | [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines/introduction)                |                                   |          | Vertex AI model Registry                                                                |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
| ***Model serving***                 | *Model deployment*            |                                                                                                      |                                   |          | AutoML                                                                                  | $0.05 per hour                                                                                                                                                                   | $0.05 \* 24 hours * 30 days = $36/month                                      |                                                                      |            |          |
|                                     | *Prediction*                  | Online predictions                                                                                   |                                   |          | AutoML                                                                                  | $5.00 per 1,000 text records<br>- 1 text record xác định = 1000 unicode characters<br>- Trung bình 3000 characters / 1 content news articles <br>- Trung bình 400 articles / day | 3000/1000 records * 400 articles  * 30 days * $5 / 1000 records = $180/month | [BigQuery ML](https://cloud.google.com/vertex-ai/docs/beginner/bqml) |            |          |
|                                     | *Feature store*               | [Vertex AI Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview)             |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Model explain*               | [Vertex Explainable AI](https://cloud.google.com/vertex-ai/docs/explainable-ai/overview)             |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Monitoring*                  | [Vertex AI Model Monitoring](https://cloud.google.com/vertex-ai/docs/model-monitoring/overview)      |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
| ***Management & administer***       | *Resource scaling*            | Ray on Vertex AI                                                                                     |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
|                                     | *Model management*            | Vertex AI model Registry                                                                             |                                   |          |                                                                                         |                                                                                                                                                                                  |                                                                              |                                                                      |            |          |
Note:
- Time series forecasting: [Vertex-ai Forecasting ](https://cloud.google.com/vertex-ai/pricing#forecast)


# 3. Documentation 

## 3.1. ML workflow

1. **Data preparation** 
	- *EDA*
		- For small + medium dataset:  [Vertex AI Workbench](https://cloud.google.com/vertex-ai/docs/workbench/introduction)
		- For large dataset: [Dataproc Serverless Spark](https://cloud.google.com/dataproc-serverless/docs/overview)
	- *Storage*
	- *Feature engineering*: [Vertex AI managed dataset](https://cloud.google.com/vertex-ai/docs/training/using-managed-datasets)
	- *Labeling*
1. **Model training**
	- *Training*
		- [AutoML](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide) : without writing code and preparing data splits (`tabular`, `image`, `text`, `video`)
		- [Custom training](https://cloud.google.com/vertex-ai/docs/training/overview) : control over the training process (ML framework, own training code, hyperparameter tuning options)
		- [Model garden](https://cloud.google.com/vertex-ai/docs/start/explore-models) : choose the pretrain model (open-source models) to test, customize, deploy.
		- [Generative AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview): Access to Google large gen AI models for multiple modalities (text, code, images, speech), then tunning and deploy
	- *Tuning*
		- Hyper-parameters:
			- For simple custom-trained models: [Custom tuning jobs](https://cloud.google.com/vertex-ai/docs/training/using-hyperparameter-tuning)
			- For complex ML models:  [Vertex AI Vizier](https://cloud.google.com/vertex-ai/docs/vizier/overview)
		- Algorithms:
			- Multi-algorithms training:  [Vertex AI Experiments](https://cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments)
			- Tensorflow: [Vertex AI TensorBoard](https://cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction)
		- Manage model versions
			- Register the version of trained models:  [Vertex AI Model Registry](https://cloud.google.com/vertex-ai/docs/model-registry/introduction)
	- *Evaluation* (list of [Model evaluation](https://cloud.google.com/vertex-ai/docs/evaluation/introduction))
		- Evaluation in [Vertex AI Model Registry](https://cloud.google.com/vertex-ai/docs/model-registry/introduction)
		- Evaluation in [Vertex AI Pipelines](https://cloud.google.com/vertex-ai/docs/pipelines/introduction)
3. **Model serving and monitoring**
	- *Serving*: deploy model to production and get predictions
		- For Custom training models 
			-  Real-time [online predictions](https://cloud.google.com/vertex-ai/docs/predictions/overview#online_predictions):  [prebuilt](https://cloud.google.com/vertex-ai/docs/predictions/pre-built-containers) or [custom](https://cloud.google.com/vertex-ai/docs/predictions/use-custom-container) containers
			- [Batch predictions](https://cloud.google.com/vertex-ai/docs/predictions/overview#batch_predictions)
		- [BigQuery ML](https://cloud.google.com/vertex-ai/docs/beginner/bqml)
	- *Manage features*: [Vertex AI Feature Store](https://cloud.google.com/vertex-ai/docs/featurestore/overview) (for Tabular)
	- *Explain model*: [Vertex Explainable AI](https://cloud.google.com/vertex-ai/docs/explainable-ai/overview)
	- *Monitoring*: [Vertex AI Model Monitoring](https://cloud.google.com/vertex-ai/docs/model-monitoring/overview) (*training-serving skew and prediction drift and sends you alerts when the incoming prediction data skews too far from the training baseline*)
## 3.2. Interfaces for Vertex-ai 

Interact with Vertex AI via:
- [Google Console](https://console.cloud.google.com/vertex-ai?project=ext-pinetree-dw) (graphical user interface)
- [Google Cloud command-line interface (CLI)](https://cloud.google.com/sdk/gcloud) ([`gcloud ai`](https://cloud.google.com/sdk/gcloud/reference/ai) command)
- [Terraform support for Vertex AI](https://cloud.google.com/vertex-ai/docs/start/use-terraform-vertex-ai) (Terraform)
- [Vertex AI SDK for Python](https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk) (Python)
- [Vertex AI API REST](https://cloud.google.com/vertex-ai/docs/reference/rest) (API)

## 3.3. Development tools
### 3.3.1. [Vertex AI SDK](https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk)
### 3.3.2. Vertex AI Notebooks 
#### 3.3.2.1. Colab Enterprise 
(use for collaborate) use if want to collaborate function with others and avoid spending time managing infrastructure.
- [Share and collaborate](https://cloud.google.com/vertex-ai/docs/workbench/notebook-solution#share_and_collaborate): share notebooks and collaborate with others (Learn how to [grant access to a notebook](https://cloud.google.com/colab/docs/manage-access-notebook).)
- [Managed compute](https://cloud.google.com/vertex-ai/docs/workbench/notebook-solution#managed_compute): work in notebooks without having to manage infrastructure, configure runtimes for specific needs, but Colab Enterprise starts them for you and shuts them down when you no longer need them.
- [Integrated into the Google Cloud console](https://cloud.google.com/vertex-ai/docs/workbench/notebook-solution#integrated_into_the)
- [Inline code completion](https://cloud.google.com/vertex-ai/docs/workbench/notebook-solution#code-completion):  [Gemini](https://cloud.google.com/gemini/docs/overview) assistance
#### 3.3.2.2. Vertex AI Workbench 
(use for control and customizability) A Jupyter notebook-based environment provided through *virtual machine (VM) instances* with features that support the entire data science workflow.
### 3.3.3. Terraform



## 3.4. Training methods

[Choosing a training method](https://cloud.google.com/vertex-ai/docs/start/training-methods)

|                                                                    | **AutoML**                                                                                                                                                                                                                                                                                                                                                                                                                                   | **BigQuery ML**                                                                                                                                                                                                              | **Custom training**                                                                                                      |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Characteristic**                                                 | - minimal technical effort<br>- quickly prototype models and explore new datasets                                                                                                                                                                                                                                                                                                                                                            | - train models using your BigQuery data directly in BigQuery using SQL commands<br>-use SQL to get batch predictions                                                                                                         | - create a training application optimized for your targeted outcome<br>- control over training application functionality |
| **DS expertise**                                                   | No                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                                                                                                                                                                                                           | Yes                                                                                                                      |
| **Programming ability**                                            | No                                                                                                                                                                                                                                                                                                                                                                                                                                           | SQL (build, evaluate model)                                                                                                                                                                                                  | Yes                                                                                                                      |
| **Time to trained model**                                          | - Lower <br>- Less data preparation is required, and no development is needed.                                                                                                                                                                                                                                                                                                                                                               | - Lower <br>- Don't need build the infrastructure required for batch predictions or model training, as BigQuery ML leverages the BigQuery computational engine -->  increases speed to training, evaluation, and prediction. | - Higher<br>- More data preparation is required, and training application development is needed.                         |
| **Limits on machine learning objectives**                          | Yes (only AutoML's predefined objectives)                                                                                                                                                                                                                                                                                                                                                                                                    | Yes                                                                                                                                                                                                                          | No                                                                                                                       |
| **Manually optimize model performance with hyperparameter tuning** | No (automated hyperparameter tuning)                                                                                                                                                                                                                                                                                                                                                                                                         | Yes. BigQuery ML supports hyperparameter tuning when training ML models using [`CREATE MODEL` statements.](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-hyperparameter-tuning)                | Yes                                                                                                                      |
| **Control aspects of the training environment**                    | - Limited. <br>- Specify the number of node hours to train for + allow early stopping of training (for `tabular` + `image`)                                                                                                                                                                                                                                                                                                                  | No.                                                                                                                                                                                                                          | Yes.<br>- Compute Engine machine type<br>- Disk size<br>- ML framework <br>- Number of nodes.                            |
| **Limits on data size**                                            | Yes<br>- [Preparing image training data](https://cloud.google.com/vertex-ai/docs/training-overview#image_data)<br>- [Preparing tabular training data](https://cloud.google.com/vertex-ai/docs/training-overview#tabular_data)<br>- [Preparing text training data](https://cloud.google.com/vertex-ai/docs/training-overview#text_data)<br>- [Preparing video training](https://cloud.google.com/vertex-ai/docs/training-overview#video_data) | Yes (base on [Quotas](https://cloud.google.com/bigquery-ml/quotas))                                                                                                                                                          | - For unmanaged datasets: No<br>- For managed datasets: same **AutoML**                                                  |

### 3.4.1. [AutoML ](https://cloud.google.com/inclusive-ml)

- make AI work for them by offering an easy-to-use + codeless user experience + requires no prior ML experience
- use `Transfer learning` and `Learning to learn`: smaller datasets than typically would be required

## 3.5. Resource config selection 


# 4. Practical guide

## 4.1. [Colab Enterprise notebook](https://cloud.google.com/colab/docs/create-console-quickstart)


## 4.2. [AutoML ](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)


## 4.3. Custom model


# 5. GCP guide

## 5.1. Automation execute python script
`Pub/Sub`, `Cloud Function`, `Cloud Scheduler`, `BigQuery`

[Youtube](https://www.youtube.com/watch?v=4Uqd71SUyLM)

1. **`Pub/Sub`** : Create topic : dev-cloudfunction-trigger-newscategory
2. 