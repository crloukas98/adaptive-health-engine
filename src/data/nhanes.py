import pandas as pd


def load_dataset(path):
    """
    Load a dataset from CSV.
    """

    df = pd.read_csv(path)

    return df


def inspect_dataset(df):
    """
    Basic dataset inspection.
    """

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isnull().sum().sort_values(ascending=False).head(20))


if __name__ == "__main__":

    print("NHANES loader ready")