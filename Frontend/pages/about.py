import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Neural Network Analysis of Kidney Stone",
    page_icon="🏥"
)
# Set the background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image URL or local path
set_background("https://www.itl.cat/pngfile/big/98-982851_a-harsh-but-beautiful-winter-white-sky-snow.jpg")

st.header("About Us")

st.sidebar.header("Project Programmer")
profile = Image.open(r"C:\Users\SHASHANK K\PycharmProjects\Project Files\Kidney Stone Detection\Shashank K.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.write("""
 **Neural Network Analysis of Kidney Stone** is a WebApp that Detects the presence of Kidney Stone using Neural Networks
 The Type of Neural Network used is Convolutional Neural Network (CNN).

 Please do read note before uploading C.T.Scan images for detection 

""")

