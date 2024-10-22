import os

# Định nghĩa cấu trúc thư mục và tệp
structure = {
    "docs": {
        "references": {},
        "materials": {},
        "reports": {},
    },
    "data": {
        "external": {},
        "raw": {},
        "interim": {},
        "processed": {},
        "features": {},
        "output": {},
    },
    "notebooks": {},
    "config": {
            ".env.local": None,
            ".env.dev": None,
            ".env.prod": None,
            "config.py": None,
            "params.yaml": None,
        },
    "src": {
        "__init__.py": None,
        "processing": {
            "loader.py": None,
        },
        "features": {
            "features.py": None,
        },
        "models": {
            "model.py": None,
            "train.py": None,
            "evaluate.py": None,
        },
        "visualization": {
            "visualization.py": None,
        },
        "utils": {
            "utils.py": None,
        },
        "apps": {
            "api": {
                "api.py": None,
                "__init__.py": None,
                "dependencies.py": None,
                "routers": {"users.py": None},
                "internal": {"admin.py": None},
            },
            "streamlit": {
                "streamlit_app.py": None,
            },
            "app.py": None,
        },
    },
    "tests": {
        "test_model.py": None,
    },
    "logs": {},
    "scripts": {
        "run_training.py": None,
    },
    "models": {},
    "deployments": {
        "Dockerfile": None,
        "docker-compose.yml": None,
        "gcp_deployment.yaml": None,
        "cloud": {
            "vertex_ai.py": None,
            "cloudbuild.yaml": None,
        },
        "kubernetes": {
            "deployment.yaml": None,
            "service.yaml": None,
        },
    },
    ".gitignore": None,
    "environment.yml": None,
    "requirements.txt": None,
    "README.md": None,
    "setup.py": None,
    "main.py": None,
}

example = {}
example[".gitignore"] = """
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
"""

example[".env.local"] = """
# Environment runtime
ENV=local
"""
example[".env.dev"] = """
# Environment runtime
ENV=dev
"""
example[".env.prod"] = """
# Environment runtime
ENV=prod
"""
example['requirements.txt'] = """
pip-chill
"""


# Hàm tạo cấu trúc thư mục và tệp
def create_structure(structure, base_path=None, print_structure=False):
    if base_path is None:
        base_path = input("Nhập đường dẫn thư mục project: ")
    assert os.path.exists(base_path), "Project folder not Found"
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            if not os.path.exists(path):
                if example.get(name) is not None:
                    with open(path, "w") as f:
                        f.write(example[name])
                else:
                    open(path, "w").close()  # Tạo file trống
        else:
            # Nếu content không phải là None, tạo thư mục và đệ quy
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            create_structure(content, path)
    if print_structure:
        print("Structure for project created successfully!")


if __name__ == "__main__":
    create_structure(structure, print_structure=True)
