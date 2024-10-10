
**Dev container** là một môi trường phát triển được đóng gói bên trong một **container** để cung cấp sự nhất quán và dễ dàng quản lý trong quá trình phát triển phần mềm. Container, thường dựa trên công nghệ như Docker, giúp tạo ra các môi trường phát triển độc lập và có thể tái tạo được, giúp giảm thiểu các vấn đề về cấu hình môi trường khi chuyển đổi giữa các máy hoặc giữa các thành viên trong nhóm.

Về cơ bản, **Dev container** tạo ra 1 bản sao về môi trường phát triển dự án (khác với đóng gói ứng dụng run trong môi trường production), bao gồm:
- Các phiên bản hệ điều hành khác nhau (Ubuntu, Fedora, Alpine...).
- Ngôn ngữ lập trình kèm phiên bản cụ thể: Node.js, Go, Java, Python,...
- Cơ sở dữ liệu: PostgreSQL, Redis, ...
- Các phần mềm, công cụ dòng lệnh hoặc thư viện hệ thống (như `gcc`, `make`, `curl`...)
Điều này đảm bảo tất cả mọi thứ đều giống nhau trên các máy khác nhau và các hệ điều hành khác nhau.

**Ví dụ**: Nếu một dự án yêu cầu Python 3.10 và một số công cụ phụ trợ như PostgreSQL và Redis để phát triển, việc cài đặt từng thành phần này theo cách thủ công và quản lý sự tương thích giữa chúng có thể phức tạp, nhưng với Dev Container, bạn có thể cấu hình tất cả trong một file `Dockerfile` hoặc `devcontainer.json`.
### Một số đặc điểm của **Dev Container**:

1. **Môi trường phát triển cô lập**: Dev container cho phép bạn chạy môi trường phát triển trong một container độc lập với hệ điều hành của máy chủ. Điều này có nghĩa là bạn có thể sử dụng các phiên bản cụ thể của phần mềm, thư viện và công cụ mà không làm ảnh hưởng đến hệ điều hành chính.

    **Ví dụ**: Nếu bạn đang làm việc trên hai dự án khác nhau, một dự án yêu cầu Python 3.6 và dự án khác yêu cầu Python 3.10, việc quản lý hai phiên bản Python cùng lúc có thể phức tạp và dễ gây lỗi. Dev container giúp bạn tạo các môi trường phát triển riêng biệt cho mỗi dự án.

2. **Tái tạo dễ dàng**: Với Dev container, bạn có thể mô tả chính xác môi trường phát triển (bao gồm các dependency, công cụ phát triển) trong các file cấu hình (ví dụ: `Dockerfile` hoặc `devcontainer.json`). Bất kỳ ai cũng có thể tái tạo môi trường này dễ dàng bằng cách kéo container từ repository về máy của họ.

	**Ví dụ**: Thay vì phải gửi hướng dẫn từng bước cài đặt môi trường cho từng hệ điều hành khác nhau, bạn chỉ cần cung cấp file cấu hình Dev Container và mỗi lập trình viên chỉ cần chạy nó để có được môi trường đầy đủ mà không phải lo về việc thiết lập thủ công.

3. **Cấu hình linh hoạt**: Bạn có thể cấu hình Dev container để chạy các phần mềm cụ thể, thậm chí những phần mềm không dễ cài đặt trực tiếp trên hệ điều hành chính của bạn. Ví dụ: bạn có thể dùng các phiên bản Python, Node.js, hoặc Go khác nhau cho mỗi dự án mà không cần cài đặt chúng trực tiếp trên máy.

4. **Đảm bảo tính nhất quán giữa các dev machine và CI/CD**: Dev Container đảm bảo mọi thành viên trong nhóm phát triển đều làm việc trong cùng một môi trường chuẩn. Điều này không chỉ đảm bảo tính nhất quán mà còn giúp giảm thiểu lỗi phát sinh do khác biệt về môi trường giữa các máy cá nhân và máy chủ CI/CD (Continuous Integration/Continuous Deployment).

	**Ví dụ**: Một thành viên trong nhóm đang sử dụng macOS, người khác sử dụng Windows, nhưng sản phẩm cuối cùng sẽ chạy trên Linux. Sử dụng Dev Container, bạn có thể tạo môi trường Linux trong container để mô phỏng chính xác môi trường triển khai cuối cùng, đảm bảo rằng mọi người đều phát triển trên cùng một môi trường.

