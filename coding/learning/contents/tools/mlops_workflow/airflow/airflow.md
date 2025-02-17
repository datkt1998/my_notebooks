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



## [Airflow Components](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/overview.html)


![](https://airflow.apache.org/docs/apache-airflow/stable/_images/edge_label_example.png)

### DAG

**Directed Acyclic Graph** là **một đồ thị có hướng không chu trình**, mô tả tất cả các bước xử lý dữ liệu trong một quy trình, từ đó xác định quy trình thực hiện task công việc

- Mỗi DAG được xác định trong 1 file DAG, nó định nghĩa một quy trình xử lý dữ liệu, được biểu diễn dưới dạng một đồ thị có hướng không chu trình, trong đó **các nút là các tác vụ (tasks) và các cạnh là các phụ thuộc giữa các tác vụ**.
- Các tác vụ trong DAG thường được **xử lý tuần tự hoặc song song**
- Khi một DAG được thực thi, nó được gọi là một lần chạy DAG

#### DAG Status

![](https://images.viblo.asia/f0b289e3-60f9-4725-9962-dfb27a37052e.png)

Vòng đời của 1 trạng thái nhiệm vụ gồm có các trạng thái sau
    - **No status**: tác vụ chưa được xếp hàng để thực hiện
    - **Scheduled**: Bộ lập lịch đã xác định rằng các phụ thuộc của nhiệm vụ được đáp ứng và đã lên lịch cho nó chạy
    - **Removed**: Vì một lý do nào đó, tác vụ đã biết mất khỏi DAG kể từ khi bắt đầu chạy
    - **Upstream failed**: tác vụ ngược dòng không thành công
    - **Queued**: Nhiệm vụ đã được giao cho Executor và đang đợi 1 worker có sẵn để thực thi
    - **Running**: Tác vụ đang được chạy bởi một worker
    - **Sucess**: Tác vụ chạy xong không có lỗi
    - **Failed**: Tác vụ có lỗi trong khi thực thi và không chạy được
    - **Up for retry**: Tác vụ không thành công nhưng vẫn còn các lần thử lại và sẽ được lên lịch lại

Vậy lý tưởng nhất cho một tác vụ là gì? Đó là đi từ **No status --> Scheduled --> Queued --> Running --> Sucess**

### Task

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html

**Task** là một đơn vị cơ bản để thực hiện một công việc nhỏ (**được định nghĩa bởi Developer**) trong quy trình xử lý dữ liệu. Mỗi Task là một bước trong quy trình và có thể được lập lịch thực hiện tùy theo các điều kiện cụ thể.

Một **Task** trong Airflow có các thuộc tính và phương thức sau:
- **`task_id`**: định danh duy nhất của task trong DAG.
- **`owner`**: người sở hữu task.
- **`depends_on_past`**: xác định liệu task hiện tại có phụ thuộc vào kết quả của task trước đó hay không.
- **`retries`**: số lần thử lại nếu task thất bại.
- **`retry_delay`**: khoảng thời gian giữa các lần thử lại.
- **`start_date`**: thời điểm bắt đầu thực hiện task.
- **`end_date`**: thời điểm kết thúc thực hiện task.
- **`execution_timeout`**: thời gian tối đa cho phép để thực hiện task.
- **`on_failure_callback`**: hàm được gọi khi task thất bại.
- **`on_success_callback`**: hàm được gọi khi task thành công.

Có 3 nhóm cơ bản về task:
- *Operator*: predefined task templates that you can string together quickly to build most parts of your DAGs.
- *Sensor*:  special subclass of Operators which are entirely about waiting for an external event to happen.
- *TaskFlow*: decorated `@task`, which is a custom Python function packaged up as a Task.

### Operator

https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html

![](https://images.viblo.asia/520a79e3-35d8-45ee-9e78-e23b380b0a55.png)

Mỗi operator đại diện cho một công việc cụ thể (**được định nghĩa trước bởi Airflow**) trong quy trình, ví dụ như đọc dữ liệu từ một nguồn dữ liệu, xử lý dữ liệu, hoặc ghi dữ liệu vào một nguồn dữ liệu khác.

Các operator trong Airflow được phân loại thành các loại chính sau
- **BashOperator**: Chạy các lệnh Bash hoặc script Shell.
- **PythonOperator**: Thực thi các hàm Python.
- **EmailOperator**: Gửi email thông qua SMTP.
- **DummyOperator**: Được sử dụng để tạo các kết nối giữa các task.
- **PythonVirtualenvOperator**: Thực thi các hàm Python trong một môi trường ảo.
- **MySqlOperator**: Thực hiện các lệnh SQL trên cơ sở dữ liệu MySQL.
- **PostgresOperator**: Thực hiện các lệnh SQL trên cơ sở dữ liệu PostgreSQL.
- **S3FileTransformOperator**: Thực hiện các chức năng xử lý file trên Amazon S3.
- **SparkSqlOperator**: Thực hiện các truy vấn Spark SQL.
- **HdfsSensor**: Kiểm tra sự tồn tại của một tệp trên Hadoop Distributed File System (HDFS).

> Ví dụ: đọc dữ liệu từ một tệp CSV, xử lý dữ liệu và lưu kết quả vào một cơ sở dữ liệu PostgreSQL:
- **FileSensor**: Kiểm tra sự tồn tại của tệp CSV trên hệ thống tệp.
- **BashOperator**: Sử dụng lệnh Bash để di chuyển tệp CSV đến thư mục xử lý.
- **PythonOperator**: Thực hiện các xử lý dữ liệu, ví dụ như đọc tệp CSV và chuyển đổi dữ liệu thành định dạng phù hợp để lưu vào cơ sở dữ liệu.
- **PostgresOperator**: Thực hiện các lệnh SQL để lưu kết quả xử lý vào PostgreSQL.
- **EmailOperator**: Gửi email thông báo cho người dùng khi quy trình xử lý dữ liệu hoàn thành.

### Sensor

Sensor là một loại Operator được sử dụng để **giám sát** các sự kiện và điều kiện, và thực hiện các hành động tương ứng. Sensor thường được sử dụng để **đợi cho đến khi một điều kiện nào đó xảy ra trước khi tiếp tục thực hiện** quy trình.

Các loại Sensor trong Airflow bao gồm:
- **FileSensor**: Kiểm tra sự tồn tại của một tệp trên hệ thống tệp.
- **TimeSensor**: Đợi cho đến khi một khoảng thời gian cụ thể đã trôi qua.
- **HttpSensor**: Kiểm tra sự phản hồi của một URL cụ thể.
- **HdfsSensor**: Kiểm tra sự tồn tại của một tệp trên Hadoop Distributed File System (HDFS).
- **SqlSensor**: Kiểm tra sự tồn tại của một bảng hoặc một số dòng dữ liệu trong cơ sở dữ liệu.
- **S3KeySensor**: Kiểm tra sự tồn tại của một đối tượng trên Amazon S3.
- **ExternalTaskSensor**: Kiểm tra trạng thái của một task khác trong DAG.

Sensor sẽ giữ cho task đang chạy và thử lại sau một khoảng thời gian cụ thể, giúp đảm bảo rằng không có dữ liệu bị mất hoặc xử lý sai.

## Aiflow Workflow

Không giống như các công cụ Dữ liệu lớn như Apache Kafka, Apache Storm, Apache Spark,hoặc Flink, **Apache Airflow** không phải là giải pháp truyền dữ liệu. Nó chủ yếu là một trình quản lý quy trình làm việc

![image.png](https://images.viblo.asia/e2d80240-05d3-4d64-a82d-3f7a37dd914a.png)

Hình vẽ trên tổng quan về các thành phần cơ bản của Apache Airflow.

- **Scheduler**: giám sát tất cả các DAG và các tác vụ được liên kết của chúng. Đối với 1 task, khi các phụ thuộc được đáp ứng, Scheduler sẽ khởi tạo tác vụ đó. Nó kiểm tra các tác vụ đang hoạt động để bắt đầu theo định kỳ
- **Executor**: xử lý việc chạy các task này bằng cách đưa chúng cho worker để chạy
- **Web server**: giao diện người dùng của Airflow, hiện thị trạng thái của nhiệm vụ và cho phép người dùng tương tác với cơ sở dữ liệu cũng như đọc tệp nhật kỹ từ kho lưu trữ từ xa như Google Cloud Storage, S3, ...
- **DAG Directory**: một thư mục chứa các file DAG của các quy trình xử lý dữ liệu (data pipelines) trong Airflow.
- **Metabase Database**: được sử dụng bởi Scheduler, Executor và Web Server để lưu trữ thông tin quan trọng của từng DAG, ví dụ như các phiên bản, số liệu thống kê mỗi lần chạy, khoảng thời gian lên lịch, ...
## Installation & Setup

