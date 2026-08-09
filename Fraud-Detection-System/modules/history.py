import streamlit as st
import pandas as pd
from database import get_history

def show():

    st.title("📜 Prediction History")

    data = get_history()

    if len(data) == 0:
        st.info("No prediction history available.")
        return

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Total Transactions",
            "Normal Transactions",
            "Fraud Transactions",
            "Fraud %",
            "Prediction Time"
        ]
    )

    st.dataframe(df, use_container_width=True)