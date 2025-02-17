import random
from datetime import datetime

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


# Định nghĩa DAG với decorator
@dag(
    dag_id="my_aiml_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    description="A simple ML flow with DAG",
    catchup=False,
)
def my_aiml_dag():
    # Định nghĩa các task DAG với decorator
    @task
    def training_model(model: str):
        accuracy = random.randint(0, 10)
        print(f"Độ chính xác của mô hình {model}: {accuracy}")
        return accuracy

    # Sử dụng @task.branch cho việc rẽ nhánh
    @task.branch
    def choosing_best_model(**kwargs):
        """
        Hàm choosing_best_model được trang trí với @task.branch để thực hiện logic rẽ nhánh.
        Dựa trên độ chính xác cao nhất trong các mô hình, hàm sẽ trả về task_id của nhánh cần thực thi (accurate hoặc inaccurate).

        - XCOM (Cross-Communication Messages) là một cơ chế cho phép dữ liệu đổi giữa các tác vụ DAG
        - Hàm choosing_best_model được sử dụng để lấy thông tin về độ chính xác của 3 task training mô hình A, B, C, nếu 1 trong 3 độ chính xác này đạt một ngưỡng nào đó (ở đây việc training mình cho trả về random 1 giá trị từ 0 đến 10) thì trả về "đạt"
        """
        ti = kwargs["ti"]
        accuracies = ti.xcom_pull(
            task_ids=[
                "training_model_A",
                "training_model_B",
                "training_model_C",
            ]
        )
        best_accuracy = max(accuracies)
        if best_accuracy > 8:
            return "accurate"
        else:
            return "inaccurate"

    # Tạo các task training_model_A, training_model_B, training_model_C
    training_tasks = {
        model: training_model.override(task_id=f"training_model_{model}")(
            model=model
        )
        for model in ["A", "B", "C"]
    }

    # Định nghĩa các task accurate và inaccurate
    # Sử dụng BashOperator để định nghĩa các task thực thi lệnh bash tương ứng khi mô hình đạt độ chính xác cao hoặc thấp.
    accurate = BashOperator(
        task_id="accurate", bash_command="echo 'Prediction'"
    )

    inaccurate = BashOperator(
        task_id="inaccurate", bash_command="echo 'Retraining'"
    )

    # Thiết lập thứ tự thực thi
    (
        training_tasks["A"]
        >> training_tasks["B"]
        >> training_tasks["C"]
        >> choosing_best_model()
        >> [accurate, inaccurate]
    )


# Khởi tạo DAG
run_aiml_dag = my_aiml_dag()
