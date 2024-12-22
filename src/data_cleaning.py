import pandas as pd

def load_raw_data(file_path):
    """Loads raw transaction data."""
    return pd.read_csv(file_path)

def clean_transaction_data(data):
    """Cleans and preprocesses transaction data."""
    data.dropna(inplace=True)
    data['amount'] = data['amount'].apply(lambda x: abs(x))
    data['date'] = pd.to_datetime(data['date'])
    return data

if __name__ == "__main__":
    raw_data = load_raw_data("data/raw/transactions.csv")
    cleaned_data = clean_transaction_data(raw_data)
    cleaned_data.to_csv("data/processed/cleaned_transactions.csv", index=False)
