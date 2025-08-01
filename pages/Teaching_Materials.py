import streamlit as st
import streamlit.components.v1 as components
from constant import *



# -----------------  style  ----------------- #

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")

# -----------------  sidebar  ----------------- #

local_css("style/style.css")

st.sidebar.markdown('<hr>Click on the image to view my <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20px" style="vertical-align:middle;">', unsafe_allow_html = True)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)


# -----------------  notebooks display  ----------------- #

st.title("👩‍🏫 Teaching Materials")

st.markdown("""#### All of the Notebooks have been created by me as support material to help students in their Python and Data Science learning.
You can scroll through the notebooks in the right panel or open them in Google Colab to use them yourself.""")
tab_en, tab_fr = st.tabs(['Notebooks 🇬🇧', 'Notebooks 🇫🇷'])
with tab_en:
    for notebook in notebooks_en:
        st.subheader(notebook["title"])
        cols = st.columns([1, 2])

        with cols[0]:
            st.markdown(notebook["description"])

        with cols[1]:
            components.iframe(src=notebook["html_preview"], height = 350, scrolling=True)
            st.markdown(f"""
            <a href="{notebook['colab_link']}" target="_blank">
                <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="height:30px;">
            </a>
            """, unsafe_allow_html=True)

        st.markdown("---")


with tab_fr:
    for notebook in notebooks_fr:
        st.subheader(notebook["title"])
        cols = st.columns([1, 2])

        with cols[0]:
            st.markdown(notebook["description"])

        with cols[1]:
            components.iframe(src=notebook["html_preview"], height = 350, scrolling=True)

            st.markdown(f"""
            <a href="{notebook['colab_link']}" target="_blank">
                <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="height:30px;">
            </a>
            """, unsafe_allow_html=True)

        st.markdown("---")
