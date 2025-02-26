import streamlit as st

st.set_page_config(page_title="MoneyMama", layout="wide")
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)


# Initialize session state variables
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.form_data = {}
    st.session_state.dashboard_ready = False

# Navigation logic
if st.session_state.dashboard_ready:
    from pages.dashboard import show_dashboard
    show_dashboard()
elif st.session_state.step == 1:
    from pages.step1_name import show_step1
    show_step1()
elif st.session_state.step == 2:
    from pages.step2_age import show_step2
    show_step2()
elif st.session_state.step == 3:
    from pages.step3_years import show_step3
    show_step3()
elif st.session_state.step == 4:
    from pages.step4_salary import show_step4
    show_step4()
elif st.session_state.step == 5:
    from pages.step5_financial_goals import show_step5
    show_step5()
elif st.session_state.step == 6:
    from pages.step6_pre_result_signup import show_step6
    show_step6()
elif st.session_state.step == 100:
    from pages.step100_budget_tracker import show_step100
    show_step100()
