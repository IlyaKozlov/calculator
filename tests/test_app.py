import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)

def test_get(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200

@pytest.mark.parametrize(
    ("operation", "expected"),
    [
        ("+", 3),
        ("-", -1),
        ("*", 2),
        ("/", 0.5),
    ],
)
def test_post_calculation(client: TestClient, operation: str, expected: float):
    response = client.post(
        "/calculations",
        data={"firstNumber": 1, "secondNumber": 2, "operation": operation},
    )
    assert response.status_code == 200
    assert response.json() == expected


@pytest.mark.parametrize(
    ("operation",),
    [
        ("+",),
        ("*",)
    ]
)
def test_post_commutative(client: TestClient, operation:str):
    numbs = [0, 5, 9, 0.003, -3, 30_000_000]
    for n in numbs:
        for k in numbs:
            response = post_calculation(client,n,k, operation)
            reverse_response = post_calculation(client,k,n, operation)
            assert response.json() == reverse_response.json()

def post_calculation(client: TestClient, first_number: float, second_number:float, operation:str):
    response = client.post("/calculations", data={"firstNumber": first_number, "secondNumber": second_number, "operation": operation})
    assert response.raise_for_status()
    return response


@pytest.mark.parametrize(
    ("first_number", "operation", "second_number", "expected",),
    [
        (-2,"+", -4, -6),
        (-3,"-", -4, 1)
    ]
)
def test_post_negative_calculation(client, operation, first_number:float, second_number:float, expected:float):
   response = post_calculation(client = client, first_number = first_number, operation = operation, second_number = second_number)
   assert response.json() == expected


def test_post_zero_division(client: TestClient):
    response = client.post("/calculations", data={"firstNumber": 5, "secondNumber": 0, "operation": "/"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'Second number cannot be zero'}
