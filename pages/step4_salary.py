import streamlit as st


def show_step4():
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

    # Centering container using columns
    col_space1, col_content, col_space2 = st.columns([1, 2, 1])
    with col_content:
        st.title(f"You want to achieve your target of RM100k in {st.session_state.form_data.get('year', '')} years")
        st.header("What is your monthly salary and average monthly expenses?")

        salary = st.number_input("💰 Monthly Salary ($)", min_value=0, value=st.session_state.form_data.get("salary", 5000))
        expenses = st.number_input("📉 Average Monthly Expenses ($)", min_value=0, value=st.session_state.form_data.get("expenses", 2000))

        col1, col2 = st.columns(2)
        if col1.button("⬅️ Back"):
            st.session_state.step -= 1
            st.rerun()

        if col2.button("Next ➡️"):
            st.session_state.form_data["salary"] = salary
            st.session_state.form_data["expenses"] = expenses
            st.session_state.step += 1
            st.rerun()
