import pandas as pd


def create_basic_health_features(df):
    """
    Transform NHANES body measurements
    into Adaptive Health Engine features.
    """

    features = pd.DataFrame()

    # Age
    features["age"] = df["RIDAGEYR"]

    # Weight
    features["weight_kg"] = df["BMXWT"]

    # Height
    features["height_cm"] = df["BMXHT"]

    # BMI
    features["bmi"] = df["BMXBMI"]

    return features


def clean_features(df):
    """
    Remove impossible values.
    """

    df = df.copy()

    df = df[
        (df["age"] > 0) &
        (df["weight_kg"] > 0) &
        (df["height_cm"] > 0) &
        (df["bmi"] > 0)
    ]

    return df