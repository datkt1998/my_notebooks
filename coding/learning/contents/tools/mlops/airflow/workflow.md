# Workflow

## Install by docker

Sử dụng docker compose là cách phố biến để khởi tạo đồng thời nhiều container (service) cùng chạy 1 lúc dành cho airflow do airflow chứa nhiều components (web, database, scheduler,...)

- **Tạo docker-compose pre-build sẵn**
```bash
	# chỉnh sửa docker-compose file cho phù hợp
	curl -LfO 'https://airflow.apache.org/docs/apache-airflow/lastest/docker-compose.yaml'
```

Trong file yaml này đã có chứa các services sẵn:

- **airflow-scheduler**: giám sát các tasks cũng như chạy tasks khi đã có đủ dependencies
- **airflow-webserver**: webserver có local domain `http://localhost:8080`
- **airflow-worker**: các worker chạy các tasks theo lệnh của scheduler
- **airflow-init**: dịch vụ khởi tạo ban đầu ( tạo account, migrate database, ... )
- **postgres**: cơ sở dữ liệu
- **redis**: cầu nối truyền dẫn các lệnh từ scheduler tới worker.

P/S: Nếu bạn muốn cài thêm một số thư viện python hoặc nâng cấp airflow providers thì có thể điều chỉnh file `docker-compose.yaml` mà bạn vừa tải về bên trên.

