# Overview

[overview](https://cloud.google.com/vertex-ai/docs)

## Introduction

### ML workflow

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

### Training and deployment option

- [AutoML](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide) lets you train tabular, image, text, or video data without writing code or preparing data splits.
- [Custom training](https://cloud.google.com/vertex-ai/docs/training/overview) gives you complete control over the training process, including using your preferred ML framework, writing your own training code, and choosing hyperparameter tuning options.
- [Model Garden](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models) lets you discover, test, customize, and deploy Vertex AI and select open-source (OSS) models and assets.
- [Generative AI](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/overview) gives you access to Google's large generative AI models for multiple modalities (text, code, images, speech). You can tune Google's LLMs to meet your needs, and then deploy them for use in your AI-powered applications.

### Vertex-ai interaction ways

- [Google Console](https://console.cloud.google.com/vertex-ai?project=ext-pinetree-dw) (graphical user interface)
- [Google Cloud command-line interface (CLI)](https://cloud.google.com/sdk/gcloud) ([`gcloud ai`](https://cloud.google.com/sdk/gcloud/reference/ai) command)
- [Terraform support for Vertex AI](https://cloud.google.com/vertex-ai/docs/start/use-terraform-vertex-ai) (Terraform)
- [Vertex AI SDK for Python](https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk) (Python)
- [Vertex AI API REST](https://cloud.google.com/vertex-ai/docs/reference/rest) (API)

## Setup environment

1. Create project and enable billing
2. Enable Vertex AI API
3. [Install](https://cloud.google.com/sdk/docs/install) the Google Cloud CLI.
4. To [initialize](https://cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command:
``` bash
gcloud init
```
5. Update and install `gcloud` components:
``` bash
gcloud components update  
gcloud components install beta
```
6. Add role ([read doc](https://cloud.google.com/vertex-ai/docs/start/cloud-environment#ask_admin))
7. Install [Vertex AI SDK for Python](https://cloud.google.com/vertex-ai/docs/start/install-sdk)

## Training methods

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

## Notebook tutorials

[List of totebook tutorials](https://cloud.google.com/vertex-ai/docs/tutorials/jupyter-notebooks#vertex-ai-workbench)

