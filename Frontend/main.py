import streamlit as st
from PIL import Image
import tensorflow as tf
from keras.models import load_model
import numpy as np
import pandas as pd
import time
import cv2

st.set_page_config(
    page_title="Neural Network Analysis of Kidney Stone",
    page_icon="🏥"
)

st.sidebar.header("Project Programmer")
profile = Image.open(r"C:\Users\SHASHANK K\Downloads\20240101_131952.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.header("Neural Network Analysis of Kidney Stone")
st.warning("warning: Neural Network or AI results purely depends on the way it is trained. **Remember AI also does mistakes!**")
st.info("Note: Please input C.T.Scan Images like below format")

##########################__Image Grid__################################################################################
# Load the images using PIL
img1 = Image.open(r"C:\Users\SHASHANK K\PycharmProjects\Kidney Stone\Image Formats\pred(1).jpg")
img2 = Image.open(r"C:\Users\SHASHANK K\PycharmProjects\Kidney Stone\Image Formats\pred(55).jpg")
img3 = Image.open(r"C:\Users\SHASHANK K\PycharmProjects\Kidney Stone\Image Formats\pred(61).jpg")

col1, col2, col3 = st.columns(3) #create 3 columns

# Display images in each column
with col1:
    st.image(img1, caption="Image Format 1", use_column_width=True)

with col2:
    st.image(img2, caption="Image Format 2", use_column_width=True)

with col3:
    st.image(img3, caption="Image Format 3", use_column_width=True)
########################################################################################################################
try:
    st.header("Input the Image below:")
    photo = st.file_uploader("Upload C.T.Scanned Image of Kidney", type=['png', 'jpeg', 'jpg'])
    st.image(photo)

    if photo is not None:
        if st.button('Predict'):
            model = load_model('kidney_stone_CNN2.h5')
            imageinput = Image.open(photo)
            resize = tf.image.resize(imageinput, (256, 256))
            image_input_array = np.array(imageinput)

            pred = model.predict(np.expand_dims(resize / 255, axis=0)).round(2)

            # Spinner/loader code
            with st.spinner("Please wait for result"):
                time.sleep(3)

            st.write("Result is: ")

            # Perform dilation on the image
            kernel = np.ones((5, 5), np.uint8)
            dilated_image = cv2.dilate(image_input_array, kernel, iterations=1)

            # image thresholding
            ret, thresh = cv2.threshold(dilated_image, 200, 255, cv2.THRESH_BINARY_INV)

            # Edge Detection
            edges = cv2.Canny(thresh, 549, 255)

            st.image(thresh, caption="processed Image", channels="BGR", width=400)
            st.image(edges, caption="processed Image", width=400)

            if pred[0] >= 0.5:
                st.header("**the input image consists Kidney Stone**")
            else:
                st.header("**the input image does not contain Kidney Stone**")

    else:
        st.write("Please upload an image.")
except AttributeError as e:
    pass
