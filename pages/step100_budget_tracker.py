import streamlit as st
import pandas as pd

def show_step100():
    # Ensure session state form_data exists
    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    # Custom CSS to center the form
    st.markdown(
        """
        <style>
            .stApp { display: flex; justify-content: center; align-items: center; height: 100vh; }
            .centered-container { width: 100%; max-width: 500px; padding: 30px; 
                                  background: #f9f9f9; border-radius: 10px; 
                                  box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
            .centered-buttons { display: flex; justify-content: space-between; margin-top: 20px; }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # Centering container using columns
    col_space1, col_content, col_space2 = st.columns([1, 2, 1])

    monthly_salary = int(st.session_state.form_data.get('salary', '3000'))
    investment_percentage = int(st.session_state.form_data.get('investment_plan', '30'))
    savings_goal = int(st.session_state.form_data.get('savings_goal', '300'))

    # Generate financial data
    data = {
        "Date": pd.date_range(start="2024-01-01", periods=12, freq='ME'),
        "Income": [monthly_salary] * 12,
        "Spending": [round(monthly_salary * 0.6, 2)] * 12,
        "Investments": [round(monthly_salary * (investment_percentage / 100), 2)] * 12,
        "Savings": [round(monthly_salary * 0.2, 2)] * 12,
    }
    df = pd.DataFrame(data)
    df["Balance"] = df["Income"].cumsum() - df["Spending"].cumsum() - df["Investments"].cumsum()


    with col_content:
        st.title("Budget Tracker")
        st.dataframe(df, height=250, use_container_width=True)

        if st.button("Back To Dashboard ➡️"):
            st.session_state.dashboard_ready = True
            st.rerun()

