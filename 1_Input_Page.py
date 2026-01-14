import streamlit as st
import base64
import os
import joblib  # <--- Added to link Backend

# 1. Page Configuration
st.set_page_config(page_title="Croply | Farm Input", layout="wide")

# =====================================
# 🛠️ BACKEND LINKING (NEW)
# =====================================
# We load the encoders to make sure the UI dropdowns match the Model
try:
    crop_enc = joblib.load('crop_encoder.pkl')
    soil_enc = joblib.load('soil_encoder.pkl')
    fert_enc = joblib.load('fert_encoder.pkl')
    
    # These get the actual categories your friend used in the model
    soil_options = soil_enc.classes_
    crop_options = crop_enc.classes_
    fert_options = fert_enc.classes_
except:
    # Fallback if files are missing during testing
    soil_options = ["Clay", "Sandy", "Loamy", "Black", "Red"]
    crop_options = ["Wheat", "Rice", "Maize", "Cotton", "Sugarcane"]
    fert_options = ["Urea", "DAP", "MOP", "NPK 14-35-14", "None"]

# --- PATH CONFIGURATION ---
IMAGE_FOLDER = r"C:\TESEM5\internship\CROPLY\finalcode"
img_path = os.path.join(IMAGE_FOLDER, "input_page_image.jpg")

# 2. File Loaders
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    return None

def load_external_files():
    if os.path.exists("style.css"):
        with open("style.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # if os.path.exists("navbar.html"):
    #     with open("navbar.html") as f:
    #         st.markdown(f.read(), unsafe_allow_html=True)

# Run Loaders
load_external_files()
img_b64 = get_base64(img_path)

# 4. Main Page Layout
st.title("Croply | Smart Irrigation Advisor")
st.write("Fill in the details below to analyze your soil and environmental needs.")
st.divider()

col_img, col_form = st.columns([1, 1.2], gap="large")

with col_img:
    if img_b64:
        st.markdown(f'<img src="data:image/jpg;base64,{img_b64}" class="animated-farm-image">', unsafe_allow_html=True)
    else:
        st.error(f"❌ Image not found")

with col_form:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        temp = st.number_input("Temperature (°C)", value=25.0)
        humidity = st.number_input("Humidity (%)", value=50)
        moisture = st.number_input("Soil Moisture (%)", value=30)
        nitrogen = st.number_input("Nitrogen (N)", value=60)
        location = st.text_input("📍 Farm Location", placeholder="e.g. Pune, Maharashtra")
    with c2:
        phosphorus = st.number_input("Phosphorus (P)", value=45)
        potassium = st.number_input("Potassium (K)", value=40)
        
        # LINKED TO BACKEND: Using encoder classes instead of manual lists
        soil_type = st.selectbox("Soil Type", soil_options)
        crop_type = st.selectbox("Crop Type", crop_options)
        fert_name = st.selectbox("Fertilizer Name", fert_options)
        
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("###") 
    
    btn_col_back, btn_col_next = st.columns([1, 1])
    with btn_col_back:
        if st.button("BACK TO HOME"):
            st.switch_page("Home.py")

    with btn_col_next:
        if st.button("📊 GENERATE RECOMMENDATION"):
            # SAVING TO SESSION STATE: This passes the data to the next page
            st.session_state.farm_inputs = {
                "Temperature": temp, 
                "Humidity": humidity, 
                "Moisture": moisture,
                "Soil Type": soil_type, 
                "Crop Type": crop_type, 
                "Nitrogen": nitrogen,
                "Potassium": potassium, 
                "Phosphorous": phosphorus,
                "Fertilizer Name": fert_name, 
                "Location": location
            }
            st.switch_page("pages/2_Recommendation.py")