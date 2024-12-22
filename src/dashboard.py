from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the financial dashboard."""
    data = pd.read_csv("data/processed/cleaned_transactions.csv")
    total_spent = data['amount'].sum()
    categories = data.groupby("category")["amount"].sum().to_dict()
    return render_template("dashboard.html", total_spent=total_spent, categories=categories)

if __name__ == "__main__":
    app.run(debug=True)
