from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """Detects anomalies in spending data using Isolation Forest."""
    model = IsolationForest(contamination=0.05)
    df['Anomaly'] = model.fit_predict(df[['Value']])
    return df[df['Anomaly'] == -1] 
