import streamlit as st
from PIL import Image

st.header("About Us")

st.sidebar.header("Project Programmer")
profile = Image.open(r"C:\Users\SHASHANK K\Downloads\20240101_131952.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.write("""
 **Neural Network Analysis of Kidney Stone** is a WebApp that Detects the presence of Kidney Stone using Neural Networks
 The Type of Neural Network used is Convolutional Neural Network (CNN).
 
 Please do read note before uploading C.T.Scan images for detection 

""")
