from pydantic import BaseModel


class HealthInput(BaseModel):
    age: float
    weight_kg: float
    height_cm: float
    activity_score: float