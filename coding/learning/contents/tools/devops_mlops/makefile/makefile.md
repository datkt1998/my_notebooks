# Makefile

- [Giới thiệu về Makefile](#gi%E1%BB%9Bi-thi%E1%BB%87u-v%E1%BB%81-makefile)  
    1.1 [Make là gì?](#make-l%C3%A0-g%C3%AC)  
    1.2 [Vì sao nên sử dụng Makefile trong MLOps?](#v%C3%AC-sao-n%C3%AAn-s%E1%BB%AD-d%E1%BB%A5ng-makefile-trong-mlops)
    
- [Cài đặt và thiết lập môi trường](#c%C3%A0i-%C4%91%E1%BA%B7t-v%C3%A0-thi%E1%BA%BFt-l%E1%BA%ADp-m%C3%B4i-tr%C6%B0%E1%BB%9Dng)  
    2.1 [Kiểm tra Make đã có sẵn](#ki%E1%BB%83m-tra-make-%C4%91%C3%A3-c%C3%B3-s%E1%BA%B5n)  
    2.2 [Cài đặt Make trên các hệ điều hành](#c%C3%A0i-%C4%91%E1%BA%B7t-make-tr%C3%AAn-c%C3%A1c-h%E1%BB%87-%C4%91i%E1%BB%81u-h%C3%A0nh)
    
- [Cấu trúc cơ bản của Makefile](#c%E1%BA%A5u-tr%C3%BAc-c%C6%A1-b%E1%BA%A3n-c%E1%BB%A7a-makefile)  
    3.1 [Targets và Dependencies](#targets-v%C3%A0-dependencies)  
    3.2 [Phần thân (Recipe)](#ph%E1%BA%A7n-th%C3%A2n-recipe)  
    3.3 [Biến (Variables)](#bi%E1%BA%BFn-variables)  
    3.4 [Hàm (Functions) trong Makefile](#h%C3%A0m-functions-trong-makefile)
    
- [Các lệnh và tùy chọn quan trọng trong Make](#c%C3%A1c-l%E1%BB%87nh-v%C3%A0-t%C3%B9y-ch%E1%BB%8Dn-quan-tr%E1%BB%8Dng-trong-make)  
    4.1 [make](#make)  
    4.2 [make -f](#make--f)  
    4.3 [make -j](#make--j)  
    4.4 [make clean](#make-clean)  
    4.5 [make help](#make-help)
    
- [Các lưu ý khi viết Makefile](#c%C3%A1c-l%C6%B0u-%C3%BD-khi-vi%E1%BA%BFt-makefile)  
    5.1 [Dấu tab trong phần recipe](#d%E1%BA%A5u-tab-trong-ph%E1%BA%A7n-recipe)  
    5.2 [Quy ước đặt tên target](#quy-%C6%B0%E1%BB%9Bc-%C4%91%E1%BA%B7t-t%C3%AAn-target)  
    5.3 [Quy tắc về thứ tự rule](#quy-t%E1%BA%AFc-v%E1%BB%81-th%E1%BB%A9-t%E1%BB%B1-rule)  
    5.4 [Phần chú thích](#ph%E1%BA%A7n-ch%C3%BA-th%C3%ADch)
    
- [Ví dụ Makefile cơ bản cho MLOps](#v%C3%AD-d%E1%BB%A5-makefile-c%C6%A1-b%E1%BA%A3n-cho-mlops)  
    6.1 [Tải dữ liệu](#t%E1%BA%A3i-d%E1%BB%AF-li%E1%BB%87u)  
    6.2 [Tiền xử lý dữ liệu](#ti%E1%BB%81n-x%E1%BB%AD-l%C3%BD-d%E1%BB%AF-li%E1%BB%87u)  
    6.3 [Huấn luyện mô hình](#hu%E1%BA%A5n-luy%E1%BB%87n-m%C3%B4-h%C3%ACnh)  
    6.4 [Đóng gói và triển khai (Docker, v.v.)](#%C4%91%C3%B3ng-g%C3%B3i-v%C3%A0-tri%E1%BB%83n-khai-docker-vv)
    
- [Các kỹ thuật nâng cao](#c%C3%A1c-k%E1%BB%B9-thu%E1%BA%ADt-n%C3%A2ng-cao)  
    7.1 [Phân chia Makefile nhiều file](#ph%C3%A2n-chia-makefile-nhi%E1%BB%81u-file)  
    7.2 [Sử dụng Makefile trong CI/CD pipeline](#s%E1%BB%AD-d%E1%BB%A5ng-makefile-trong-cicd-pipeline)  
    7.3 [Tự động hoá với Shell script và Makefile](#t%E1%BB%B1-%C4%91%E1%BB%99ng-ho%C3%A1-v%E1%BB%9Bi-shell-script-v%C3%A0-makefile)
    
- [Tổng kết và tài nguyên tham khảo](#t%E1%BB%95ng-k%E1%BA%BFt-v%C3%A0-t%C3%A0i-nguy%C3%AAn-tham-kh%E1%BA%A3o)

## Giới thiệu về Makefile

### Make là gì?

- **Make** là một công cụ tự động hoá quá trình xây dựng (build) và quản lý các dự án phần mềm, thường được sử dụng trong các dự án C/C++.
- **Makefile** là tập tin cấu hình chứa tập hợp các quy tắc (rule) mà `make` sẽ sử dụng để biết cách và thời điểm cần (re)build các thành phần.
- Mặc dù ra đời ban đầu cho việc build chương trình C/C++, Makefile có thể được ứng dụng rộng rãi để **tự động hoá bất kỳ quy trình** nào, đặc biệt hữu ích trong **MLOps** khi ta cần chạy nhiều tác vụ (tải data, tiền xử lý, huấn luyện, đóng gói, v.v.).

### Vì sao nên sử dụng Makefile trong MLOps?

- **Tái sử dụng và kiểm soát phiên bản**: Dễ dàng quản lý các bước trong pipeline, nhất là khi dùng chung Git.
- **Tự động hoá**: Giúp tự động hoá mọi tác vụ lặp lại như cài dependencies, chạy training, evaluate, v.v.
- **Tính module hoá**: Chia nhỏ các tác vụ phức tạp thành các rule nhỏ, dễ bảo trì.
- **Tích hợp CI/CD**: Makefile có thể chạy trong các pipeline CI/CD (GitHub Actions, GitLab CI, Jenkins, v.v.) một cách dễ dàng.

---

## Cài đặt và thiết lập môi trường

### Kiểm tra Make đã có sẵn

Trước hết, hãy kiểm tra xem `make` đã được cài trên hệ thống chưa:

```bash
make --version
```

- Nếu có, bạn sẽ thấy phiên bản Make được in ra, ví dụ: `GNU Make 4.3 Built for x86_64-pc-linux-gnu`
- Nếu chưa được cài đặt, hãy cài theo hướng dẫn bên dưới.

### Cài đặt Make trên các hệ điều hành

- **Ubuntu/Debian**:
 ```bash
sudo apt-get update
sudo apt-get install build-essential
```
- **CentOS/Fedora/RHEL**:
 ```bash
sudo yum groupinstall "Development Tools"
```
- **macOS**:
    - Cài đặt [Xcode Command Line Tools](https://developer.apple.com/xcode/features/) (thường mặc định đã có `make`).
    - Hoặc dùng [Homebrew](https://brew.sh/):
    ```bash
	brew install make
	```
- **Windows**:
    - Sử dụng [MSYS2](https://www.msys2.org/) hoặc [Cygwin](https://www.cygwin.com/) để có lệnh `make`.
    - Hoặc dùng WSL (Windows Subsystem for Linux), cài như trên Ubuntu/Debian.

---

## Cấu trúc cơ bản của Makefile

Dưới đây là ví dụ tối giản:

```makefile
# Tên target: Danh sách dependencies
#     Lệnh recipe (thường cần dấu tab ở đầu dòng)
all: main.py data.csv                     # chạy trước 2 dependencies là main.py và data.csv
    python main.py

main.py:
    echo "print('Hello, MLOps!')" > main.py

data.csv:
    echo "col1,col2" > data.csv
    echo "1,2" >> data.csv
```
### Targets và Dependencies

- **Target**: Thường là file đầu ra (lúc này target đại diện cho file output sau khi chạy lệnh xong), hoặc tên nhiệm vụ (phím tắt). Ví dụ: `all`, `train`, `data.csv`.
	- mỗi _target_ mặc định được hiểu là một **tệp tin** (file) đầu ra — tức là, nếu bạn định nghĩa một target có tên trùng với một file, Make sẽ so sánh thời gian sửa đổi (timestamp) của target đó với các **dependencies** để quyết định xem có cần chạy **recipe** (các lệnh để tạo/update target) hay không.
- **Dependencies**: Những thứ target cần có trước khi chạy recipe. Nếu dependencies đã sẵn sàng và “mới hơn” target, lệnh recipe sẽ chạy để cập nhật target.
- **Phony target** `.PHONY` là một **danh sách** chỉ định những target nào **không** liên quan đến file trên đĩa. Thông báo cho Make rằng **đây chỉ là target mang tính “chức năng”** (task), chứ không gắn với một file cụ thể.
```makefile
.PHONY: all clean train

all: train
    @echo "All tasks done!"

train:
    python train.py --data data.csv --model model.pkl
    @echo "Training completed."

clean:
    rm -f data.csv processed.csv model.pkl
    @echo "Cleaned up."

```
- Nếu **không** có `.PHONY: clean`, Make sẽ kiểm tra xem có file tên `clean` trong thư mục hay không. Nếu có một file tên `clean`, Make có thể so sánh timestamp giữa file đó và dependencies (nếu có) để quyết định có chạy recipe hay không, hoặc thậm chí nhầm lẫn rằng “file `clean` đang mới hơn, ta không cần chạy lệnh rm... nữa”.
- **Khai báo `.PHONY: clean`** sẽ giúp Make luôn **chạy recipe** của `clean` khi bạn gõ `make clean`. Make **không** tìm file `clean` thực trên ổ đĩa để so sánh timestamp nữa.
- Lợi ích của việc khai báo `.PHONY`
	1. **Tránh trùng tên file**: Đảm bảo target luôn được thực thi, kể cả khi có file trùng tên.
	2. **Phản ánh rõ mục đích**: Cho Make biết những target nào là “chức năng” (task), không phải file đầu ra.
	3. **Tăng tính nhất quán**: Khi hợp tác với nhiều người, định nghĩa `.PHONY` giúp người khác nhanh chóng hiểu logic Makefile hơn.

> Nên đặt target `all` hoặc `help` lên đầu để làm **mặc định**.
### Phần thân (Recipe)

- Là các lệnh shell sẽ được chạy khi target cần cập nhật.
- Mỗi lệnh **bắt buộc phải bắt đầu bằng dấu tab** (thay vì dấu cách).
- Có thể chứa nhiều lệnh shell liên tiếp.
### Biến (Variables)

- Giúp tái sử dụng các giá trị và tránh lặp code.

```makefile
PYTHON = python3
DATA = data.csv

preprocess:
	$(PYTHON) preprocess_pipeline.py --data=$(DATA)

train: preprocess                      # để chạy train cần preprocess chạy trước
    $(PYTHON) train.py --data=$(DATA)
```
- Sử dụng cú pháp `$(BIEN)` để gọi biến.
### Hàm (Functions) trong Makefile

- Make hỗ trợ một số hàm tiện ích như `shell`, `wildcard`, `patsubst`, v.v.
- Ví dụ, muốn lấy danh sách file `.py`:
```makefile
SRC = $(wildcard *.py)
```
    
- Hoặc gọi lệnh shell:
```makefile
GIT_COMMIT := $(shell git rev-parse HEAD)
```
    
---

## Các lệnh và tùy chọn quan trọng trong Make

### `make`

- Lệnh mặc định để chạy. `make` sẽ tìm file `Makefile` hoặc `makefile` trong thư mục hiện tại.
- Khi gọi không kèm target, `make` sẽ chạy target đầu tiên trong Makefile.

### `make -f`

- Chỉ định tệp Makefile cụ thể: `make -f MyMakefile`

### `make -j`

- Chạy song song nhiều job (ví dụ, build nhiều file cùng lúc). Rất hữu ích khi build các project lớn: `make -j 4`

### `make clean`

- Thường được định nghĩa như một target để dọn dẹp file tạm, file build cũ. Ví dụ: 
```makefile
clean:     
	rm -rf *.o *.pyc
```
- Để chạy: `make clean`

### `make help`

- Hay được sử dụng để liệt kê các target kèm mô tả. Ví dụ:
```makefile
help:
    @echo "Possible targets:"
    @echo "  train   : Train the model"
    @echo "  clean   : Remove temporary files"
```

---
## Ví dụ Makefile cơ bản cho MLOps

```makefile

.PHONY: all data preprocess train docker-build docker-run clean

all: train

data:
    wget https://example.com/dataset.csv -O data.csv
    echo "Data downloaded."

preprocess: data
    python3 preprocess.py --input data.csv --output processed.csv
    echo "Data preprocessed."

train: preprocess
    python3 train.py --data processed.csv --model model.pkl
    echo "Model trained."

docker-build: train
    docker build -t my-ml-model:latest .
    echo "Docker image built."

docker-run:
    docker run -p 8080:8080 my-ml-model:latest
    echo "Docker container is running."

clean:
    rm -f data.csv processed.csv model.pkl
    echo "Cleaned up."

```
- `make data` tải dữ liệu từ nguồn nào đó (s3, http,...).
- `make preprocess`: trước khi chạy preprocess, Make sẽ kiểm tra và gọi `data` (nếu chưa có hoặc cũ hơn).
- `make train` (tự động gọi `preprocess`)
- `make docker-build` (tự động gọi `train`): `docker-build` phụ thuộc vào `train` để đảm bảo model đã được huấn luyện trước khi đóng gói vào container.
- `make docker-run` chạy container đã build
- `make all` chạy target `train` (vì `all: train`)

---

## Các kỹ thuật nâng cao

### Phân chia Makefile nhiều file

Khi dự án lớn, có thể chia Makefile thành nhiều file để dễ quản lý: 
- `Makefile` chính: bao gồm rule cơ bản và lệnh `include`:
```makefile
include Makefile.data
include Makefile.model
include Makefile.deploy
```
- `Makefile.data`: chứa các rule liên quan đến dữ liệu.
- `Makefile.model`: chứa các rule liên quan đến huấn luyện, test, v.v.
- `Makefile.deploy`: chứa các rule liên quan đến Docker, k8s, deploy, v.v.

### Sử dụng Makefile trong CI/CD pipeline

- **GitHub Actions**:
```yaml
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: make install  # Giả sử có target install
      - name: Run training
        run: make train
      - name: Build Docker
        run: make docker-build
```
- **GitLab CI** hay **Jenkins** cũng tương tự, ta chỉ cần chạy các lệnh `make` tương ứng.

### Tự động hoá với Shell script và Makefile

- Kết hợp lệnh Shell script phức tạp trong `*.sh` với Makefile, khi **Makefile** chỉ gọi shell script tương ứng.
```makefile
.PHONY: train
train:
    bash scripts/train.sh
```
- Giúp tổ chức code sạch hơn, tách logic dài ra khỏi Makefile.

---
## Tổng kết và tài nguyên tham khảo

- **Makefile** là một công cụ mạnh mẽ để **tự động hoá** và **quản lý** quy trình MLOps.
- Với một cấu trúc rule - dependencies - recipe đơn giản, ta có thể thiết lập và duy trì pipeline MLOps hiệu quả, từ tải dữ liệu, tiền xử lý, huấn luyện cho đến đóng gói, triển khai.
- Kết hợp Makefile với các CI/CD platform (GitHub Actions, GitLab CI, Jenkins,...) sẽ giúp **tự động hoá** mọi thứ, giảm thiểu sai sót, rút ngắn thời gian phát triển và triển khai.