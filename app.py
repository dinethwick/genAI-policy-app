import streamlit as st

# --- PAGE SETUP ---
user_guide_page = st.Page (
    page="pages/user_guide.py",
    title="User Guide for this application",
    #icon=":material/account_circle",
)

students_page = st.Page (
    page="pages/students.py",
    title="Policies for students"
)
educators_page = st.Page (
    page="pages/educators.py",
    title="Policies for educators"
)
about_page = st.Page (
    page="pages/about.py",
    title="About this project",
    default=True                                   # this is the home page for now
)

# -- Navigation Setup -- 
pg = st.navigation(pages=[students_page, educators_page, user_guide_page, about_page])
pg.run()