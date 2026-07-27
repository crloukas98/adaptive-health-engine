from src.inference.phenotype_predictor import (
    predict_phenotype
)


def test_predict_phenotype():

    cluster = predict_phenotype(
        age=28,
        weight_kg=122,
        height_cm=183,
        activity_score=5
    )

    assert cluster in [0, 1, 2, 3]