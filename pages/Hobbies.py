import streamlit as st
from constant import *
from utils import load_images as _load_images

# -----------------  style  ----------------- #

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
local_css("style/style.css")

# -----------------  sidebar  ----------------- #


st.sidebar.markdown('<hr>Click on the image to view my <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20px" style="vertical-align:middle;">', unsafe_allow_html = True)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)


# -----------------  image display  ----------------- #
@st.cache_resource
def load_images():
    return _load_images()

st.title("⛷️ Hobbies")

col1, col2, col3 = st.columns(3)

imgs = load_images()
with col1:
    st.image(imgs[0], caption = "Skiing ⛷️")

with col2:
    st.image(imgs[1], caption="Crocheting 🧶")

with col3:
    st.image(imgs[2], caption = "Hiking 🚶‍♀️")
