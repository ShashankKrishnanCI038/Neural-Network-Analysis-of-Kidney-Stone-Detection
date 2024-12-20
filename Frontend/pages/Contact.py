import streamlit as st
from PIL import Image

st.header("Get in Touch")

st.sidebar.header("Project Programmer")
profile = Image.open(r"C:\Users\SHASHANK K\Downloads\20240101_131952.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.write("""
 **Neural Network Analysis of Kidney Stone** is a WebApp that is Developed by Shashank K, AIML Engineering graduate from Don Bosco Institute of Technology, Kumbalagodu.

 For Any Queries ragarding trained CNN Model:
    * Please do mail to shashank2002.shashu@gmail.com 
    * Ping me on +91 7829493269

""")