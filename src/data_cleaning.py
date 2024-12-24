import pandas as pd

def clean_data(file_path):
    """Clean raw transaction data."""
    data = pd.read_csv(file_path)
    data.dropna(inplace=True)
    data["amount"] = data["amount"].apply(lambda x: abs(x))  # Ensure positive amounts
    return data

def normalize_amounts(data):
    """Normalize transaction amounts."""
    max_amount = data["amount"].max()
    data["amount_normalized"] = data["amount"] / max_amount
    return data

if __name__ == "__main__":
    # Load raw data
    raw_data = clean_data("data/raw/transactions.csv")
    
    # Normalize amounts
    processed_data = normalize_amounts(raw_data)
    
    # Save processed data
    processed_data.to_csv("data/processed/processed_transactions.csv", index=False)
    print("Data processing complete. Processed data saved.")
