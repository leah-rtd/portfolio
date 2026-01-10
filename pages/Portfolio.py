import streamlit as st
from constant import *

# -----------------  style  ----------------- #

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")

# -----------------  sidebar  ----------------- #


st.sidebar.markdown('Click on the image to view my <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20px" style="vertical-align:middle;">', unsafe_allow_html = True)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)




st.title("📂 Portfolio")
