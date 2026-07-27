from src.recommendations.profile_generator import (
    generate_health_profile
)

from src.recommendations.intervention_engine import (
    generate_recommendation
)


def generate_full_report(cluster_profile, cluster_id):
    """
    Generate complete adaptive health report.
    """

    profile = generate_health_profile(
        cluster_profile,
        cluster_id
    )

    recommendations = generate_recommendation(
        cluster_profile
    )

    report = {
        "profile": profile,
        "recommendations": recommendations
    }

    return report