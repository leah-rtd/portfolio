import streamlit as st
from pathlib import Path

st.set_page_config(page_title='Leah Rothschild' ,layout="wide",page_icon='👧🏻',
                   initial_sidebar_state = "expanded")

home_page = st.Page(Path("pages/Home.py"), title = "Home", icon = "🏠")
# resume_page = st.Page(Path("pages/Resume.py"), title = "Resume", icon = "💼")
hobby_page = st.Page(Path("pages/Hobbies.py"), title = "Hobbies", icon = "⛷️")
teaching_content_page = st.Page(Path("pages/Teaching_Materials.py"), title = "Teaching Materials", icon = "👩‍🏫")

pg = st.navigation([home_page,
                    # resume_page,
                    teaching_content_page,
                    hobby_page])

pg.run()
