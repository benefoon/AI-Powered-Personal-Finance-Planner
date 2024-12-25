import pandas as pd

def clean_data(df):
    """Cleans the DataFrame by filling missing values and removing outliers."""
    df.fillna(method='ffill', inplace=True)
    df = df[(df['Value'] < df['Value'].quantile(0.95)) & (df['Value'] > df['Value'].quantile(0.05))]
    return df
