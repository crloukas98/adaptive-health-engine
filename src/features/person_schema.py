from dataclasses import dataclass


@dataclass
class PersonProfile:
    """
    Unified representation of a person
    used by the adaptive health engine.
    """

    age: float
    bmi: float

    # Behavioral features
    executive_function: float
    impulsivity: float
    reward_sensitivity: float
    routine_stability: float

    # Lifestyle features
    sleep_quality: float
    activity_level: float

    # Health features
    metabolic_risk: float