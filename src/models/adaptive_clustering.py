import pandas as pd
import joblib
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def create_adaptive_clusters(df, n_clusters=4):

    data = df.drop(columns=["SEQN"]).copy()

    data = data.fillna(
        data.median()
    )

    scaler = StandardScaler()

    scaled = scaler.fit_transform(data)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(scaled)

    result = df.copy()
    result["cluster"] = clusters

    return result, model, scaler


def save_adaptive_model(model, scaler):
    """
    Save trained clustering model
    and scaler for inference.
    """

    path = Path("../src/models/artifacts")

    path.mkdir(
    parents=True,
    exist_ok=True
    )
    joblib.dump(
        model,
        path / "adaptive_cluster_model.pkl"
    )

    joblib.dump(
        scaler,
        path / "adaptive_scaler.pkl"
    )


def load_adaptive_model():
    """
    Load trained clustering model
    and scaler.
    """

    path = Path("../src/models/artifacts")

    model = joblib.load(
        path / "adaptive_cluster_model.pkl"
    )

    scaler = joblib.load(
        path / "adaptive_scaler.pkl"
    )

    return model, scaler