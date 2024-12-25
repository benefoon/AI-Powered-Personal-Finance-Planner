import pandas as pd

def feature_engineering(df):
    """Creates new features from the transaction data."""
    df['Transaction_Date'] = pd.to_datetime(df['Transaction_Date'])
    df['Month'] = df['Transaction_Date'].dt.month
    df['Year'] = df['Transaction_Date'].dt.year
    df['Category'] = df['Description'].apply(lambda x: categorize_transaction(x))
    return df