5. **Tích hợp với IDE**: Một số IDE như **Visual Studio Code** hỗ trợ Dev container thông qua extension, giúp bạn có thể chạy mã nguồn và phát triển trực tiếp bên trong container mà không cần phải rời IDE. Điều này giúp việc phát triển trên các môi trường phức tạp trở nên đơn giản và đồng bộ hơn.

### Các thành phần chính của Dev Container:

1. `Dockerfile`: Đây là file mô tả cách xây dựng container, bao gồm việc cài đặt các dependency cần thiết.
2. `devcontainer.json`: File cấu hình của Dev container, chứa các thiết lập môi trường phát triển như extension cho IDE, các port cần mở, hay các công cụ cần cài đặt.

### Ví dụ về quy trình sử dụng Dev Container:

1. Bạn tạo một dự án với file `Dockerfile` và `devcontainer.json` để mô tả môi trường phát triển.
2. Khi một thành viên mới tham gia dự án, họ chỉ cần khởi động container trên máy của họ thông qua Docker, và mọi công cụ, thư viện sẽ được thiết lập tự động theo cấu hình đã định sẵn.
3. Mọi người trong nhóm sẽ làm việc trên cùng một môi trường phát triển, giảm thiểu rủi ro về việc "máy của tôi chạy được mà máy bạn thì không".

## Khác biệt của DevContainer vs AppContainer


