import streamlit as st


def show_step2():
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
        st.title(f"Hi {st.session_state.form_data.get("name", "")}! Let's get to know you better!")
        st.header("How old are you?")

        age = st.text_input("Age", st.session_state.form_data.get("age", ""))

        col1, col2 = st.columns(2)
        if col1.button("⬅️ Back"):
            st.session_state.step -= 1
            st.rerun()

        if col2.button("Next ➡️"):
            if age:
                st.session_state.form_data["age"] = age
                st.session_state.step += 1
                st.rerun()
            else:
                st.warning("Please fill in all fields.")
