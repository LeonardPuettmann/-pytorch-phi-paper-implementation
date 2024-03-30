import pandas as pd

def save_data(dataframe, path):
    return dataframe.to_parquet(path, index=False)

def load_data(path):
    return pd.read_parquet(path)