| **TIêu chí**                                 | **AppContainer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | **DevContainer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ***Mục đích sử dụng***                       | - Mục đích chính là tạo ra một môi trường _runtime_ độc lập để chạy ứng dụng của bạn. Đây thường là cách làm khi bạn muốn triển khai ứng dụng vào môi trường production, hoặc chia sẻ một môi trường đã đóng gói sẵn để chạy ứng dụng mà không yêu cầu sự can thiệp của lập trình viên.<br><br>- Docker image đã được xây dựng trước và chỉ chứa các thành phần cần thiết để ứng dụng của bạn chạy, tối ưu cho mục đích sản xuất hoặc kiểm thử.                                                                                                                                           | - Mục đích chính là tạo ra một môi trường _phát triển_ thống nhất. Dev Container không chỉ chứa ứng dụng mà còn chứa các công cụ phát triển (IDE extensions, debugger, linter, formatter...) mà lập trình viên cần để phát triển và thử nghiệm mã.<br><br>- Dev Container được thiết kế để sử dụng tương tác với một **IDE** (như Visual Studio Code), nơi bạn có thể viết, chỉnh sửa và chạy mã trực tiếp trong container.                                                                                                             |
| ***Môi trường***                             | - Docker image thường chứa _runtime environment_, nghĩa là một môi trường được tối ưu hóa để chạy ứng dụng của bạn mà không cần bất kỳ công cụ phát triển nào. Docker image thường không chứa các công cụ như trình biên dịch, debugger, hoặc IDE extensions.<br><br>- Đây là môi trường không cần phải tương tác nhiều, và chỉ cần ứng dụng chạy đúng cách là đủ.<br><br>**Ví dụ:** Một Docker image để chạy một ứng dụng Flask có thể chỉ bao gồm Flask và các dependency cần thiết cho ứng dụng chạy, nhưng không có các công cụ như pylint hoặc mypy để phát hiện lỗi khi phát triển. | - Dev Container là một môi trường phát triển đầy đủ, có thể bao gồm các công cụ lập trình, trình gỡ lỗi (debugger), kiểm thử tự động, và các tiện ích mở rộng của IDE. Điều này giúp lập trình viên dễ dàng code, kiểm tra và sửa lỗi.<br><br>**Ví dụ:** Dev Container không chỉ chứa Flask và các dependency của nó mà còn bao gồm cả các công cụ như pytest để chạy test, pylint để kiểm tra chất lượng code, và cả các extension của Visual Studio Code để hỗ trợ phát triển nhanh chóng.                                            |
| ***Sự tương tác với IDE***                   | - Khi chạy một Docker image, lập trình viên thường không tương tác với môi trường bên trong container. Họ chỉ cần khởi động container và truy cập ứng dụng từ bên ngoài (thông qua terminal hoặc web).<br><br>- Để thay đổi mã nguồn, lập trình viên thường chỉnh sửa code trên máy cục bộ, sau đó build lại Docker image hoặc mount thư mục mã nguồn từ máy cục bộ vào container.                                                                                                                                                                                                        | - Dev Container được tích hợp trực tiếp với **IDE** (thường là Visual Studio Code). Điều này có nghĩa là lập trình viên có thể chỉnh sửa mã nguồn **trực tiếp bên trong container** mà không cần phải mount thủ công các thư mục hoặc build lại image.<br><br>- Các tiện ích mở rộng của IDE cũng có thể hoạt động bên trong Dev Container, giúp lập trình viên dễ dàng làm việc với các công cụ như linter, formatter, và debugger mà không cần cấu hình lại thủ công.                                                                 |
| ***Dễ dàng phát triển và chia sẻ***          | - Khi bạn cung cấp một Docker image, bạn đã tạo ra một phiên bản môi trường cố định. Các lập trình viên khác khi muốn thay đổi mã nguồn, sửa lỗi hoặc thêm tính năng phải sửa đổi trên máy cục bộ, sau đó rebuild lại Docker image hoặc phải sửa Dockerfile để rebuild lại môi trường.<br><br>- Docker image chủ yếu dùng để **chạy** ứng dụng, không phải để phát triển.                                                                                                                                                                                                                 | - Dev Container cung cấp một môi trường **động**, nơi bạn có thể phát triển, kiểm thử, và triển khai liên tục mà không cần phải rebuild lại từ đầu sau mỗi lần thay đổi. Khi làm việc với Dev Container, bạn có thể dễ dàng đồng bộ hóa toàn bộ môi trường giữa các thành viên trong nhóm mà không gặp khó khăn trong việc chia sẻ Dockerfile hoặc yêu cầu họ tự setup thủ công.<br><br>- Các file như `devcontainer.json` và `Dockerfile` dùng trong Dev Container giúp bạn dễ dàng cấu hình và chia sẻ toàn bộ môi trường phát triển. |
| ***Quy trình làm việc***                     | 1. Xây dựng Docker image một lần.<br>2. Chia sẻ hoặc triển khai Docker image để chạy ứng dụng.<br>3. Nếu cần phát triển thêm, lập trình viên chỉnh sửa code cục bộ và rebuild lại Docker image nếu cần thay đổi môi trường.<br>4. Người dùng chỉ cần chạy container từ Docker image mà không cần quan tâm đến cấu hình môi trường chi tiết.                                                                                                                                                                                                                                               | 1. Dev Container chứa cả môi trường phát triển và công cụ (IDE tích hợp) được cấu hình sẵn.<br>2. Lập trình viên không cần build lại Docker image thủ công mỗi khi chỉnh sửa code, mà có thể phát triển trực tiếp bên trong container.<br>3. Môi trường phát triển được đồng bộ hóa giữa tất cả các lập trình viên, không yêu cầu thiết lập phức tạp trên mỗi máy.                                                                                                                                                                      |
| ***Khả năng tái tạo môi trường phát triển*** | Môi trường chỉ tái tạo được ở mức **chạy ứng dụng**, nhưng không bao gồm đầy đủ môi trường phát triển. Để tái tạo môi trường phát triển (cài đặt các công cụ như debugger, linter, v.v.), người dùng phải làm thêm các bước cấu hình thủ công.                                                                                                                                                                                                                                                                                                                                            | Môi trường phát triển được tái tạo hoàn toàn. Khi lập trình viên khác clone dự án và mở bằng Visual Studio Code, mọi thứ (bao gồm các công cụ phát triển) sẽ được tự động cài đặt và sẵn sàng sử dụng.                                                                                                                                                                                                                                                                                                                                  |
| ***Sự linh hoạt và mở rộng***                | - Docker image cố định hơn và thường không thay đổi thường xuyên trong quá trình phát triển. Khi bạn tạo ra Docker image, mục tiêu là ổn định hóa môi trường **runtime**.<br><br>- Môi trường có thể hơi hạn chế nếu bạn cần thêm các công cụ phát triển mới hoặc cần thử nghiệm các tính năng mới.                                                                                                                                                                                                                                                                                       | - Dev Container linh hoạt hơn trong phát triển. Bạn có thể dễ dàng thay đổi hoặc mở rộng môi trường phát triển bằng cách thêm các công cụ vào `devcontainer.json` hoặc Dockerfile mà không làm ảnh hưởng đến quá trình phát triển hiện tại.<br><br>- Nếu bạn cần thêm công cụ phát triển mới, chỉ cần thêm vào file cấu hình và mọi người trong nhóm đều có thể cập nhật ngay lập tức.                                                                                                                                                  |

