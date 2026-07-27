def generate_health_profile(cluster_profile, cluster_id):
    """
    Convert phenotype data into a human-readable health profile.
    """

    profile = {
    "phenotype_id": int(cluster_id),
    "age": float(round(cluster_profile["age"], 1)),
    "bmi": float(round(cluster_profile["bmi"], 1)),
    "weight_kg": float(round(cluster_profile["weight_kg"], 1)),
    "activity_score": float(round(cluster_profile["activity_score"], 1)),
}

    return profile