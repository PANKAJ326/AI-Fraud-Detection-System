import streamlit as st
import pandas as pd
import plotly.express as px
import os


def show():

    st.title("📊 Analytics Dashboard")

    if not os.path.exists("data/latest_prediction.csv"):
        st.warning("No prediction data found. Please run Fraud Detection first.")
        return

    df = pd.read_csv("data/latest_prediction.csv")

    total = len(df)
    fraud = len(df[df["Prediction"] == "Fraud Transaction"])
    normal = len(df[df["Prediction"] == "Normal Transaction"])

    fraud_percentage = (fraud / total) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total", total)
    col2.metric("Normal", normal)
    col3.metric("Fraud", fraud)
    col4.metric("Fraud %", f"{fraud_percentage:.2f}%")

    st.divider()

    chart = pd.DataFrame({
        "Transaction": ["Normal", "Fraud"],
        "Count": [normal, fraud]
    })

    pie = px.pie(
        chart,
        names="Transaction",
        values="Count",
        title="Normal vs Fraud Transactions"
    )

    bar = px.bar(
        chart,
        x="Transaction",
        y="Count",
        title="Transaction Distribution"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(pie, use_container_width=True)

    with col2:
        st.plotly_chart(bar, use_container_width=True)

    st.subheader("Latest Prediction")

    st.dataframe(df.head(20))