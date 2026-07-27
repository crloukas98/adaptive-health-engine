from src.models.adaptive_clustering import (
    load_adaptive_model
)


def test_model_loading():

    model, scaler = load_adaptive_model()

    assert model is not None
    assert scaler is not None