- Do thư mục DAG sẽ được mount vào trong các container (chi tiết vui lòng xem trong file [docker-compose.yaml](https://airflow.apache.org/docs/apache-airflow/2.6.0/docker-compose.yaml) ) vậy nên ta cần điều chỉnh một chút thông qua việc đặt biến môi trường `AIRFLOW_UID` để tránh các vấn đề liên quan đến quyền có thể phát sinh, nhất là với các file trong thư mục DAG

- **Tạo docker compose tuỳ chỉnh**
```yaml{toggle}
# docker-compose.yaml

version: '2.1'
services:

# DATABASE SERVICE
  postgres:
    build: './docker/postgres'
    restart: always
    container_name: postgres
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    ports:
      - "32769:5432"
    #volumes:
      #- ./mnt/postgres:/var/lib/postgresql/data/pgdata
    environment:
      - POSTGRES_USER=airflow
      - POSTGRES_PASSWORD=airflow
      - POSTGRES_DB=airflow_db
      #- PGDATA=/var/lib/postgresql/data/pgdata
    healthcheck:
      test: [ "CMD", "pg_isready", "-q", "-d", "airflow_db", "-U", "airflow" ]
      timeout: 45s
      interval: 10s
      retries: 10
      
  adminer:
    image: wodby/adminer:latest
    restart: always
    container_name: adminer
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    ports:
      - "32767:9000"
    environment:
      - ADMINER_DEFAULT_DB_DRIVER=psql
      - ADMINER_DEFAULT_DB_HOST=postgres
      - ADMINER_DEFAULT_DB_NAME=airflow_db
    healthcheck:
      test: [ "CMD", "nc", "-z", "adminer", "9000" ]
      timeout: 45s
      interval: 10s
      retries: 10

# HADOOP SERVICES
  namenode:
    build: ./docker/hadoop/hadoop-namenode
    restart: always
    container_name: namenode
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    ports:
      - "32763:9870"
    volumes:
      - ./mnt/hadoop/namenode:/hadoop/dfs/name
    environment:
      - CLUSTER_NAME=hadoop_cluster
    healthcheck:
      test: [ "CMD", "nc", "-z", "namenode", "9870" ]
      timeout: 45s
      interval: 10s
      retries: 10

  datanode:
    build: ./docker/hadoop/hadoop-datanode
    restart: always
    container_name: datanode
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - namenode
    volumes:
      - ./mnt/hadoop/datanode:/hadoop/dfs/data
    environment:
      - SERVICE_PRECONDITION=namenode:9870
    healthcheck:
      test: [ "CMD", "nc", "-z", "datanode", "9864" ]
      timeout: 45s
      interval: 10s
      retries: 10

  hive-metastore:
    build: ./docker/hive/hive-metastore
    restart: always
    container_name: hive-metastore
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - namenode
      - datanode
      - postgres
    environment:
      - SERVICE_PRECONDITION=namenode:9870 datanode:9864 postgres:5432
    ports:
      - "32761:9083"
    healthcheck:
      test: [ "CMD", "nc", "-z", "hive-metastore", "9083" ]
      timeout: 45s
      interval: 10s
      retries: 10

  hive-server:
    build: ./docker/hive/hive-server
    restart: always
    container_name: hive-server
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - hive-metastore
    environment:
      - SERVICE_PRECONDITION=hive-metastore:9083
    ports:
      - "32760:10000"
      - "32759:10002"
    healthcheck:
      test: [ "CMD", "nc", "-z", "hive-server", "10002" ]
      timeout: 45s
      interval: 10s
      retries: 10

  hive-webhcat:
    build: ./docker/hive/hive-webhcat
    restart: always
    container_name: hive-webhcat
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - hive-server
    environment:
      - SERVICE_PRECONDITION=hive-server:10000
    healthcheck:
      test: [ "CMD", "nc", "-z", "hive-webhcat", "50111" ]
      timeout: 45s
      interval: 10s
      retries: 10

  hue:
    build: ./docker/hue
    restart: always
    container_name: hue
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - hive-server
      - postgres
    ports:
      - "32762:8888"
    volumes:
      - ./mnt/hue/hue.ini:/usr/share/hue/desktop/conf/z-hue.ini
    environment:
      - SERVICE_PRECONDITION=hive-server:10000 postgres:5432
    healthcheck:
      test: [ "CMD", "nc", "-z", "hue", "8888" ]
      timeout: 45s
      interval: 10s
      retries: 10

# SPARK SERVICES
  spark-master:
    build: ./docker/spark/spark-master
    restart: always
    container_name: spark-master
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    ports:
      - "32766:8082"
      - "32765:7077"
    volumes:
      - ./mnt/spark/apps:/opt/spark-apps
      - ./mnt/spark/data:/opt/spark-data
    healthcheck:
      test: [ "CMD", "nc", "-z", "spark-master", "8082" ]
      timeout: 45s
      interval: 10s
      retries: 10

  spark-worker:
    build: ./docker/spark/spark-worker
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - spark-master
    ports:
      - "32764:8081"
    volumes:
      - ./mnt/spark/apps:/opt/spark-apps
      - ./mnt/spark/data:/opt/spark-data
    healthcheck:
      test: [ "CMD", "nc", "-z", "spark-worker", "8081" ]
      timeout: 45s
      interval: 10s
      retries: 10

  livy:
    build: ./docker/livy
    restart: always
    container_name: livy
    logging:
      driver: "json-file"
      options:
          max-file: "5"
          max-size: "10m"
    depends_on:
      - spark-worker
    ports:
      - "32758:8998"
    environment:
      - SPARK_MASTER_ENDPOINT=spark-master
      - SPARK_MASTER_PORT=7077
      - DEPLOY_MODE=client
    healthcheck:
      test: [ "CMD", "nc", "-z", "livy", "8998" ]
      timeout: 45s
      interval: 10s
      retries: 10

# AIRFLOW
  airflow:
    build: ./docker/airflow
    restart: always
    container_name: airflow
    volumes:
      - ./mnt/airflow/airflow.cfg:/opt/airflow/airflow.cfg
      - ./mnt/airflow/dags:/opt/airflow/dags
    ports:
      - 8080:8080
    healthcheck:
      test: [ "CMD", "nc", "-z", "airflow", "8080" ]
      timeout: 45s
      interval: 10s
      retries: 10 

# NETWORK
# Change name of default network otherwise URI invalid for HIVE
# because of the _ contained by default network
networks:
  default:
    name: airflow-network
```

Tạo thư mục docker trong đó chứa các file Dockerfile theo từng service