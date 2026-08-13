import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)

def test_get(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200

def test_post_add(client: TestClient):
    response = client.post("/calculations", data={"firstNumber": 1, "secondNumber": 2, "operation": "+"})
    assert response.status_code == 200
    assert response.json() == 3

def test_post_zero_division(client: TestClient):
    response = client.post("/calculations", data={"firstNumber": 5, "secondNumber": 0, "operation": "/"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Second number cannot be zero'}
