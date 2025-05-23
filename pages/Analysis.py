import streamlit as st
from PIL import Image,ImageOps
import numpy as np
from io import BytesIO
import base64
import os
import traceback
import time
import logging
from test import *

sample_images = {
    "Sample1.1.JPG": "⚠️ Wrong contrast",
    "Sample2.1.JPG": "💡 Lighting uneven",
    "Sample3.1.JPG": "📐 Uneven alignment"
}

if "matched_sample" not in st.session_state:
    st.error("Oops! It looks like you haven’t uploaded an image yet, please add one to continue. Click on Home tab to proceed further!")
    st.stop()

# Simulate AI processing
with st.spinner("🔍🔬 Applying AI insights to your dental image... please hold on"):
    time.sleep(6)



if st.session_state.matched_sample == "Sample1.1.JPG":
    col1, col2 = st.columns(2)
    with col1:
        logo = Image.open("images/Sample1.1.JPG")
        logo = logo.resize((500,500))
        logo = ImageOps.exif_transpose(logo)
        st.image(logo)
        st.write("Initial Image")
    with col2:
        logo2 = Image.open("images/Sample1.2.png")
        logo2 = logo2.resize((500,500))
        logo2 = ImageOps.exif_transpose(logo2)
        st.image(logo2)
        st.write("AI Rectified image")
elif st.session_state.matched_sample == "Sample2.1.JPG":
    col1, col2 = st.columns(2)
    with col1:
        logo = Image.open("images/Sample2.1.JPG")
        logo = logo.resize((500,500))
        logo = ImageOps.exif_transpose(logo)
        st.image(logo)
        st.write("Initial Image")
    with col2:
        logo2 = Image.open("images/Sample2.2.png")
        logo2 = logo2.resize((500,500))
        logo2 = ImageOps.exif_transpose(logo2)
        st.image(logo2)
        st.write("AI Rectified image")
elif st.session_state.matched_sample == "Sample3.1.JPG":
    col1, col2 = st.columns(2)
    with col1:
        logo = Image.open("images/Sample3.1.JPG")
        logo = logo.resize((500,500))
        logo = ImageOps.exif_transpose(logo)
        st.image(logo)
        st.write("Initial Image")
    with col2:
        logo2 = Image.open("images/Sample3.2.jpg")
        logo2 = logo2.resize((500,500))
        logo2 = ImageOps.exif_transpose(logo2)
        st.image(logo2)
        st.write("AI Rectified image")
else:
    st.write("Unable to process request at the moment, please try again later!")