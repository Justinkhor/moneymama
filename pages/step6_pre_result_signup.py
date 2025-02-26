import streamlit as st


def show_step6():
    # Ensure session state form_data exists
    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    # Custom CSS to center the form
    st.markdown("""
        <style>
            .stApp { display: flex; justify-content: center; align-items: center; height: 100vh; }
            .centered-container { width: 100%; max-width: 500px; padding: 30px; 
                                  background: #f9f9f9; border-radius: 10px; 
                                  box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
            .centered-buttons { display: flex; justify-content: space-between; margin-top: 20px; }
        </style>
    """, unsafe_allow_html=True)

    years_to_reach_goal = int(st.session_state.form_data["year"])
    salary = int(st.session_state.form_data["salary"])
    expenses = st.session_state.form_data["expenses"]
    monthly_saving_goal = int(st.session_state.form_data["savings_goal"])
    investment_plan = st.session_state.form_data["investment_plan"]

    principal_monthly = salary
    interest_rate = 0.0001
    if investment_plan == "Conservative":
        interest_rate = 0.03
    if investment_plan == "Balanced":
        interest_rate = 0.05
    if investment_plan == "Aggressive":
        interest_rate = 0.07

    FV = (
        principal_monthly
        * ((1 + interest_rate / 12) ** (12 * years_to_reach_goal) - 1)
        / (interest_rate / 12)
        * (1 + interest_rate / 12)
    )

    roundFV = round(FV)
    FVBalance = 100000 - roundFV

    reached_target = FVBalance < 0

    # Centering container using columns
    col_space1, col_content, col_space2 = st.columns([1, 2, 1])
    with col_content:
        st.title("Forecasted Results")
        st.markdown(
            f"With your current plan, you will get **RM{roundFV}** (estimated) within your target time of {years_to_reach_goal} years"
        )
        if reached_target:
            st.markdown("Congratulations! You will achieve your target of RM100k")
        else: 
            st.markdown(
                f"Unfortunately you will not be able to achieve your target of RM100k, you will be RM{abs(FVBalance)} short. "
            )
        st.markdown("If you would love to learn more about how to **improve your current financial profile and plan for your future.** ")
        st.markdown(
            "We provide this service for **FREE**. All you have to do is **sign up** with us today and achieve your goals with our AI financial advisor!"
        )

        st.markdown("---")
        st.subheader("Create an account today and plan your finances with us!")
        email = st.text_input("Email", st.session_state.form_data.get("email", ""))
        password = st.text_input("Password", st.session_state.form_data.get("password", ""))

        col1, col2 = st.columns(2)
        if col1.button("⬅️ Back"):
            st.session_state.step -= 1
            st.rerun()

        if col2.button("Submit ✅"):
            st.session_state.form_data["email"] = email
            st.session_state.form_data["password"] = password
            st.session_state.dashboard_ready = True
            st.rerun()
