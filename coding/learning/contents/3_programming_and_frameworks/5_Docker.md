# Docker

## Khái niệm cơ bản
[Tìm hiểu về docker và các khái niệm](https://viblo.asia/p/tim-hieu-ve-docker-va-mot-so-khai-niem-co-ban-GrLZD3OOKk0)

**1. Docker Image**

Một **Docker Image** là một `read-only` template dùng để tạo ra các **containers**. Image được cấu tạo theo dạng layer và tất cả các layer đều là `read-only`. Một **image** có thể được tạo ra dựa trên một **image** khác với một số tùy chỉnh bổ sung. Nói ngắn gọn, **Docker Image** là nơi lưu trữ các cài đặt môi trường như OS, package, phần mềm cần chạy, …

Từ 1 image chúng ta có thể tạo ra nhiều containers với môi trường bên trong giống hệt nhau.

Trong Image có thể chứa: OS (Ubuntu,...), Packages (Git, ...) hoặc các ứng dụng phần mềm khác.

**2. Docker File**

**Dockerfile** là một file dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho **Docker image**. Từ những câu lệnh đó, Docker sẽ build ra **Docker image** (thường có dung lượng nhỏ từ vài MB đến lớn vài GB).

**3. Docker Container**

**Docker Container** được tạo ra từ **Docker Image**, là nơi chứa mọi thứ cần thiết để có thể chạy ứng dụng. Là ảo hóa nhưng **Container** lại rất nhẹ, có thể coi như là một process của hệ thống. Chỉ mất vài giây để `start`, `stop` hoặc `restart` một **Container**. Với một máy chủ vật lý, thay vì chạy được vài cái máy ảo truyền thống thì ta có thể chạy vài chục, thậm chí vài trăm cái **Docker Container**.

Các trạng thái có thể có: 
- `run`
- `started`
- `stopped`
- `moved`
- `deleted`

**4. Docker Network**

**Docker network** có nhiệm vụ cung cấp private network (VLAN) để các container trên một host có thể liên lạc được với nhau, hoặc các container trên nhiều hosts có thể liên lạc được với nhau (multi-host networking).

**5. Docker Volume**

**Docker volume** là cơ chế tạo và sử dụng dữ liệu của docker, có nhiệm vụ lưu trữ dữ liệu độc lập với vòng đời của container.

Có 3 trường hợp sử dụng **Docker Volume**:
- Giữ lại dữ liệu khi một Container bị xóa.
- Để chia sẻ dữ liệu giữa máy chủ vật lý và Docker Container.
- Chia sẻ dữ liệu giữa các Docker Container.

**6. Docker Hub**

Nếu bạn là developer thì chắc hẳn bạn đã quen với công cụ github dùng để upload code của mình lên đó, hiểu đơn giản thì Docker hub cũng tương tự như github nhưng dành cho DockerFile, Docker Images. Ở đây có những DockerFile, Images của người dùng cũng như những bản chính thức từ các nhà phát triển lớn như Google, Oracle, Microsoft, … 

Ngoài ra còn có Docker Hub cho phép quản lý các image với những câu lệnh giống như Github như push, pull... để bạn có thể quản lý dễ dàng image của mình.

**7. Docker Registry**
Nơi lưu trữ **Docker image**. Docker Hub là một registry công khai mà bất cứ ai cũng có thể sử dụng và Docker được cấu hình để tìm kiếm image trên Docker Hub theo mặc định. Bạn thậm chí có thể chạy registry riêng của mình. Có hai loại registry là public hoặc private registry.

**8. Docker Compose**

**Docker compose** là công cụ dùng để định nghĩa và `run multi-container` cho Docker application. Với compose bạn sử dụng file `YAML` để config các services cho application của bạn. Sau đó dùng command để `create` và `run` từ những config đó.

Sử dụng cũng khá đơn giản chỉ với ba bước:
- Khai báo app’s environment trong **Dockerfile**.
- Khai báo các services cần thiết để chạy application trong file `docker-compose.yml`.
- Run `docker-compose up` để start và run app.
## Các câu lệnh cơ bản

### Docker authen

`docker login`

### Khởi tạo docker theo template

`docker init`
### Search thông tin

`docker search <keyword>`: search thông tin các image theo keyword có trên **docker hub**

```bash
docker search mysql
```
```
    NAME                            DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
    mysql                           MySQL is a widely used, open-source relation…   13970     [OK]       
    mariadb                         MariaDB Server is a high performing open sou…   5325      [OK]       
    phpmyadmin                      phpMyAdmin - A web interface for MySQL and M…   766       [OK]       
    percona                         Percona Server is a fork of the MySQL relati…   602       [OK]       
    databack/mysql-backup           Back up mysql databases to... anywhere         82                   
    bitnami/mysql                   Bitnami MySQL Docker Image                      80                   [OK]
    linuxserver/mysql-workbench                                                     48                   
    ubuntu/mysql                    MySQL open source fast, stable, multi-thread…   43                   
    linuxserver/mysql               A Mysql container, brought to you by LinuxSe…   38                   
    circleci/mysql                  MySQL is a widely used, open-source relation…   29                   
    google/mysql                    MySQL server for Google Compute Engine          23                   [OK]
    rapidfort/mysql                 RapidFort optimized, hardened image for MySQL   14                        
```

### Pull image từ Hub

`docker pull`: Lệnh này dùng để tải các image trên docker hub về.

```bash
docker pull python:3
```
### Build image từ docker file
`docker build`: Lệnh này dùng để build một image từ **Dockerfile** và **Context**. 

**Context** ở đây là một tập file được xác đinh bởi đường dẫn hoặc url cụ thể. 

Ta có thể sử dụng thêm tham số `-t` để gắn nhãn cho image.
```bash
`docker build -t your_name_container`
```

```bash
docker build -t datkt98/exam02 .
```

### List các images

`docker images`: Lệnh này dùng để liệt kê các image có trên máy tính

```bash
docker images
```

    REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
    datkt98/exam02   latest    324475812f6b   4 seconds ago    887MB
    datkt98/exam01   latest    1b3ec0e42e26   21 minutes ago   887MB
    python           3         74707af2d4ec   2 days ago       871MB

### Tạo container từ image by command
`docker run`: Lệnh này dùng để tạo 1 container với images của bạn, ví dụ để tạo 1 container với image ubuntu đã tải về trước đó, bạn dùng lệnh
```bash
`docker run -it ubuntu`
```

**Các option thường dùng với `docker run`**
Trong các lệnh trên có lẽ docker run là lệnh hữu ích nhất và ta sẽ thường sử dụng nhất. Nó sử dụng để tạo container dựa vào một image cụ thể. Có nhiều option có thể sử dụng với docker run.

- `--detach`, `-d`
Mặc định docker container chạy thì mọi input, output, lỗi được hiện thị trực tiếp trên màn hình terminal. Tuy nhiên với tùy chọn --detach/-d, container sẽ được chạy ngầm vì vậy mọi output, lỗi sẽ không hiển thị.

- `--entrypoint`
Thiết lập hoặc ghi đè các lệnh mặc định khi chạy images. Entrypoint là một tập các lệnh và tham số sẽ chạy đầu tiên khi container được chạy từ image. Bất kỳ câu lệnh và tham số được truyền vào sau docker run sẽ được nối vào entrypoint.

- `--env`, `-e`
Thiết lập biến môi trường sử dụng cặp (key=value). Nếu ta có biến môi trường trong file ta có thể truền nó vào file bằng tùy chọn --env-file.

- `--ip`
Khai báo địa chỉ IP cho container

- `--name`
Gắn tên cho container

- `--publish`, `-p` | `--publish-all`, `-P`
Do các container của docker được gộp và chạy trong một network riêng nên nó sẽ độc lập với máy chủ mà docker chạy trên đó. Để mở các cổng của network các container và ánh xạ nó với cổng của máy host ta sử dụng tùy chọn --publish, -p. Hoặc sử dụng --publish-all, -P sẽ mở tất cả các cổng của container.

    `docker run --publish 80:80 <image_name> bash`

- `--rm`
Tự động xóa container khi nó thoát.

- `--tty`, `-t`
Cấp một terminal ảo cho container. Tùy chọn này thường được sử dụng với --interactive, -i giúp cho STDIN mở ngay cả khi container chạy ở dạng ngầm.

- `--volume`, `-v`
Gắn một volume vào một container, cho phép chúng ta thao tác ở container nhưng dữ liệu vẫn được lưu trữ ở máy chủ.

    `docker run --volume /volume_name <image_name> bash`

- `--workdir`, `-w`
Chỉ định thư mục sẽ làm việc bên trong container. Giả sử ta sẽ làm việc với thư mục app trong docker

    `docker run --workdir /app <image_name> bash`


***Ví dụ 1: Run app***

```bash
docker run --name con_exam01 datkt98/exam01
```

    hello world 

***Ví dụ 2: Thay đổi port từ container sang local***

Trên app container ta cần sử dụng port `8888`, và ta muốn ánh xạ sang 1 port khác là `9000` trên host

```bash
docker run --name con_exam02 -p 9000:8888 datkt98/exam02
```

Trên host, lúc này ta truy cập http://172.17.0.2:5555

***Ví dụ 3: entry tới thư mục trong container***

```bash
docker run --rm -it --entrypoint bash myimage01
```

### Tạo container từ image by docker-compose

### Liệt kê các container đang chạy

`docker ps`: Lệnh này để liệt kê các container đang chạy

Khi sử dụng với các tham số

- `-a`/`-all`: Liệt kê tất cả các container, kể cả đang chạy hay đã kể thúc
- `-q`/`-quiet`: chỉ liệt kê ra id của các container.

Để liệt kệ các container đã tạo trước đó bạn dùng lệnh `docker ps -a`

```bash
docker ps -a
```

### Stop 1 container đang chạy

`docker stop <container_id>`: Lệnh này dùng để dừng 1 container đang chạy. Ví dụ như hình bên dưới bạn có container đang chạy với ID là 03a1db578cc3, bạn dùng lệnh `docker stop 03a1`

```bash
docker stop a6e267c
```

### Start 1 container

`docker start <container_id>`: Để start lại container đã dừng trước đó, bạn dùng lệnh docker start, ví dụ bạn start lại container đã stop phía trên dùng lệnh

```bash
docker start 03a1
```
### Xóa containers

`docker rm`: Lệnh này dùng để xóa 1 or nhiều container đã tạo trước đó, nếu container đang chạy, bạn cần thêm tham số `-f`

```bash
docker rm -f 9978bf498c50
```
### Xóa images
`docker rmi <list_image_id>`: Lệnh này dùng để xóa một hoặc nhiều images.

```bash
docker rmi -f b4d961f671a2
```

### Execute 1 lệnh trong container
`docker exec`: Lệnh này dùng để chạy 1 lệnh trong container, ví dụ bên dưới là liệt kê các tệp tin, thư mục trong folder root của container

```bash
docker exec 03a1 ls -la /root
```

### Hiện thị log trong container
`docker logs`: Lệnh này được sử dụng để hiển thị logs của một container, ta cần phải chỉ rõ container để hiển thị logs thông qua tên của nó. Ngoài cũng có thể sử dụng thêm một số flag như `--follow` để giữ việc theo dõi logs.

```bash
docker logs --follow <your_name_container>
```

### Liệt kê các volumn mà container sử dụng
`docker volume ls`: Lệnh này dùng để liệt kê ra các volumn mà các container sử dụng, volume là một cơ chế dùng để lưu trữ dữ liệu sinh ra và sử dụng bởi Docker.

```bash
docker volume ls
```

### Liệt kê các network
`docker network ls`: liệt kê tất cả các network có sẵn

```bash
docker network ls
```

### Liên kết network giữa các container
`docker network`: tạo connect vào một network mới. Nó giúp container giao tiếp được với một container khác qua tên thay vì mở cổng IP để giao tiếp trên host.

```bash
docker network
```

### Lưu trữ image
`docker save [OPTIONS] IMAGE [IMAGE...]`: save docker image to a tar archive

```bash
# using STDOUT
docker save image_name01 > image_name01.tar 

# using Write to a file, instead of STDOUT (want to specific output path)
docker save -o image_name01.tar > image_name01 

#gzip to smaller file
docker save image_name01:latest | gzip > image_name01.tar.gz 
```

### Load image từ file lưu trữ
`docker load [OPTIONS]`: load docker image from a tar archive or STDIN

```bash
# using STDIN
docker load < image_name01.tar.gz 

# Read from tar archive file (want to specific input path), instead of STDIN
docker load --input image_name01.tar 
```

## Dockerfile

Câu lệnh tạo file docker
```bash
# tạo thư mục
mkdir viblo 

# truy cập thư mục
cd viblo 

# tại file Dockerfile
touch Dockerfile
```

*Dockerfile* là một file dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho Docker Image. Từ những câu lệnh đó, Docker sẽ build ra Docker image (thường có dung lượng nhỏ từ vài MB đến lớn vài GB). 

_Dockerfile_ chứa tập hợp các lệnh để docker có thể đọc hiểu và **thực hiện theo thứ tự** để đóng gói thành một image theo yêu cầu người dùng

**[Các chỉ thị trong Dockerfile](https://docs.docker.com/engine/reference/builder/)**

| Thứ tự | Lệnh            | Mô tả bằng tiếng Việt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Cú pháp                        | Ví dụ                                                                                                                                                                                                       |
| ------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | **FROM**        | Tạo một giai đoạn build mới từ một image cơ sở. Là base image để chúng ta tiến hành build một image mới. Command này phải được đặt trên cùng của Dockerfile                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `FROM <image>`                 | `FROM ubuntu:20.04`                                                                                                                                                                                         |
| 2      | **ARG**         | Sử dụng biến trong quá trình build.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `ARG <variable_name>`          | `ARG VERSION=1.0` <br>`ARG APP_NAME=datkt` <br><br>`RUN echo "Building $APP_NAME version $APP_VERSION"`                                                                                                     |
| 3      | **LABEL**       | Thêm metadata cho image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `LABEL <key> =<value>`         | `LABEL maintainer="admin@example.com"`                                                                                                                                                                      |
| 3      | **MAINTAINER**  | Chỉ định tác giả của image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `MAINTAINER <name>`            | `MAINTAINER John Doe`                                                                                                                                                                                       |
| 4      | **ENV**         | Đặt các biến môi trường.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `ENV <key> =<value>`           | `ENV NODE_ENV=production`                                                                                                                                                                                   |
| 5      | **WORKDIR**     | Thay đổi thư mục làm việc mặc định trong container. Về sau, tất cả các câu lệnh sẽ chạy từ thư mục này. Phải set `WORKDIR` trước khi thực hiện các command liên quan đến đường dẫn.                                                                                                                                                                                                                                                                                                                                                                                                                                 | `WORKDIR <path>`               | `WORKDIR /usr/src/app`                                                                                                                                                                                      |
| 6      | **COPY**        | Sao chép tệp và thư mục. Chỉ thị `COPY` cũng giống với `ADD` là copy file, thư mục từ `<src>` và thêm chúng vào `<dest>` của container. Khác với `ADD`, nó không hỗ trợ thêm các file remote file URLs từ các nguồn trên mạng.                                                                                                                                                                                                                                                                                                                                                                                      | `COPY <source> <destination>`  | `COPY ./app /usr/src/app/`                                                                                                                                                                                  |
| 6      | **ADD**         | Thêm tệp và thư mục từ nguồn cục bộ hoặc từ xa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `ADD <source> <destination>`   | `ADD ./file.txt /app/`                                                                                                                                                                                      |
| 7      | **RUN**         | Thực thi các lệnh **trong quá trình build** và kết quả của các lệnh này được lưu trữ trong layer của image. <br><br>Khi khởi chạy container thì `CMD` chạy còn `RUN` không chạy.<br><br>**Ứng dụng**: Thường dùng để cài đặt phần mềm, cập nhật hệ điều hành, thiết lập môi trường hoặc bất kỳ lệnh nào cần thiết để chuẩn bị cho container.                                                                                                                                                                                                                                                                        | `RUN <command>`                | `RUN apt-get update && apt-get install -y git`<br><br>Ở đây, lệnh `RUN` sẽ cài đặt gói `git` vào image trong quá trình build. Khi quá trình build hoàn tất, gói đã được cài đặt sẽ tồn tại sẵn trong image. |
| 8      | **EXPOSE**      | Chỉ ra các cổng mà ứng dụng lắng nghe. Chỉ thị `EXPOSE` cho phép container mở publish port được chỉ định sau khi run từ image. Sau đó, ta có thể truy cập thông qua `<Container_id>:<port>`                                                                                                                                                                                                                                                                                                                                                                                                                         | `EXPOSE <port>`                | `EXPOSE 8080`                                                                                                                                                                                               |
| 9      | **ENTRYPOINT**  | Chỉ định chương trình thực thi mặc định của container.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `ENTRYPOINT ["executable"]`    | `ENTRYPOINT ["python"]`                                                                                                                                                                                     |
| 9      | **CMD**         | Chỉ định lệnh mặc định khi container chạy. <br><br>**Mục đích**: Chỉ định lệnh sẽ **chạy** khi container **khởi động** (runtime), tức là khi bạn chạy container từ image đã build. Kết quả không ảnh hưởng đến image, chỉ thực thi tại runtime<br><br>**Thời điểm thực thi**: `CMD` được thực thi khi container bắt đầu chạy, và chỉ có **một lệnh `CMD`** có thể tồn tại trong một Dockerfile (lệnh cuối cùng sẽ ghi đè các lệnh `CMD` trước đó). Khi khởi chạy container thì `CMD` chạy còn `RUN` không chạy<br><br>**Ứng dụng**: Dùng để chỉ định lệnh mặc định khi container chạy, như việc khởi động ứng dụng. | `CMD ["executable", "param1"]` | `CMD ["python", "app.py"]`                                                                                                                                                                                  |
| 10     | **HEALTHCHECK** | Kiểm tra tình trạng của container khi khởi động.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `HEALTHCHECK <options>`        | `HEALTHCHECK CMD curl --fail http://localhost:8080`                                                                                                                                                         |
| 11     | **SHELL**       | Đặt shell mặc định của image.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `SHELL ["executable", "flag"]` | `SHELL ["/bin/bash", "-c"]`                                                                                                                                                                                 |
| 12     | **USER**        | Thiết lập người dùng và nhóm ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `USER <user>`                  | `USER root`                                                                                                                                                                                                 |
| 13     | **VOLUME**      | Tạo các mount điểm volume.  Cho phép truy cập / liên kết thư mục giữa các container và máy chủ (host machine). Tạo 1 volume bên ngoài từ host hoặc 1 container khác mà container có thể giao tiếp được.                                                                                                                                                                                                                                                                                                                                                                                                             | `VOLUME ["/data"]`             | `VOLUME /var/lib/mysql`                                                                                                                                                                                     |
| 14     | **STOPSIGNAL**  | Chỉ định tín hiệu hệ thống để thoát container.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `STOPSIGNAL <signal>`          | `STOPSIGNAL SIGTERM`                                                                                                                                                                                        |
| 15     | **ONBUILD**     | Chỉ định các lệnh sẽ được thực thi khi image được sử dụng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `ONBUILD <instruction>`        | `ONBUILD RUN apt-get update`                                                                                                                                                                                |


## Docker compose


**Docker Compose** xây dựng template cho việc run docker image thành container, trong đó có thể run multi-container từ 1 image cùng lúc.

**Docker Compose** giúp đơn giản hóa việc quản lý và triển khai các ứng dụng phức tạp với nhiều container. Bằng cách sử dụng tệp cấu hình `docker-compose.yml`, bạn có thể định nghĩa rõ ràng các dịch vụ, mạng, và volumes cần thiết cho ứng dụng của mình, giúp cho việc triển khai và quản lý trở nên dễ dàng hơn rất nhiều.

**VÍ DỤ** triển khai một hệ thống mô hình AI tóm tắt văn bản với **Docker Compose**, chúng ta sẽ cần xây dựng một giải pháp bao gồm các thành phần chính sau:

1. **Ứng dụng Streamlit**: Để tạo giao diện người dùng tương tác cho người dùng nhập văn bản và xem bản tóm tắt.

3. **Mô hình AI**: Dịch vụ chạy mô hình tóm tắt văn bản.
4. **Cơ sở dữ liệu**: Để lưu trữ các bản tóm tắt và văn bản gốc.

### Cấu trúc Tổng Quan

- **Streamlit App (app.py)**: Chạy ứng dụng giao diện người dùng.

*Streamlit App (app.py)*
```python
import streamlit as st
import requests
import psycopg2

# Connect to database
conn = psycopg2.connect("dbname=summarizer user=user password=password host=db")
cursor = conn.cursor()

# Streamlit UI
st.title("Text Summarization App")

text = st.text_area("Enter text here:")

if st.button("Summarize"):
    if text:
        # Call model API
        response = requests.post("http://model:5000/summarize", json={"text": text})
        summary = response.json().get('summary', '')

        # Display summary
        st.write("Summary:")
        st.write(summary)

        # Save to database
        cursor.execute("INSERT INTO summaries (original_text, summary) VALUES (%s, %s)", (text, summary))
        conn.commit()
        st.write("Summary saved to database.")
    else:
        st.write("Please enter some text.")
```

- **Summary Model (model_server.py)**: Chạy mô hình tóm tắt văn bản, có thể là một API hoặc một dịch vụ mà Streamlit có thể gọi.

*Model Server (model_server.py)*
```python
from flask import Flask, request, jsonify
from your_model_library import load_model, summarize_text

app = Flask(__name__)
model = load_model('/models/summarization_model')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    summary = summarize_text(model, text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

- **Database**: Lưu trữ dữ liệu văn bản và bản tóm tắt.
### Cấu trúc tệp `docker-compose.yml`

```yaml
version: '3.8' 

services: 
	streamlit: 
		image: streamlit/streamlit:latest 
		ports: 
			- "8501:8501" 
		volumes: 
			- ./streamlit_app:/app 
		working_dir: /app 
		command: streamlit run app.py 
		depends_on: 
			- model 
			- db 
		environment: 
			- MODEL_API_URL=http://model:5000 
			- DATABASE_URL=postgresql://user:password@db:5432/summarizer 

model: 
image: yourmodelimage:latest ports: - "5000:5000" environment: - MODEL_PATH=/models/summarization_model volumes: - ./model:/models command: python model_server.py expose: - "5000" db: image: postgres:latest environment: POSTGRES_USER: user POSTGRES_PASSWORD: password POSTGRES_DB: summarizer volumes: - db_data:/var/lib/postgresql/data volumes: db_data:
```
### Cách Hoạt Động

1. **Ứng dụng Streamlit** cung cấp giao diện người dùng để nhập văn bản và hiển thị bản tóm tắt.
2. Khi người dùng nhấn nút "Summarize", ứng dụng Streamlit gửi yêu cầu đến dịch vụ mô hình (model service) qua API.
3. **Dịch vụ mô hình** nhận yêu cầu, xử lý văn bản bằng mô hình tóm tắt và trả kết quả về cho ứng dụng Streamlit.
4. **Ứng dụng Streamlit** lưu bản tóm tắt và văn bản gốc vào cơ sở dữ liệu PostgreSQL để lưu trữ.
5. **Cơ sở dữ liệu** lưu trữ tất cả các bản tóm tắt và văn bản gốc.