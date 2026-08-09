import streamlit as st

from modules import home
from modules import fraud_detection
from modules import analytics
from modules import about
from modules import login
from modules import history


st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login.show()
    st.stop()

col1, col2, col3 = st.sidebar.columns([1, 2, 1])

with col2:
    st.image("modules/assets/logo.png", width=65)

st.sidebar.markdown(
    "<h2 style='text-align:center;'>🛡 AI Fraud Detection</h2>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<p style='text-align:center;color:gray;'>Industry-Based ML Project</p>",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

if st.sidebar.button("🚪 Logout", use_container_width=True):
    st.session_state["logged_in"] = False
    st.rerun()

st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "📂 Select Page",
    [
        "🏠 Home",
        "🛡 Fraud Detection",
        "📊 Analytics",
        "📜 History",
        "ℹ️ About"
    ]
)

if menu == "🏠 Home":
    home.show()

elif menu == "🛡 Fraud Detection":
    fraud_detection.show()

elif menu == "📊 Analytics":
    analytics.show()

elif menu == "📜 History":
    history.show()

elif menu == "ℹ️ About":
    about.show()