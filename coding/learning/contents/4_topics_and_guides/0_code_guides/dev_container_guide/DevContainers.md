
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

### Pre-requisites

Install:
- Docker, then enable **WSL using Ubuntu**
- VSCode + Remote Development extension
- Git

### Tạo Project folder

- Open WSL terminal (Ubuntu) and navigate to new project folder
![[navigate_project.webp]]
- Create the initial dev container config, _before_ I start writing my application code.
	- Command **Add Dev Container Configuration Files**: 
	![[add_dev_con.webp]]
	- Select **Python 3**, then choose whichever version you want to develop on. This will create a _.devcontainer_ folder with a _devcontainer.json_ file inside.
### Thiết lập tạo mới DevContainier

Trong thư mục `.devcontainer` gồm 2 file `Dockerfile` và `devcontainer.json`
#### `Dockerfile`
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
# CMD ["python", "app.py"]
```

#### `devcontainer.json`
 `devcontainer.json`: là file cấu hình dành riêng cho Visual Studio Code. Nó chỉ định cách Visual Studio Code sẽ khởi tạo và kết nối với Dev Container, và có thể định nghĩa các cài đặt khác như extensions, biến môi trường, và các lệnh sau khi container được tạo.
```json
{
    // Tên của Dev Container, được hiển thị trong Visual Studio Code
    "name": "Python Dev Container",
    
    // Image is Standard Image or Custom Image
    // More info: https://containers.dev/guide/dockerfile  
    // "image": "mcr.microsoft.com/devcontainers/python:1-3.12-bullseye"      

    // Chỉ định tên file Dockerfile để xây dựng container.
    "dockerFile": "Dockerfile",
    "context": "..",

    // các tham số khi chạy docker run thành image
    "runArgs": [
        "-p", "8080:80"
        // ,"--memory", "2g"
        // ,"--cpus", "2"
    ],

    // Thêm Features bổ sung cho dev container: https://containers.dev/features.
    // "features": {},                                                    

    // Cài đặt port của containe
    // Chỉ định các port được mở từ container ra local "host:port"
    "forwardPorts": [3000, "db:9999"],  
      
    // Cấu hình thuộc tính cho các cổng được mở trong container.                                          
    "portsAttributes": { "8000": { "label": "App", "onAutoForward": "notify" }},
    
    // Chạy các lệnh được lưu trong file .devcontainer/post-create.sh sau khi container được tạo xong
    "postCreateCommand": "bash .devcontainer/post-create.sh",
    // "postCreateCommand": "pip3 install --user -r requirements.txt",  
  
    // Thiết lập các biến môi trường
    "containerEnv": {
        "PYTHONUNBUFFERED": "1", // đảm bảo rằng output của Python sẽ không bị buffer hóa, giúp dễ dàng theo dõi log trong thời gian thực.
        "ENV": "dev"
    },

    // định nghĩa user chạy trong container, should be non-root if using Dockerfile
    "remoteUser": "devuser",

    // Configure tool-specific properties.  
    "customizations": {
        "settings": {
            "workbench.iconTheme":"vscode-icons",
            "workbench.colorCustomizations":{
               "editorError.background":"#ff4a3d5d",
               "notebook.cellBorderColor":"#a14b1836",
               "editor.lineHighlightBackground":"#4c5d7941",
               "editor.lineHighlightBorder":"#2c2c5a00",
               "editor.selectionBackground":"#997018",
               "editor.selectionHighlightBackground":"#0b34706e",
               "editor.wordHighlightBackground":"#0b34706e",
               "editorError.foreground":"#00000000"
            },
            "notebook.lineNumbers":"on",
            "security.workspace.trust.untrustedFiles":"open",
            "editor.suggestSelection":"first",
            "editor.fontFamily":"Hack Nerd, Fira Code, Roboto Mono, monospace",
            "editor.fontLigatures":true,
            "vsintellicode.modify.editor.suggestSelection":"automaticallyOverrodeDefaultValue",
            "git.enableSmartCommit":true,
            "git.decorations.enabled":false,
            "workbench.editorAssociations":{
               "*.xlsx":"default"
            },
            "gitlens.advanced.messages":{
               "suppressGitMissingWarning":true
            },
            "terminal.integrated.shell.linux":"/bin/bash",
            "editor.fontSize":13,
            "explorer.confirmDelete":false,
            "editor.unicodeHighlight.includeStrings":false,
            "indentRainbow.ignoreErrorLanguages":[
               "markdown",
               "haskell"
            ],
            "terminal.integrated.defaultProfile.osx":"zsh",
            "vsicons.dontShowNewVersionMessage":true,
            "indentRainbow.colors":[
               "rgba(255,255,64,0.03)",
               "rgba(127,255,127,0.03)",
               "rgba(255,127,255,0.03)",
               "rgba(79,236,236,0.03)"
            ],
            "jupyter.interactiveWindow.cellMarker.decorateCells":"allCells",
            "system-info.processorUsageType":"PROCESS",
            "[json]":{
               "editor.defaultFormatter":"esbenp.prettier-vscode"
            },
            "[sql]":{
               "editor.defaultFormatter":"inferrinizzard.prettier-sql-vscode"
            },
            "[yaml]":{
               "editor.defaultFormatter":"esbenp.prettier-vscode"
            },
            "ruff.lineLength":79,
            "cSpell.language":"en,vi",
            "workbench.startupEditor":"none",
            "editor.tabCompletion":"on",
            "emmet.triggerExpansionOnTab":true,
            "editor.useTabStops":false,
            "editor.stickyTabStops":true,
            "editor.acceptSuggestionOnEnter":"smart",
            "jupyter.widgetScriptSources":[
               "jsdelivr.com",
               "unpkg.com"
            ],
            "gitlens.launchpad.indicator.enabled":false,
            "vsintellicode.java.completionsEnabled":false,
            "files.autoSave":"onFocusChange",
            "python.analysis.logLevel":"Warning",
            "indentRainbow.indicatorStyle":"light",
            "indentRainbow.lightIndicatorStyleLineWidth":2,
            "indentRainbow.tabmixColor":"rgba(128,32,96,1)",
            "ruff.nativeServer":"on",
            "editor.defaultFormatter":"charliermarsh.ruff",
            "notebook.defaultFormatter":"charliermarsh.ruff",
            "[python]":{
               "editor.formatOnSave":true,
               "editor.codeActionsOnSave":{
                  "source.fixAll":"explicit",
                  "source.organizeImports":"explicit"
               },
               "editor.defaultFormatter":"charliermarsh.ruff"
            },
            "notebook.formatOnSave.enabled":true,
            "workbench.colorTheme":"One Dark Pro Italic Vivid",
            "interactiveWindow.executeWithShiftEnter":true,
            "git.openRepositoryInParentFolders":"always",
            "redhat.telemetry.enabled":true,
            "hediet.vscode-drawio.theme":"atlas"
         },
    "extensions": [
        "akamud.vscode-theme-onedark",
        // "alefragnani.bookmarks",
        "charliermarsh.ruff",
        "codeium.codeium",
        // "cweijan.dbclient-jdbc",
        // "cweijan.vscode-database-client2",  
        "donjayamanne.python-environment-manager",
        "donjayamanne.python-extension-pack",
        "eamodio.gitlens",
        "esbenp.prettier-vscode",
        "hediet.vscode-drawio",
        "inferrinizzard.prettier-sql-vscode",    
        "jsjlewis96.one-dark-pro-italic-vivid",
        "kevinrose.vsc-python-indent",
        // "masshuu12.system-info",
        "mechatroner.rainbow-csv",
        "ms-azuretools.vscode-docker",
        "ms-python.black-formatter",
        "ms-python.debugpy",
        "ms-python.isort",
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.datawrangler",
        "ms-toolsai.jupyter",
        "ms-toolsai.jupyter-keymap",
        "ms-toolsai.jupyter-renderers",
        // "ms-toolsai.vscode-jupyter-cell-tags",
        // "ms-toolsai.vscode-jupyter-slideshow",
        // "ms-vscode-remote.remote-containers",
        // "ms-vscode-remote.remote-ssh",
        // "ms-vscode-remote.remote-ssh-edit",
        // "ms-vscode-remote.remote-wsl",
        // "ms-vscode-remote.vscode-remote-extensionpack",
        // "ms-vscode.remote-explorer",
        // "ms-vscode.remote-server",
        // "mtxr.sqltools",
        // "mtxr.sqltools-driver-sqlite",
        "gruntfuggly.todo-tree",
        "pkief.material-icon-theme",
        "postman.postman-for-vscode",
        "redhat.vscode-yaml",
        "visualstudioexptteam.intellicode-api-usage-examples",
        "visualstudioexptteam.vscodeintellicode",
        "vscode-icons-team.vscode-icons",
        "yzhang.markdown-all-in-one"
        ]
    },  
    
    // Mount thư mục từ host vào container
    "mounts": [
        "source=path_on_host,target=path_in_container,type=bind" ,
        "source=/path/to/local/config.json,target=/workspace/config.json,type=bind"
    ]
}
```

- `name`: Tên của DevContainer
- `image`: nếu sử dụng từ 1 standard image mà không cần cài đặt gì thêm (không dùng custom image build từ Dockerfile), bỏ tham số này nếu sử dụng Dockerfile
- `dockerFile`: path của `Dockerfile` để build ra custom image cho devcontainer. `Dockerfile` thường nằm trong cùng thư mục với `devcontainer.json`.
- `context`: context mà Docker sẽ sử dụng khi build container. Context thường là thư mục gốc của project. ".." có nghĩa là Docker sẽ sử dụng thư mục cha của `.devcontainer/` làm context.
- `features`: Bổ sung các feature cho dev container
- `forwardPorts`: Chỉ định các port mà muốn forword từ container ra local theo định dạng `host:port` hoặc `port number`. Điều này cho phép bạn truy cập các service chạy bên trong container từ local machine.
- `portsAttributes`: Cấu hình thuộc tính cho các cổng được mở trong container và mặc định sẽ được forward ra ngoài và người dùng sẽ được thông báo khi điều này xảy ra.
- `postCreateCommand`: Lệnh này được thực thi sau khi container đã được tạo xong.
- `containerEnv`: set các cặp name-value pairs được chỉ định làm environment variables, Có thể sử dụng các biến được định nghĩa trước.
- `mounts`: Cấu hình các mount points giữa máy host và container.
	- `source`: Đường dẫn trên máy chủ cục bộ (host) mà bạn muốn mount vào container.
	- `target`: Đường dẫn trong container mà bạn muốn gắn (mount) thư mục hoặc tệp.
	- `type`: Kiểu mount, thường sử dụng giá trị `"bind"` cho việc mount tệp hoặc thư mục từ host vào container. `"volume"` cũng có thể được sử dụng khi tạo volume Docker.
- `remoteUser`: Chỉ định người dùng sẽ được sử dụng bên trong container, nếu sử dụng Dockerfile thì thường chỉ định non-root user.
- `runArgs`: Thêm các tham số khi run image, tương đương với các tham số khi chạy `docker run`
- `customizations`: Cài đặt VSCode settings và các extensions (Có thể sử dụng setting sync nếu đăng nhập lại VSCode account để đồng bộ hoá các cài đặt, tuy nhiên thường DevContainer sẽ là chia sẻ cho 1 người khác nên việc sync setting thông qua account thì không khả thi)
	- `settings`: Các settings cho VSCode khi kết nối với container.
	- `extensions`: Danh sách các extension của VS Code được tự động cài đặt trong container. Tips: Chạy lệnh `code --list-extensions` trong local VSCode 

### Build container

Make sure you have Docker Desktop running and press **Shift+Ctrl+P** and select **Reopen in Container**

