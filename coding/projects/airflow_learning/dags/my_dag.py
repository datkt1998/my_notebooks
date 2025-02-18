from datetime import datetime, timedelta

from airflow.decorators import dag, task
from pytz import timezone

local_tz = timezone("Asia/Ho_Chi_Minh")


# Định nghĩa DAG với decorator
@dag(
    dag_id="my_dag",
    default_args={
        "owner": "airflow",
        "depends_on_past": False,
        "start_date": datetime(2023, 6, 7, tzinfo=local_tz),
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple DAG",
    schedule_interval="* * * * *",
    catchup=False,
)
def my_dag():
    # Định nghĩa các task với decorator
    @task
    def task1():
        print("Task 1")

    @task
    def process_data():
        print("process data")

    @task
    def save_data():
        print("save data")

    # Thiết lập phụ thuộc giữa các task
    task1() >> process_data() >> save_data()


# Khởi tạo DAG
run_my_dag = my_dag()
