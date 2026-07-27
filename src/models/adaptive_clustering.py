import pandas as pd

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