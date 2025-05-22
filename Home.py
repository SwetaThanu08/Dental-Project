import streamlit as st
from PIL import Image, ImageOps

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
        
        st.page_link("pages/Analysis.py", label="➡️ Click here for AI Analysis", use_container_width=True)
