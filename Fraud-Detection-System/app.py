
import streamlit as st
from pathlib import Path

from modules import home
from modules import fraud_detection
from modules import analytics
from modules import about
from modules import login
from modules import history


# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Logo path
LOGO_PATH = BASE_DIR / "modules" / "assets" / "logo.png"


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


# Sidebar logo
col1, col2, col3 = st.sidebar.columns([1, 2, 1])

with col2:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=65)
    else:
        st.sidebar.warning("Logo file not found")


st.sidebar.markdown(
    "<h2 style='text-align:center;'>🛡 AI Fraud Detection</h2>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<p style='text-align:center;color:gray;'>Industry-Based ML Project</p>",
    unsafe_allow_html=True
)

st.sidebar.markdown("---")


# Logout
if st.sidebar.button("🚪 Logout", use_container_width=True):
    st.session_state["logged_in"] = False
    st.rerun()

st.sidebar.markdown("---")


# Navigation menu
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


# Page routing
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
