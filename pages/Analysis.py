import streamlit as st
from PIL import Image,ImageOps
import numpy as np
from io import BytesIO
import base64
import os
import traceback
import time
import logging




# Increased file size limit
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

# Max dimensions for processing
MAX_IMAGE_SIZE = 2000  # pixels

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Resize image while maintaining aspect ratio
def resize_image(image, max_size):
    width, height = image.size
    if width <= max_size and height <= max_size:
        return image
    
    if width > height:
        new_width = max_size
        new_height = int(height * (max_size / width))
    else:
        new_height = max_size
        new_width = int(width * (max_size / height))
    
    return image.resize((new_width, new_height), Image.LANCZOS)

@st.cache_data
def process_image(image_bytes):
    """Process image with caching to avoid redundant processing"""
    try:
        image = Image.open(BytesIO(image_bytes))
        # Resize large images to prevent memory issues
        resized = resize_image(image, MAX_IMAGE_SIZE)
        # Process the image
        #fixed = remove(resized)
        return image, image
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
        return None, None

def fix_image(upload):
    try:
        start_time = time.time()
        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        
        status_text.text("Loading image...")
        progress_bar.progress(10)
        
        # Read image bytes
        if isinstance(upload, str):
            # Default image path
            if not os.path.exists(upload):
                st.error(f"Default image not found at path: {upload}")
                return
            with open(upload, "rb") as f:
                image_bytes = f.read()
        else:
            # Uploaded file
            image_bytes = upload.getvalue()
        
        status_text.text("Processing image...")
        progress_bar.progress(30)
        
        # Process image (using cache if available)
        image, fixed = process_image(image_bytes)
        if image is None or fixed is None:
            return
        
        progress_bar.progress(80)
        status_text.text("Displaying results...")
        
        # Display images
        col1.write("Original Image :camera:")
        col1.image(image)
        
        col2.write("Fixed Image :wrench:")
        col2.image(fixed)
        
        # Prepare download button
        st.sidebar.markdown("\n")
        st.sidebar.download_button(
            "Download fixed image", 
            convert_image(fixed), 
            "fixed.png", 
            "image/png"
        )
        
        progress_bar.progress(100)
        processing_time = time.time() - start_time
        status_text.text(f"Completed in {processing_time:.2f} seconds")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.sidebar.error("Failed to process image")
        # Log the full error for debugging
        print(f"Error in fix_image: {traceback.format_exc()}")

# UI Layout

col1, col2 = st.columns(2)
with col1:
    logo = Image.open("images/improper.JPG")
    logo = logo.resize((500,500))
    logo = ImageOps.exif_transpose(logo)
    st.image(logo)
    st.write("Initial Image")
with col2:
    logo2 = Image.open("images/proper.JPG")
    logo2 = logo2.resize((500,500))
    logo2 = ImageOps.exif_transpose(logo2)
    st.image(logo2)
    st.write("AI Rectified image")

default_images = ["./improper.JPG", "./proper.JPG"]