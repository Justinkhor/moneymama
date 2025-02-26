import streamlit as st


def show_step1():
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
    with col_content:
        st.title("Hello! Are you looking to achieve a target of RM100k in savings?")
        st.header("Let's get started with your name! ")
        name = st.text_input("👤 Name", st.session_state.form_data.get("name", ""))

        if st.button("Next ➡️"):
            if name:
                st.session_state.form_data["name"] = name
                st.session_state.step += 1
                st.rerun()
            else:
                st.warning("Please fill in all fields.")

        if st.button("Skip to Dashboard (Demo)"):
            if name:
                st.session_state.form_data["name"] = name
                st.session_state.dashboard_ready = True
                st.rerun()
            else:
                st.warning("Please fill in all fields.")
