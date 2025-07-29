import streamlit as st
from PIL import Image, ImageOps
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

@st.cache_resource
def load_images():
    target_size = (300, 300)
    img_1 = ImageOps.fit(Image.open("images/skiing_2.jpg"), target_size)
    img_2 = ImageOps.fit(ImageOps.exif_transpose(Image.open("images/crochet.jpeg")), target_size)
    img_3 = ImageOps.fit(Image.open("images/hiking.jpeg"), target_size)
    return img_1, img_2, img_3

st.title("🫶 Hobbies")

col1, col2, col3 = st.columns(3)

imgs = load_images()
with col1:
    st.image(imgs[0], caption = "Skiing ⛷️")

with col2:
    st.image(imgs[1], caption="Crocheting 🧶")

with col3:
    st.image(imgs[2], caption = "Hiking 🚶‍♀️")
