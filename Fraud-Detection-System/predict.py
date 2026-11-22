
import joblib
import pandas as pd
from pathlib import Path

# Get the directory where predict.py is located
BASE_DIR = Path(__file__).resolve().parent

# Load trained model using absolute path
MODEL_PATH = BASE_DIR / "models" / "fraud_model.pkl"

model = joblib.load(MODEL_PATH)


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
