import streamlit as st

def show():

    st.title("💳 AI-Based Online Transaction Fraud Detection System")

    st.markdown("""
    ### Welcome 👋

    This system helps banks and financial institutions detect
    fraudulent online transactions using Machine Learning.

    ---
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", "100000")

    col2.metric("Fraud Transactions", "170")

    col3.metric("Detection Accuracy", "99.8%")

    st.info("✔ Upload a transaction CSV file from the Fraud Detection menu.")