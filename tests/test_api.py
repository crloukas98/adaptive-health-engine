from fastapi.testclient import TestClient

from src.api.app import app


client = TestClient(app)


def test_predict_endpoint():

    response = client.post(
        "/predict",
        json={
            "age": 28,
            "weight_kg": 122,
            "height_cm": 183,
            "activity_score": 5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "profile" in data
    assert "recommendations" in data

    assert "phenotype_name" in data["profile"]