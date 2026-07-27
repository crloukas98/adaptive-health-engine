def generate_recommendation(cluster_profile):

    bmi = cluster_profile["bmi"]
    activity = cluster_profile["activity_score"]
    age = cluster_profile["age"]

    recommendations = []

    # High adiposity
    if bmi >= 35:
        recommendations.append(
            "High adiposity phenotype: prioritize sustainable weight reduction and metabolic health."
        )

        recommendations.append(
            "Preserve muscle mass through resistance training and adequate protein intake."
        )

    # Low activity
    if activity < 6:
        recommendations.append(
            "Low activity phenotype: gradually increase daily movement and structured exercise."
        )

    # Aging
    if age >= 60:
        recommendations.append(
            "Older phenotype: emphasize strength training, mobility, and fall prevention."
        )

    # Healthy maintenance
    if len(recommendations) == 0:
        recommendations.append(
            "Maintain current lifestyle behaviors and monitor long-term trends."
        )

    return recommendations