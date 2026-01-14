import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="About Us | Croply Project", layout="wide")

# 2. Professional Software Styling (Clean & Modern)
def apply_pro_about_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    .stApp {
        background-color: #FFFFFF;
        color: #1A202C;
        font-family: 'Inter', sans-serif;
    }

    /* Hero Section */
    .hero-container {
        padding: 60px 0;
        text-align: center;
        background: #F0FFDF;
        border-bottom: 1px solid #EDF2F7;
        margin-bottom: 40px;
    }

    /* Info Cards */
    .value-card {
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        background: #FFFFFF;
        height: 100%;
        transition: 0.3s;
    }
    
    .value-card:hover {
        border-color: #2F855A;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .value-icon {
        color: #2F855A;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 15px;
    }

    .value-title {
        font-weight: 700;
        font-size: 1.2rem;
        color: #2D3748;
        margin-bottom: 10px;
    }

    /* Simple Tech Badges */
    .tech-pill {
        display: inline-block;
        padding: 5px 15px;
        background: #F0FFF4;
        color: #2F855A;
        border: 1px solid #C6F6D5;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 5px;
    }

    /* Team Section (High Contrast) */
    .team-section {
        background: #1A365D;
        color: white;
        padding: 60px;
        border-radius: 24px;
        margin-top: 60px;
    }

    .block-container {
        padding-top: 0rem !important;
        max-width: 1100px;
    }
    </style>
    """, unsafe_allow_html=True)

apply_pro_about_styles()

# --- HERO SECTION (Simple & Direct) ---
st.markdown("""
    <div class="hero-container">
        <h1 style="color: #22543D; font-size: 3rem; font-weight: 800; margin-bottom: 10px;">Croply</h1>
        <p style="color: #4A5568; font-size: 1.2rem; max-width: 700px; margin: 0 auto;">
            A simple tool we built to help Indian farmers manage irrigation using real data.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- THE PROBLEM & SOLUTION ---
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("### 🎯 Why we built this")
    st.write("""
    We noticed that most farmers in our area water their fields based on habit or guesswork. 
    This leads to wasted water and sometimes damages the crops. 
    
    Our project, **Croply**, is a solution that takes scientific details like soil nutrients 
    and weather and turns them into a simple instruction: *How much water does the crop need today?*
    """)
    
    st.markdown("#### Tools we used")
    st.markdown("""
    <span class="tech-pill">Python</span>
    <span class="tech-pill">Streamlit UI</span>
    <span class="tech-pill">Agricultural Data</span>
    <span class="tech-pill">Conditional Logic</span>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### ⚙️ How it works")
    st.write("""
    We designed a logic engine that checks three main things before giving advice:
    """)
    st.info("**1. Environment:** Current temperature and humidity from weather data.")
    st.info("**2. Soil Info:** The N-P-K levels and the type of soil (Sandy, Clay, etc.).")
    st.info("**3. Crop Type:** Each crop has different needs at different growth stages.")

# --- SYSTEM FLOW DIAGRAM ---
st.write("---")
st.markdown("<h3 style='text-align:center;'>Our System Architecture</h3>", unsafe_allow_html=True)

st.write("")

# --- THE VALUES SECTION ---
v1, v2, v3 = st.columns(3)

def value_box(col, icon, title, text):
    with col:
        st.markdown(f"""
            <div class="value-card">
                <div class="value-icon">{icon}</div>
                <div class="value-title">{title}</div>
                <div style="color: #718096; font-size: 0.95rem;">{text}</div>
            </div>
        """, unsafe_allow_html=True)

value_box(v1, "📈", "Better Yield", "By giving the exact amount of water needed, the plant stays healthy and grows better.")
value_box(v2, "💧", "Saving Water", "Farmers can save a lot of water by not over-irrigating soil that is already moist.")
value_box(v3, "✅", "Easy to Use", "We kept the UI very simple so that any farmer with a smartphone can use it easily.")

# --- THE TEAM SECTION ---
st.markdown(f"""
    <div class="team-section">
        <div style="text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; opacity: 0.8;">The Developers</div>
        <h2 style="margin-top:10px; font-size: 2.5rem;">Shreya & Siddhi</h2>
        <p style="font-size: 1.1rem; opacity: 0.9; line-height: 1.8; max-width: 800px;">
            We built this project to show how simple technology can solve big problems in Indian farming. 
            By combining our coding skills with agricultural research, we wanted to create something 
            practical that helps the 'Annadatas' of our country.
        </p>
        <div style="margin-top:30px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 20px;">
            <p style="font-size: 0.9rem;">Built with care for a better agricultural future.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align:center; padding: 40px; color: #A0AEC0; font-size: 0.8rem;">
        Croply  | Version 1.0.0 | © 2025
    </div>
""", unsafe_allow_html=True)