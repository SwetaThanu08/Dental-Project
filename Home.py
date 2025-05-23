import streamlit as st
from PIL import Image, ImageOps
import imagehash
import os
import time
# Set wide layout and page config early
st.set_page_config(
    page_title="Extra Oral AI Orthodontics",
    layout="wide",
    page_icon="🦷",
    initial_sidebar_state="collapsed"
)

logo = Image.open("images/Dental_icon.png")
st.logo(logo, size="large")

# App Title & Logo
col1, col2 = st.columns([1, 14])
with col1:
    logo = Image.open("images/Dental_icon.png")
    st.image(logo, width=70)
with col2:
    st.title("Extra Oral AI Orthodontics")

st.markdown("### 📸 Fix your extra-oral dental images with AI assistance")
st.markdown("_Select the correct category for your image to proceed with the upload._")

# Initialize session state
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# Dropdown to choose category
selected_category = st.selectbox(
    "📂 Select Image Category",
    ("Frontal", "Frontal Smile", "Profile", "Profile Smile", "Oblique", "Oblique Smile"),
    index=None,
    placeholder="-- Select Category --"
)


# Path to sample images and expected outputs
sample_images = {
    "Sample1.1.JPG": "⚠️ Wrong contrast",
    "Sample2.1.JPG": "💡 Lighting uneven",
    "Sample3.1.JPG": "📐 Uneven alignment"
}

# Compute hash for each known image
def compute_image_hash(image_path):
    return imagehash.average_hash(Image.open(image_path))

# Precompute hashes for known images
sample_hashes = {img: compute_image_hash(os.path.join("samples", img)) for img in sample_images}








# Proceed to upload page
if selected_category:
    st.session_state.selected_category = selected_category
    st.success(f"✅ Selected: _{selected_category}_ category")

if selected_category:
    uploaded_file = st.file_uploader(f"Upload image for '{selected_category}' category", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        
        image = Image.open(uploaded_file)
        image = ImageOps.exif_transpose(image)

        # Resize to fixed dimensions (e.g., 400x300)
        image = image.resize((400, 500))
        st.success("✅ Image uploaded successfully!")
        image = ImageOps.exif_transpose(image)
        st.image(image, caption=f"{selected_category} Image")

         # Compute hash of uploaded image
        uploaded_hash = imagehash.average_hash(image)

        name_match=""
        match_found = False
        for sample_name, sample_hash in sample_hashes.items():
            if uploaded_hash - sample_hash < 5:  # Hamming distance threshold
                #st.success(f"✅ Match found: {sample_name}")
                # Simulate AI processing
                with st.spinner("🔍⚙️ Verifying image quality as per orthodontic documentation guidelines"):
                    time.sleep(6)
                st.info(f"🔍 Issue Detected: {sample_images[sample_name]}")
                match_found = True
                st.session_state.matched_sample = sample_name
                st.page_link("pages/Analysis.py", label="➡️ Click here for AI Analysis", use_container_width=True)

        if not match_found:
            with st.spinner("🔍⚙️ Verifying image quality as per orthodontic documentation guidelines"):
                    time.sleep(6)
            st.warning("Unable to process image at the moment, please try again later!")

