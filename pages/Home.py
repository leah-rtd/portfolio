import streamlit as st
import requests
from streamlit_timeline import timeline
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components


import openai

from constant import *
from PIL import Image


from utils import return_all_lotties as _return_all_lotties, create_slideshow as _create_slideshow, ask_bot as _ask_bot



# -----------------  page config  ----------------- #

st.set_page_config(page_title='Leah Rothschild' ,layout="wide",page_icon='👧🏻',
                   initial_sidebar_state = "expanded")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style/style.css")

# -----------------  sidebar  ----------------- #
openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
openai.api_key = (openai_api_key)
st.sidebar.markdown('<hr>Click on the image to view my <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20px" style="vertical-align:middle;">', unsafe_allow_html = True)
st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)



# -----------------  chatbot  ----------------- #
# get the user's input by calling the get_text function
def get_text():
    input_text = st.text_area("After providing OpenAI API Key on the sidebar, you can send your questions and hit Ctrl + Enter to know more about me.", key="input")
    return input_text

def ask_bot(user_input):
    return _ask_bot(user_input)

with st.container():
    st.markdown("Ask my AI agent Buddy some questions about me !")
    user_input = get_text()

    if user_input:
    #   text = st.text_area('Enter your questions')
        if not openai_api_key.startswith('sk-'):
            st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
        if openai_api_key.startswith('sk-'):
            st.info(ask_bot(user_input))


# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:60px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:17px;">{content2}</span></h1>',
                unsafe_allow_html=True)

with st.container():

    full_name = info['Full_Name']

    gradient("#DED9FA","#7677C4",'e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])




# ----------------- skillset ----------------- #
@st.cache_resource
def return_all_lotties():
    return _return_all_lotties()
lotties = return_all_lotties()
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(lotties[0], height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(lotties[1], height=70,width=70, key="tensorflow", speed=4)
    with col3:
        st_lottie(lotties[2],height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(lotties[3],height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(lotties[4],height=70,width=70, key="github", speed=2.5)
    with col2:
        st_lottie(lotties[5],height=70,width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(lotties[6],height=70,width=70, key="gcp", speed=2.5)
    with col4:
        st_lottie(lotties[7],height=70,width=70, key="js", speed=1)


# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('extra_material/timeline.json', "r") as f:
        data = f.read()
    # for number of students as of 29/07/2025
    # render timeline
    timeline(data, height=600)

# -----------------  notebooks  -----------------  #
@st.cache_resource
def create_slideshow(notebooks, unique_id):
    return _create_slideshow(notebooks, unique_id)


# Layout: Two Columns
with st.container():
    st.markdown("""""")
    st.subheader('👩‍🏫 Teaching Materials')
    col1, col2 = st.columns(2)

    with col1:
        components.html(create_slideshow(notebooks_en, "GB"), height=410)
        st.markdown("""""")


    with col2:
        components.html(create_slideshow(notebooks_fr, "FR"), height=410)
        st.markdown("""""")






# -----------------  contact  ----------------- #
with st.container():
    st.subheader("📨 Contact Me")
    contact_form = f"""
        <form action="https://formsubmit.co/430d11100db23f61bdfebe1e4ea6e020" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    st.markdown(contact_form, unsafe_allow_html=True)
