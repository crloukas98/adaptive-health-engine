from sklearn.cluster import KMeans


def create_clusters(
    data,
    n_clusters=3
):
    """
    Create unsupervised health profiles.
    """

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data)

    return labels, model