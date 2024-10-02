import os

# Định nghĩa cấu trúc thư mục và tệp
structure = {
    "docs": {
        "references": {},
        "materials": {},
        "reports": {},
    },
    "config": {
        "config.yaml": None,
    },
    "data": {
        "external": {},
        "raw": {},
        "interim": {},
        "processed": {},
        "features": {},
    },
    "notebooks": {},
    "src": {
        "__init__.py": None,
        "data": {
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
    },
    "tests": {
        "test_model.py": None,
    },
    "output": {},
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
    ".gitignore": None,
    "environment.yml": None,
    "requirements.txt": None,
    "README.md": None,
    "setup.py": None,
    "main.py": None,
}


# Hàm tạo cấu trúc thư mục và tệp
def create_structure(structure, base_path=None):
    if base_path is None:
        base_path = input("Nhập đường dẫn thư mục project: ")
    assert os.path.exists(base_path), "Project folder not Found"
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            if not os.path.exists(path):
                open(path, "w").close()  # Tạo file trống
        else:
            # Nếu content không phải là None, tạo thư mục và đệ quy
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            create_structure(content, path)
    print("Structure for project created successfully!")


if __name__ == "__main__":
    create_structure(structure)
