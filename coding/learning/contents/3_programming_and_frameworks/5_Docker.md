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

### Tạo container từ image
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

_Dockerfile_ chứa tập hợp các lệnh để docker có thể đọc hiểu và thực hiện để đóng gói thành một image theo yêu cầu người dùng

__Cú pháp của một Dockerfile__
```
INSTRUCTION arguments
```

trong đó:
- __INSTRUCTION__ là tên các chỉ thị có trong Dockerfile, mỗi chỉ thị thực hiện một nhiệm vụ nhất định, được Docker quy định. Khi khai báo các chỉ thị này phải được viết bằng chữ IN HOA.
- `aguments` là phần nội dung của các chỉ thị, quyết định chỉ thị sẽ làm gì.

Ví dụ:

```
FROM alpine:3.4

RUN apk update && \
    apk add curl && \
    apk add git && \
    apk add vim

```

**[Các chỉ thị trong Dockerfile](https://docs.docker.com/engine/reference/builder/)**
- **FROM**: Là base image để chúng ta tiến hành build một image mới. Command này phải được đặt trên cùng của Dockerfile
- **MAINTAINER**: Command này là tùy chọn, có thể có hoặc không. Nó chưa thông tin của người tiến hành xây dựng lên images.
- **RUN**: Sử dụng khi muốn thực thi một command trong quá trình build image
- **COPY**: Copy một file từ host machine tới docker image. Có thể sử dụng URL cho tệp tin cần copy, khi đó docker sẽ tiến hành tải tệp tin đó đến thư mục đích.
- **ENV**: Định nghĩa các biến môi trường
- **CMD**: Sử dụng khi muốn thực thi (execute) một command trong quá trình build một container mới từ docker image
- **ENTRYPOINT**: Định nghĩa những command mặc định, cái mà sẽ được chạy khi container running.
- **WORKDIR**: Định nghĩa directory cho **CMD**
- **USER**: Đặt user hoặc UID cho container được tạo bởi image
- **VOLUME**: Cho phép truy cập / liên kết thư mục giữa các container và máy chủ (host machine)
### `FROM`

Là base image để chúng ta tiến hành build một image mới. Command này phải được đặt trên cùng của Dockerfile

Chỉ định rằng image nào sẽ được dùng làm image cơ sở để quá trình build image thực thiện các câu lệnh tiếp theo. Các image base này sẽ được tải về từ Public Repository hoặc Private Repository riêng của mỗi người tùy theo setup.

Chỉ thị `FROM` là bắt buộc và phải được để lên phía trên cùng của Dockerfile.

__Cú pháp__
```
FROM <image> [AS <name>]
FROM <image>[:<tag>] [AS <name>]
FROM <image>[@<digest>] [AS <name>]
```

__Ví dụ__

```FROM ubuntu```
hoặc ```FROM ubuntu:latest```

###  `LABEL`

được dùng để thêm các thông tin `meta` vào Docker Image khi chúng được build. Chúng tồn tại dưới dạng các cặp `key` - `value`, được lưu trữ dưới dạng chuỗi. Có thể chỉ định nhiều label cho một Docker Image, và tất nhiên mỗi cặp `key` - `value` phải là duy nhất. Nếu cùng một key mà được khai báo nhiều giá trị (`value`) thì giá trị được khai báo gần đây nhất sẽ ghi đè lên giá trị trước đó.

__Cú pháp__
```
LABEL <key>=<value> <key>=<value> <key>=<value> ... <key>=<value>
```

__Ví dụ__

```
LABEL com.example.some-label="lorem"
LABEL version="2.0" description="Lorem ipsum dolor sit amet, consectetur adipiscing elit."
```

Để xem thông tin meta của một Docker Image, ta sử dụng dòng lệnh:
`docker inspect <image id>`

###  `RUN`

dùng để chạy một lệnh nào đó trong quá trình build image và thường là các câu lệnh Linux. Tùy vào image gốc được khai báo trong phần `FROM` thì sẽ có các câu lệnh tương ứng. Ví dụ, để chạy câu lệnh update đối với __Ubuntu__ sẽ là `RUN apt-get update -y` còn đối với __CentOS__ thì sẽ là `Run yum update -y`. Kết quả của câu lệnh sẽ được commit lại, kết quả commit đó sẽ được sử dụng trong bước tiếp theo của Dockerfile.

__Cú pháp__
```
RUN <command>
RUN ["executable", "param1", "param2"]
```

__Ví dụ__

```
RUN /bin/bash -c 'source $HOME/.bashrc; echo $HOME'
```
```
RUN ["/bin/bash", "-c", "echo hello"]
```
```
RUN apt-get update; \
    apt-get install curl -y
```

### `ADD`

Chỉ thị `ADD` sẽ thực hiện sao chép các tập, thư mục từ máy đang build hoặc remote file URLs từ `src` và thêm chúng vào filesystem của image `dest`.

__Cú pháp__
```
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
```
Trong đó:

- `src` có thể khai báo nhiều file, thư mục, ...
- `dest` phải là đường dẫn tuyệt đối hoặc có quan hệ chỉ thị đối với WORKDIR.

__Ví dụ__

```
ADD hom* /mydir/
ADD hom?.txt /mydir/
ADD test.txt relativeDir/
```


###  `COPY`

Chỉ thị `COPY` cũng giống với `ADD` là copy file, thư mục từ `<src>` và thêm chúng vào `<dest>` của container. Khác với `ADD`, nó không hỗ trợ thêm các file remote file URLs từ các nguồn trên mạng.

__Cú pháp__
```
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

__Ví dụ__

```
COPY hom* /mydir/
COPY hom?.txt /mydir/
COPY . .
```


###  `ENV`

Chỉ thị `ENV` dùng để khai báo các biến môi trường. Các biến này được khai báo dưới dạng `key` - `value` bằng các chuỗi. Giá trị của các biến này sẽ có hiện hữu cho các chỉ thị tiếp theo của __Dockerfile__.

__Cú pháp__
```
ENV <key>=<value> ...
```
__Ví dụ__

```
ENV DOMAIN="viblo.asia"
ENV PORT=80
ENV USERNAME="namdh" PASSWORD="secret"
```

Ngoài ra cũng có thể thay đổi giá trị của biến môi trường bằng câu lệnh khởi động container:
`docker run --env <key>=<value>`


###  `CMD`

Chỉ thị `CMD` định nghĩa các câu lệnh sẽ được chạy sau khi container được khởi động từ image đã build. Có thể khai báo được nhiều nhưng chỉ có duy nhất `CMD` cuối cùng được chạy.

__Cú pháp__
```
CMD ["executable","param1","param2"]
CMD ["param1","param2"]
CMD command param1 param2
```
__Ví dụ__

```
CMD ["python", "main.py"]
```


###  `EXPOSE`

Chỉ thị `EXPOSE` cho phép container mở publish port chỉ định sau khi run từ image.

__Cú pháp__
```
EXPOSE <port> [<port>/<protocol>...]
```
__Ví dụ__

```
EXPOSE 8080
```


###  `VOLUME`

Tạo 1 volume bên ngoài từ host hoặc 1 container khác mà container có thể giao tiếp được.

__Ví dụ__

```
VOLUME ["/data"]
```


###  `WORKDIR`

sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` __instructions__ that follow it in the Dockerfile. If the `WORKDIR` doesn’t exist, it will be created even if it’s not used in any subsequent Dockerfile instruction. Set `WORKDIR` trước khi thực hiện các __instructions__ trên.

__Cú pháp__
```
WORKDIR /path/to/workdir
```

__Ví dụ__

```
WORKDIR /Users/khongdat/Library/CloudStorage/GoogleDrive-k55.1613310017@ftu.edu.vn/My Drive/GitCode/My_learning/6. Docker
RUN pwd
```

## Các bước build image

Trước khi tiến hành các bước sau, hãy đảm bảo rằng trên máy của bạn đã được cài đặt [Docker](https://docs.docker.com/engine/installation/).

### Tạo Dockerfile


