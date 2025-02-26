import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard():    
    st.title(f"📊 Welcome to your Financial Dashboard, {st.session_state.form_data.get('name', 'User')}!")
    st.write("Here is your financial overview based on the details you provided.")

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

    # Layout
    col1, col2 = st.columns(2, gap="large")

    # Financial Overview
    with col1:
        st.subheader("🏦 Financial Overview")
        st.metric("💰 Current Balance", f"${df['Balance'].iloc[-1]:,.2f}")
        st.metric("📥 Total Income", f"${df['Income'].sum():,.2f}")
        st.metric("📤 Total Spending", f"${df['Spending'].sum():,.2f}")
        st.metric("📈 Total Investments", f"${df['Investments'].sum():,.2f}")
        st.metric("💾 Total Savings", f"${df['Savings'].sum():,.2f}")

        st.markdown("---")

        # Balance Over Time Chart
        fig = px.line(df, x="Date", y="Balance", title="Balance Over Time", markers=True, line_shape='spline')
        st.plotly_chart(fig, use_container_width=True)

    # Monthly Breakdown
    with col2:
        # # Logout button at the top
        # if st.button("🔄 Logout"):
        #     st.session_state.step = 1
        #     st.session_state.form_data = {}
        #     st.session_state.dashboard_ready = False
        #     st.rerun()

        # st.write("")

        # Savings Goal Progress
        st.subheader("🎯 Savings Goal Progress")
        st.progress(min(df['Savings'].sum() / savings_goal, 1.0))
        st.write(f"Current progress: {min(df['Savings'].sum() / savings_goal * 100, 100):.2f}%")

        st.markdown("---")

        st.subheader("📆 Monthly Breakdown")
        # st.dataframe(df, height=250, use_container_width=True)

        # Spending & Investments Breakdown Pie Chart
        fig_pie = px.pie(df.melt(id_vars=["Date"], value_vars=["Spending", "Investments", "Savings"]), 
                        values="value", names="variable", title="Expense Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)

        if st.button("Budget Tracker"):
            st.session_state.step = 100
            st.session_state.dashboard_ready = False
            st.rerun()

        st.markdown("---")
        
        st.subheader("😊 Financial Personality")
        st.markdown("<div class='big-font'>Low Risk</div>", unsafe_allow_html=True)


    # # Charts Section
    # st.subheader("📊 Financial Insights")

    # # Layout
    # col1, col2 = st.columns(2, gap="large")

    # with col1:
    #     # Balance Over Time Chart
    #     fig = px.line(df, x="Date", y="Balance", title="Balance Over Time", markers=True, line_shape='spline')
    #     st.plotly_chart(fig, use_container_width=True)

    # with col2:
    #     # Spending & Investments Breakdown Pie Chart
    #     fig_pie = px.pie(df.melt(id_vars=["Date"], value_vars=["Spending", "Investments", "Savings"]), 
    #                     values="value", names="variable", title="Expense Distribution")
    #     st.plotly_chart(fig_pie, use_container_width=True)
