from fastapi.testclient import TestClient

from main import app

client = TestClient(app=app)
base_url = ""


def test_health():
    response = client.get(f"{base_url}/health")
    assert response.status_code == 200
    assert response.json() == {"health": "ok"}
    print("pass: test_health")


def test_predict_item():
    response = client.post(
        f"{base_url}/predict",
        json={
            "instances": [
                {"text": "Cong hoa xa hoi chu nghia"},
                {"text": "doc lap"},
                {"text": "doc lap tich cuc"},
                {"text": "te doc"},
                {"text": "positive doc lap"},
            ]
        },
    )
    assert response.status_code == 200
    result = response.json()
    sentiments = [i["sentiment"] for i in result["predictions"]]
    assert sentiments == [
        "neutral",
        "negative",
        "neutral",
        "negative",
        "positive",
    ]
    print("pass: test_predict_item")


def test_predict_item_non_instance():
    response = client.post(
        f"{base_url}/predict",
        json={
            "instan": [
                {"text": "Cong hoa xa hoi chu nghia"},
                {"text": "doc lap"},
                {"text": "doc lap tich cuc"},
                {"text": "te doc"},
                {"text": "positive doc lap"},
            ]
        },
    )
    assert response.status_code == 400
    response.json() == {
        "detail": "Invalid input format. 'instances' should be a list of texts."
    }
    print("pass: test_predict_item_non_instance")


def test_predict_item_not_list():
    response = client.post(
        f"{base_url}/predict",
        json={"instan": {"text": "Cong hoa xa hoi chu nghia"}},
    )
    assert response.status_code == 400
    response.json() == {
        "detail": "Invalid input format. 'instances' should be a list of texts."
    }
    print("pass: test_predict_item_not_list")


if __name__ == "__main__":
    # test for running container
    import requests

    client = requests
    base_url = "http://127.0.0.1:8080"
    test_health()
    test_predict_item()
    test_predict_item_non_instance()
    test_predict_item_not_list()
