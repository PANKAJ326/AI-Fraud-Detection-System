import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/fraud_model.pkl")

def predict_transactions(data):
    """
    Predict fraud for uploaded transaction data.
    Returns dataframe with prediction column.
    """

    prediction = model.predict(data)

    result = data.copy()

    result["Prediction"] = prediction

    result["Prediction"] = result["Prediction"].map({
        0: "Normal Transaction",
        1: "Fraud Transaction"
    })

    return result