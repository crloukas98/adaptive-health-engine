import pandas as pd


def create_activity_features(paq):

    activity = paq.copy()

    activity_features = pd.DataFrame()

    activity_features["SEQN"] = activity["SEQN"]

    activity_features["sedentary_minutes"] = (
        activity["PAD680"]
    )

    activity_features["vigorous_activity"] = (
        activity["PAQ650"].fillna(0)
    )

    activity_features["moderate_activity"] = (
        activity["PAQ665"].fillna(0)
    )

    activity_features["work_activity"] = (
        activity["PAQ605"].fillna(0) +
        activity["PAQ620"].fillna(0)
    )

    activity_features["activity_score"] = (
        activity_features["vigorous_activity"] +
        activity_features["moderate_activity"] +
        activity_features["work_activity"]
    )

    return activity_features

def clean_activity_features(df):

    df = df.copy()

    # NHANES missing codes
    df["sedentary_minutes"] = df["sedentary_minutes"].replace(
        [7777, 9999],
        pd.NA
    )

    # Impossible values
    df.loc[
        df["sedentary_minutes"] > 960,
        "sedentary_minutes"
    ] = pd.NA

    return df