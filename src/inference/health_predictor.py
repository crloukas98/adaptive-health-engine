from src.inference.phenotype_predictor import (
    prepare_individual_features,
    predict_phenotype
)

from src.recommendations.profile_generator import (
    generate_health_profile
)

from src.recommendations.intervention_engine import (
    generate_recommendation
)


def predict_health_profile(
    age,
    weight_kg,
    height_cm,
    activity_score
):
    """
    Generate a complete adaptive health profile
    for a new individual.
    """

    cluster = predict_phenotype(
        age,
        weight_kg,
        height_cm,
        activity_score
    )

    features = prepare_individual_features(
        age,
        weight_kg,
        height_cm,
        activity_score
    )

    profile = generate_health_profile(
        features.iloc[0],
        cluster
    )

    recommendations = generate_recommendation(
        features.iloc[0]
    )

    return {
        "profile": profile,
        "recommendations": recommendations
    }