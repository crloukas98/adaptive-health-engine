from fastapi import FastAPI

from src.api.schemas import HealthInput

from src.inference.health_predictor import (
    predict_health_profile
)


app = FastAPI(
    title="Adaptive Health Engine",
    description="AI-powered phenotype prediction and intervention engine",
    version="1.0"
)


@app.get("/")
def root():
    return {
        "message": "Adaptive Health Engine API running"
    }


@app.post("/predict")
def predict(
    data: HealthInput
):

    result = predict_health_profile(
        age=data.age,
        weight_kg=data.weight_kg,
        height_cm=data.height_cm,
        activity_score=data.activity_score
    )

    return result