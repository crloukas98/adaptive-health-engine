import pandas as pd

from src.models.adaptive_clustering import (
    load_adaptive_model
)


def prepare_individual_features(
    age,
    weight_kg,
    height_cm,
    activity_score,
    sedentary_minutes=300,
    vigorous_activity=1,
    moderate_activity=1,
    work_activity=3
):
    """
    Prepare individual health features.
    """

    bmi = weight_kg / ((height_cm / 100) ** 2)

    features = pd.DataFrame([{
        "age": age,
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "bmi": bmi,
        "sedentary_minutes": sedentary_minutes,
        "vigorous_activity": vigorous_activity,
        "moderate_activity": moderate_activity,
        "work_activity": work_activity,
        "activity_score": activity_score
    }])

    return features

def predict_phenotype(
    age,
    weight_kg,
    height_cm,
    activity_score
):
    """
    Predict phenotype cluster for a new individual.
    """

    model, scaler = load_adaptive_model()

    features = prepare_individual_features(
        age,
        weight_kg,
        height_cm,
        activity_score
    )

    scaled = scaler.transform(features)

    cluster = model.predict(
        scaled
    )[0]

    return int(cluster)