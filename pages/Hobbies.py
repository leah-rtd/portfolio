import streamlit as st
from constant import *
from utils import load_images as _load_images


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

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
