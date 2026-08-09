import streamlit as st
import pandas as pd
import os
import time
import plotly.express as px

from predict import predict_transactions
from database import create_database, save_prediction


def show():

    # ---------- Session State ----------
    if "prediction_result" not in st.session_state:
        st.session_state.prediction_result = None

    # ---------- Title ----------
    st.title("🛡 Fraud Detection")
    st.write("Upload a CSV file to detect fraudulent transactions.")

    # ---------- Upload CSV ----------
    uploaded_file = st.file_uploader(
        "Choose CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head(), use_container_width=True)

        st.info(f"📂 Total Records Uploaded: {len(df)}")

        if st.button("🚀 Predict Fraud", use_container_width=True):

            with st.spinner("🔍 AI is analyzing transactions..."):

                progress = st.progress(0)

                for i in range(100):
                    time.sleep(0.01)
                    progress.progress(i + 1)

                # Remove target column if present
                if "Class" in df.columns:
                    input_data = df.drop(columns=["Class"])
                else:
                    input_data = df

                result = predict_transactions(input_data)

                # Save in session
                st.session_state.prediction_result = result

                progress.empty()

                total = len(result)
                fraud_count = len(
                    result[result["Prediction"] == "Fraud Transaction"]
                )

                normal_count = len(
                    result[result["Prediction"] == "Normal Transaction"]
                )

                percentage = (fraud_count / total) * 100

                create_database()

                save_prediction(
                    total,
                    normal_count,
                    fraud_count,
                    percentage
                )

                os.makedirs("data", exist_ok=True)

                result.to_csv(
                    "data/latest_prediction.csv",
                    index=False
                )

    # ---------- Show Result ----------
    if st.session_state.prediction_result is not None:

        result = st.session_state.prediction_result

        total = len(result)

        fraud_count = len(
            result[result["Prediction"] == "Fraud Transaction"]
        )

        normal_count = len(
            result[result["Prediction"] == "Normal Transaction"]
        )

        st.success("✅ Prediction Completed Successfully!")

        if fraud_count > 0:
            st.error(f"🚨 {fraud_count} Fraud Transactions Detected.")
        else:
            st.success("🎉 No Fraudulent Transactions Found.")

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        col1.metric("📄 Total Transactions", total)
        col2.metric("✅ Normal Transactions", normal_count)
        col3.metric("🚨 Fraud Transactions", fraud_count)

        st.markdown("---")

        st.subheader("📊 Prediction Result")

        filter_option = st.selectbox(
            "📂 Filter Transactions",
            [
                "All",
                "Fraud Only",
                "Normal Only"
            ]
        )

        filtered_result = result.copy()

        if filter_option == "Fraud Only":
            filtered_result = filtered_result[
                filtered_result["Prediction"] == "Fraud Transaction"
            ]

        elif filter_option == "Normal Only":
            filtered_result = filtered_result[
                filtered_result["Prediction"] == "Normal Transaction"
            ]

        st.write(f"📄 Showing {len(filtered_result)} Records")

        st.dataframe(
            filtered_result,
            use_container_width=True,
            height=450
        )

        csv = filtered_result.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Prediction Result",
            data=csv,
            file_name="prediction_result.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.markdown("---")
        st.subheader("📊 Fraud Distribution")

        chart_data = pd.DataFrame(
    {
        "Transaction Type": ["Normal", "Fraud"],
        "Count": [normal_count, fraud_count]
    }
)

        fig = px.pie(
        chart_data,
        values="Count",
        names="Transaction Type",
        title="Normal vs Fraud Transactions",
        hole=0.4
)

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader("📈 Transaction Summary")

        bar_data = pd.DataFrame(
    {
        "Transaction Type": ["Normal", "Fraud"],
        "Count": [normal_count, fraud_count]
    }
)

        bar_fig = px.bar(
        bar_data,
        x="Transaction Type",
        y="Count",
        text="Count",
        title="Normal vs Fraud Transactions"
)

        bar_fig.update_traces(textposition="outside")

        st.plotly_chart(bar_fig, use_container_width=True)