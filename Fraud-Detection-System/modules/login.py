import streamlit as st


def show():
    st.title("🔐 Login")
    st.caption("Sign in with credentials or use one-click Reviewer access for demo testing.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([1, 1.4])

    with col1:
        if st.button("Login", type="primary", use_container_width=True):
            if username == "admin" and password == "admin123":
                st.session_state["logged_in"] = True
                st.session_state["user_role"] = "Admin"
                st.success("Login Successful!")
                st.rerun()
            else:
                st.error("Invalid Username or Password")

    with col2:
        if st.button("🚀 Reviewer Quick Login", use_container_width=True):
            st.session_state["logged_in"] = True
            st.session_state["user_role"] = "Reviewer (Demo)"
            st.success("Reviewer Access Granted!")
            st.rerun()

    st.info("**Demo Credentials:** Username: `admin` | Password: `admin123` (or click **Reviewer Quick Login**)")
