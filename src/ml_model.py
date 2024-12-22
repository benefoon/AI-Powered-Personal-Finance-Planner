import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def train_model(data):
    """Trains a model to predict future spending."""
    X = data[['category', 'month', 'day']]
    y = data['amount']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse:.2f}")
    return model

if __name__ == "__main__":
    processed_data = pd.read_csv("data/processed/cleaned_transactions.csv")
    model = train_model(processed_data)
    print("Model trained successfully!")
