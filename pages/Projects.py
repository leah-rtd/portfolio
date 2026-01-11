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




st.title("📂 Projects")

for project in projects:
    st.subheader(project["title"])
    cols = st.columns([1, 2])

    with cols[0]:
        st.markdown(f"**🛠️ Tech Stack:**")
        st.markdown(project["tech_stack"])

        st.markdown(f"**💡 Skills Learned:**")
        for skill in project["skills_learned"]:
            st.markdown(f"- {skill}")

        st.markdown(f"""
        <a href="{project['source_code']}" target="_blank">
            <button style="
                background-color: #262730;
                color: white;
                border: 1px solid #4CAF50;
                padding: 8px 16px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
            ">🔗 See Source Code</button>
        </a>
        """, unsafe_allow_html=True)

    with cols[1]:
        st.markdown(f"""
        <a href="{project['project_link']}" target="_blank">
            <img src="{project['image']}" alt="{project['title']}" style="width:100%; border-radius: 8px;">
        </a>
        """, unsafe_allow_html=True)

    st.markdown("---")
