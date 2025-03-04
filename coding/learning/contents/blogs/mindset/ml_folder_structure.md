# Cấu trúc source code

**Khi tổ chức cấu trúc thư mục:**

- *Tách biệt mã nguồn và dữ liệu*: Đảm bảo dữ liệu, mã nguồn và các file kết quả luôn được tổ chức trong các thư mục riêng biệt.
- *Sử dụng notebooks cho khám phá*: Đặt các file notebook vào một thư mục riêng để tránh xung đột với mã nguồn chính.
- *Quản lý các bước xử lý dữ liệu*: Đặt các file xử lý dữ liệu vào thư mục riêng, tránh lẫn lộn với các phần khác như training mô hình.

```bash

project_name/
│
├── docs/                       # Tài liệu mô hình/dự án và tài liệu tham khảo, links, v.v.
│   └── references/                 # Tài liệu tham khảo, links, v.v.
│   └── materials/                  # Tài liệu mô hình/dự án
│   └── reports/                    # Báo cáo, kết quả phân tích (PDF, HTML, etc.)
│
├── data/                       # Dữ liệu thô và dữ liệu đã xử lý
│   ├── external/                   # Dữ liệu từ nguồn bên ngoài (không có update khi chạy production)
│   ├── raw/                        # Dữ liệu gốc (dữ liệu input khi model chạy production)
│   ├── interim/                    # Dữ liệu trung gian trong quá trình xử lý
│   ├── processed/                  # Dữ liệu đã được xử lý
│   ├── features/                   # (optional) Dữ liệu features được được tạo ra (chỉ lưu trong quá trình dev model)
│   └── output/                     # Kết quả dự đoán và các file output khác   
│
├── notebooks/                  # Các file notebook Jupyter
│
├── config/                      # Cấu hình dự án (hyperparameters, settings, etc.)
│   ├── .env.local                   # Config cho môi trường local
│   ├── .env.dev                   # Config cho môi trường dev
│   ├── .env.prod                   # Config cho môi trường prod
│   ├── config.py                   # Config chung
│   └── params.yaml                  # Tham số
│
├── src/                        # Mã nguồn chính của dự án
│   ├── __init__.py                 # File init để biến src thành module
│   ├── processing/                       # Xử lý dữ liệu
│   │   └── loader.py                   # Hàm tải dữ liệu
│   ├── features/                   # Xử lý đặc trưng dữ liệu
│   │   └── features.py                 # Trích xuất và xử lý đặc trưng
│   ├── models/                     # Mô hình machine learning/AI
│   │   ├── model.py                    # Định nghĩa mô hình
│   │   ├── train.py                    # Training mô hình
│   │   └── evaluate.py                 # Đánh giá mô hình
│   ├── visualization/              # Các hàm trực quan hóa dữ liệu
│   │   └── visualization.py 
│   ├── apps/                       # Giao diện tương tác
│   │   ├── api/                          # API
│   │   │   ├── __init__.py                 # File init để biến src thành module
│   │   │   ├── api.py                      # Main API
│   │   │   ├── dependencies.py             # Dependency config
│   │   │   ├── routers/                    # API
│   │   │   │   └── users.py                    # User endpoint
│   │   │   └── internal/                   # Internal config
│   │   │       └── admin.py                    # Admin endpoint
│   │   ├── streamlit/                  # Streamlit Web
│   │   │   └── streamlit_app.py            # Streamlit interface
│   │   └── app.py                      # Ứng dụng chính sử dụng Streamlit hoặc API đó để tương tác người dùng
│   └── utils/                      # Các hàm tiện ích, helpers
│       └── utils.py
│
├── tests/                      # Các bài test để kiểm tra module
│   └── test_model.py
│
├── logs/                       # File log (trong quá trình training)
│
├── scripts/                    # Các script để chạy training, inference
│   └── run_training.py             # Script chạy mô hình
│
├── models/                     # Mô hình đã được lưu lại
│ 
├── deployments/                # Tài liệu triển khai (Docker, GCP, etc.)
│   ├── Dockerfile                   # Dockerfile để container hóa ứng dụng
│   ├── docker-compose.yml          # File docker-compose (nếu sử dụng nhiều container)
│   ├── gcp_deployment.yaml         # Cấu hình cho việc deploy lên GCP Vertex AI
│   ├── cloud/                      # Scripts liên quan đến cloud deployment
│   │   ├── vertex_ai.py                # Script triển khai lên Vertex AI
│   │   └── cloudbuild.yaml             # Cấu hình Cloud Build trên GCP
│   └── kubernetes/                 # File để triển khai trên Kubernetes (nếu sử dụng)
│       ├── deployment.yaml             # Cấu hình triển khai trên Kubernetes
│       └── service.yaml                # Cấu hình dịch vụ trên Kubernetes
│
├── .gitignore                  # File gitignore để bỏ qua các file không cần commit
├── environment.yml             # Môi trường Anaconda/Conda (nếu dùng)
├── requirements.txt            # Thư viện cần thiết cho dự án
├── README.md                   # Thông tin dự án
├── main.py                     # Script chạy chính của model
└── setup.py                    # Cài đặt dự án thành package Python (nếu cần)

```

CODE PYTHON để gen structure theo template trên : [Project Structure Gennerator](https://github.com/datkt1998/notebooks/tree/master/coding/functions/pyfunc/utils/project_structure_gen.py)

## Ignore file

### `.gitignore` sample

```text
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.conda

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
.idea/
.DS_Store
**/.DS_Store

.vscode/

# dataset
data/
```

### `.gcloudignore` sample

```text
.gcloudignore
.gitignore
README.md
*.sh
.idea
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
__pycache__/
*.py[cod]
*.class
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
.DS_Store
tmp/

# test
tests/

# dataset
data/
```
