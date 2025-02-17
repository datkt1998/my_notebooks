# Airflow

## Overview

Apache Airflow is a powerful workflow orchestration tool that helps you schedule, monitor, and manage data pipelines. Since you’re working with feature engineering and GCP, Airflow can be a great addition to automate your ML pipelines.

Nguyên tắc của Airflow:

- Tính năng động ( Dynamic ) : Airflow pipeline được config bằng code Python, cho phép bạn thay đổi code dễ dàng để tùy biến luồng làm việc của bạn.
- Tính tăng trưởng ( Scalable ) : Ví dụ đơn giản là bạn có thể mở rộng các task về xử lý dữ liệu để tiết kiệm thời gian
- Tính gọn gàng ( Elegant ) : code gọn gàng, ngăn nắp, rõ ràng giúp bạn đọc hiểu code nhanh chóng.
- Tính mở rộng ( Extensible ) : Bạn có thể thêm thắt thư viện, modules, packages, ... phù hợp với môi trường của bạn

P/S : Airflow không phải một giải pháp về stream dữ liệu như Spark Streaming, Apache Storm

**1. Core components:**
• *DAGs (Directed Acyclic Graphs)* – Define workflows. (đọc bởi scheduler và executor ( với mọi worker mà executor có ))
• *Tasks & Operators* – Atomic units of execution.
• *Schedulers* – Manage task execution (chạy workflow , gửi các tasks tới executor)
• *Executors* – Define how tasks run (Local, Celery, Kubernetes, etc.) (quản lý các workers, xử lý các tác vụ đang chạy)
• *Metadata Database* – Stores execution history. (nơi lưu trạng thái của scheduler, executor, webserver)
• *Web UI* – Monitor DAGs visually. (giao diện web cho phép kiểm tra, kích hoạt, sửa lỗi các tasks và DAGs)

![](https://images.viblo.asia/cf6457f8-82c2-4d05-9ac5-f33fadbe5d15.png)

**2. Advanced Features**
• *Sensors* (waiting for events like files in GCS).
• *Hooks* (connectors to external services like BigQuery, Pub/Sub).
• *XComs* (passing data between tasks).
• *Branching & Conditional Execution* (BranchPythonOperator).
• *TaskRetries & SLAs* (handling failures).

**3. Writing DAGs**

• How to define DAGs in Python.
• Using **Operators** (BashOperator, PythonOperator, DummyOperator).
• Task dependencies (set_upstream, set_downstream).
• Using Jinja templating for dynamic DAGs.

**4. Airflow with GCP**

• Using **Google Cloud Operators**:
	• **BigQueryOperator** – Querying BigQuery.
	• **DataflowTemplateOperator** – Running Dataflow jobs.
	• **PubSubPublishMessageOperator** – Publishing messages.
	• **KubernetesPodOperator** – Running tasks in GKE.
• Integrating Airflow with **Vertex AI Pipelines**.

**5. Airflow in Production**

• Airflow deployment strategies (Kubernetes, Cloud Composer).
• Monitoring & logging best practices.
• Handling failures & retries.
• Airflow security & authentication.

**6. Real-World Use Cases**

• Automating ML feature engineering pipelines with Airflow.
• ETL/ELT pipelines with Airflow & BigQuery.
• Orchestrating ML training & inference workflows.

## Installation & Setup

