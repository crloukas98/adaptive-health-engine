from src.inference.phenotype_predictor import (
    prepare_individual_features,
    predict_phenotype
)

from src.recommendations.report_generator import (
    generate_full_report
)

from src.recommendations.phenotype_labels import (
    PHENOTYPE_LABELS
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

    Parameters
    ----------
    age : float
        Age in years.

    weight_kg : float
        Body weight in kilograms.

    height_cm : float
        Height in centimeters.

    activity_score : float
        Activity index.

    Returns
    -------
    dict
        Health profile and recommendations.
    """

    # Predict phenotype cluster
    cluster = predict_phenotype(
        age,
        weight_kg,
        height_cm,
        activity_score
    )

    # Load phenotype interpretation
    phenotype_info = PHENOTYPE_LABELS[cluster]

    # Create feature vector
    features = prepare_individual_features(
        age,
        weight_kg,
        height_cm,
        activity_score
    )

    individual_features = features.iloc[0]


    # Generate report
    report = generate_full_report(
        individual_features,
        cluster
    )


    # Add explainable phenotype information
    report["profile"]["phenotype_name"] = (
        phenotype_info["name"]
    )

    report["profile"]["phenotype_description"] = (
        phenotype_info["description"]
    )


    return report