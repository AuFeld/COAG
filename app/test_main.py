from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/", tags=["Root"])
    assert response.status_code == 200
    assert response.json() == {"message": "Wecome to COAG!"}