## Thiết lập DevContainer

Trong thư mục `.devcontainer` gồm 2 file `Dockerfile` và `devcontainer.json`

### `Dockerfile`
- `Dockerfile`: Dockerfile là file hướng dẫn cho Docker để xây dựng container. Nó chứa các lệnh để thiết lập môi trường hệ điều hành, cài đặt các thư viện và công cụ cần thiết để chạy ứng dụng.
```Dockerfile
# 1. Base image
FROM python:3.10-slim

# 2. Thiết lập người dùng, thư mục làm việc
RUN useradd -ms /bin/bash devuser
WORKDIR /workspace

# 3. Cài đặt các phụ thuộc hệ thống
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# 4. Cài đặt các thư viện Python từ requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy mã nguồn vào container
COPY . .

# 6. Expose port (nếu cần)
EXPOSE 8000

# 7. Command khởi chạy container (tùy chọn)
CMD ["python", "app.py"]
```

### `devcontainer.json`
 `devcontainer.json`: là file cấu hình dành riêng cho Visual Studio Code. Nó chỉ định cách Visual Studio Code sẽ khởi tạo và kết nối với Dev Container, và có thể định nghĩa các cài đặt khác như extensions, biến môi trường, và các lệnh sau khi container được tạo.
```json
{

    "name": "Python Dev Container", // Tên của Dev Container, được hiển thị trong Visual Studio Code
    "dockerFile": "Dockerfile", // Chỉ định tên file Dockerfile để xây dựng container. Ở đây là Dockerfile nằm trong cùng thư mục với devcontainer.json.
    "context": "..", //Chỉ định context mà Docker sẽ sử dụng khi build container. Context thường là thư mục gốc của project. ".." có nghĩa là Docker sẽ sử dụng thư mục cha của .devcontainer/ làm context.
    "settings": { //Các thiết lập dành cho Visual Studio Code khi kết nối với container. 
        "terminal.integrated.shell.linux": "/bin/bash" // Thiết lập shell mặc định là /bin/bash.
    },
    "extensions": [ // Danh sách các extension của VS Code được tự động cài đặt trong container.
        "ms-python.python", // Hỗ trợ phát triển Python.
        "esbenp.prettier-vscode" // Hỗ trợ định dạng code bằng Prettier.
    ],
    "postCreateCommand": "pip install -r requirements.txt", // Lệnh này được thực thi sau khi container đã được tạo xong.
    "runArgs": [   // Các tham số bổ sung khi chạy container. 
        "--cap-add=SYS_PTRACE", // Cho phép thêm quyền truy cập hệ thống.
        "--security-opt",
        "seccomp=unconfined" // Tắt seccomp để cho phép gỡ lỗi trong container (hữu ích cho gỡ lỗi với GDB).
    ],
    "remoteUser": "devuser",  // Chỉ định người dùng sẽ được sử dụng bên trong container. Trong ví dụ này, người dùng là devuser (được tạo trong Dockerfile).
    "containerEnv": { // Các biến môi trường được cài đặt trong container.
        "PYTHONUNBUFFERED": "1" // đảm bảo rằng output của Python sẽ không bị buffer hóa, giúp dễ dàng theo dõi log trong thời gian thực.
    },
    "portsAttributes": { // Cấu hình thuộc tính cho các cổng được mở trong container.
        "8000": { //  Ở đây, cổng 8000 sẽ tự động chuyển tiếp (forward) ra ngoài, và người dùng sẽ được thông báo khi điều này xảy ra.
            "label": "App",
            "onAutoForward": "notify"
        }
    },
    "mounts": [  // Cấu hình các mount points giữa máy host và container. 
        "source=/var/run/docker.sock,target=/var/run/docker.sock,type=bind" // Ở đây, Docker socket của máy host (/var/run/docker.sock) được mount vào container, giúp container có thể chạy Docker bên trong nó (Docker-in-Docker).
    ]
}
```
