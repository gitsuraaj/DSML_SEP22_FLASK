import pytest
from hello import app
import json

@pytest.fixture
def client():
    return app.test_client()

def test_ping_something(client):
    resp=client.get("/ping")
    assert resp.status_code == 200


def test_predictions(client):
    test_data= {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome": 5000000,
    "LoanAmount": 5000,
    "Credit_History": 1.0}

    resp=client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {"loan_approval_status": "Accepted"}



