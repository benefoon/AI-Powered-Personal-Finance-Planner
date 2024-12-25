import matplotlib.pyplot as plt
import seaborn as sns

def visualize_spending(df):
    """Visualizes spending trends over time."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Transaction_Date', y='Value', hue='Category')
    plt.title('Spending Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount Spent')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
