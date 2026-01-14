import streamlit as st
import os
import joblib
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Croply | Welcome", layout="wide", initial_sidebar_state="collapsed")

# =====================================
# 🛠️ BACKEND LINK (The "Brain")
# =====================================
@st.cache_resource # Added cache so it doesn't reload every time you click
def load_models():
    try:
        model = joblib.load('random_forest_irrigation_model.pkl')
        # ... (other encoders)
        return model
    except:
        return None

model = load_models()

# =====================================
# 🎨 UI CODE (Cinematic Style)
# =====================================
def apply_welcome_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@900&family=Inter:wght@300;700&display=swap');

    /* Custom Navbar for this cinematic page */
    .custom-nav {
        display: flex;
        justify-content: flex-end;
        padding: 20px 50px;
        gap: 30px;
        position: absolute;
        top: 0;
        right: 0;
        width: 100%;
        z-index: 1000;
    }
    .custom-nav a {
        color: #81C784;
        text-decoration: none;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        transition: 0.3s;
    }
    .custom-nav a:hover { color: #FFFFFF; }

    /* Deep Cinematic Background */
    .stApp {
        background: linear-gradient(135deg, #041407 0%, #0a2e12 100%);
        overflow: hidden;
    }

    /* 🌿 Thematic Organic Particles */
    @keyframes leafFloat {
        0% { transform: translateY(0) rotate(0deg); opacity: 0; }
        20% { opacity: 0.4; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }

    .leaf-particle {
        position: absolute;
        bottom: -20px;
        background: rgba(76, 175, 80, 0.4);
        border-radius: 50% 0; 
        pointer-events: none;
        animation: leafFloat linear infinite;
    }

    /* ✨ BOLD ATTRACTIVE TITLE DESIGN */
    @keyframes textGlow {
        0% { text-shadow: 0 0 10px rgba(76, 175, 80, 0.2); transform: scale(1); }
        50% { text-shadow: 0 0 30px rgba(76, 175, 80, 0.6); transform: scale(1.02); }
        100% { text-shadow: 0 0 10px rgba(76, 175, 80, 0.2); transform: scale(1); }
    }

    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 85vh;
        text-align: center;
    }

    .main-title {
        font-family: 'Lexend', sans-serif;
        font-weight: 900;
        font-size: 8rem;
        margin: 0;
        background: linear-gradient(to bottom, #FFFFFF 60%, #A5D6A7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textGlow 4s ease-in-out infinite;
        letter-spacing: -4px;
        line-height: 1;
    }

    .sub-title {
        font-family: 'Inter', sans-serif;
        color: #81C784;
        font-size: 1.4rem;
        font-weight: 700;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-top: 10px;
        opacity: 0.9;
    }

    /* 🚀 Minimalist Professional Button */
    .stButton > button {
        background: transparent !important;
        color: #FFFFFF !important;
        border: 2px solid #4CAF50 !important;
        padding: 12px 60px !important;
        border-radius: 5px !important;
        font-size: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        letter-spacing: 2px !important;
        transition: all 0.4s ease !important;
        margin-top: 40px !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        background: #4CAF50 !important;
        box-shadow: 0 0 30px rgba(76, 175, 80, 0.5) !important;
        color: white !important;
    }

    /* Remove Streamlit Branding */
    [data-testid="stHeader"], footer, #MainMenu {display:none;}
    </style>

    <div class="custom-nav">
        <a href="/" target="_self">Home</a>
        <a href="/about" target="_self">About Us</a>
    </div>

    <div class="leaf-particle" style="left:15%; width:12px; height:12px; animation-duration:15s;"></div>
    <div class="leaf-particle" style="left:35%; width:18px; height:18px; animation-duration:22s; animation-delay:2s;"></div>
    <div class="leaf-particle" style="left:85%; width:14px; height:14px; animation-duration:25s; animation-delay:1s;"></div>

    <div class="hero-container">
        <h1 class="main-title">CROPLY</h1>
        <div class="sub-title">Smart Irrigation Advisor</div>
    </div>
    """, unsafe_allow_html=True)

apply_welcome_styles()

# 3. Interactive Entry
c1, col_btn, c3 = st.columns([1, 1, 1])
with col_btn:
    if st.button("Get Started"):
        st.toast("Establishing Data Connection...", icon="🌱")
        # Ensure your Input page is in pages/1_Input_Page.py
        st.switch_page("pages/1_Input_Page.py")