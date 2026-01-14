import streamlit as st
import os
from datetime import datetime


# ============================================
# 🌿 Page Configuration
# ============================================
st.set_page_config(page_title="CropMaster | Light Mode", layout="wide")

# ============================================
# 🎨 Light Game-UI CSS
# ============================================
def apply_light_game_ui():
    st.markdown("""
    <style>
    /* Force high visibility for all text */
    .stApp {
        background-color: #F0F4F2;
        color: #2C3E50 !important;
    }
    
    /* Ensure all Markdown and generic text is dark */
    .stMarkdown, p, span, label {
        color: #2C3E50 !important;
    }

    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Quicksand:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    /* Game-Style Header (Light) */
    .game-header {
        background: white;
        padding: 15px 30px;
        border-radius: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.05);
        border-bottom: 4px solid #81C784;
    }

    /* Card Styling */
    .stat-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        border: 1px solid #E8F5E9;
        text-align: center;
        transition: transform 0.2s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        border-color: #81C784;
    }

    .label-tag {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 0.7rem !important;
        font-weight: 700 !important;
        color: #757575 !important; /* Slightly darker for visibility */
        text-transform: uppercase;
    }

    .value-text {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        color: #2E7D32 !important;
    }

    /* Timeline Styling */
    .timeline-bar {
        background: #E0E0E0;
        height: 12px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .timeline-progress {
        background: linear-gradient(90deg, #66BB6A, #AED581);
        height: 100%;
        border-radius: 10px;
        width: 65%; /* Simulated progress */
    }

    /* Mission Box Text Fix */
    .mission-box {
        background: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        color: #1B5E20 !important;
    }

    /* Selectbox and Radio Label Fix */
    .stSelectbox label, .stRadio label {
        color: #2C3E50 !important;
        font-weight: bold !important;
    }

    /* Print Button Simulation */
    .stButton>button {
        border-radius: 10px;
        background-color: #FFFFFF;
        color: #2E7D32 !important;
        border: 2px solid #2E7D32;
    }
    </style>
    """, unsafe_allow_html=True)

apply_light_game_ui()

# ============================================
# ⚙️ Data Engine
# ============================================
cal = {
    "Paddy": {"Sowing": "June–July", "Irrigation": "Standing Water", "Fertilizer": "N, P & K Splits", "Harvest": "Oct–Nov", "Temp": "22-32°C", "Water": "High", "Soil": "Clayey/Loomy", "Icon": "🌾"},
    "Sugarcane": {"Sowing": "Jan–March", "Irrigation": "7–10 days", "Fertilizer": "Monthly NPK", "Harvest": "12–16 Mon", "Temp": "20-30°C", "Water": "Extreme", "Soil": "Deep Rich", "Icon": "🎋"},
    "Cotton": {"Sowing": "June–July", "Irrigation": "15 days", "Fertilizer": "NPK + Micro", "Harvest": "Nov–Jan", "Temp": "21-35°C", "Water": "Medium", "Soil": "Black Soil", "Icon": "☁️"},
    "Maize": {"Sowing": "June / Jan", "Irrigation": "Flowering", "Fertilizer": "High Nitrogen", "Harvest": "Sept / April", "Temp": "18-27°C", "Water": "Medium", "Soil": "Well-drained", "Icon": "🌽"},
    "Wheat": {"Sowing": "Nov–Dec", "Irrigation": "Medium", "Fertilizer": "NPK 3 Splits", "Harvest": "March–April", "Temp": "10-25°C", "Water": "Medium", "Soil": "Loamy", "Icon": "🍞"},
    "Millets": {"Sowing": "June–July", "Irrigation": "Low", "Fertilizer": "Organic", "Harvest": "Sept–Oct", "Temp": "25-35°C", "Water": "Low", "Soil": "Sandy/Poor", "Icon": "🥣"},
}

# ============================================
# 🕹️ User Interface
# ============================================

# Header
st.markdown(f"""
<div class="game-header">
    <div style="font-size: 1.4rem; font-weight: 700; color: #2E7D32;">🌱 CROP<span style="color: #81C784;">MASTER</span></div>
    <div style="font-weight: bold; background: #F1F8E9; padding: 5px 15px; border-radius: 10px; color: #388E3C;">Level: Master Farmer</div>
</div>
""", unsafe_allow_html=True)

# Controls
c1, c2, c3 = st.columns([2, 1, 1])
with c1:
    crop = st.selectbox("🎯 SELECT YOUR CROP", list(cal.keys()))
with c2:
    lang = st.radio("LANGUAGE", ["English", "मराठी"], horizontal=True)
with c3:
    st.button("🖨️ PRINT CALENDAR")

def tr(en, mr): return mr if lang=="मराठी" else en
data = cal[crop]

# --- VITAL STATS GRID ---
st.markdown(f"### {data['Icon']} {tr('Crop Profile:', 'पिकाची माहिती:')} {crop}")
v1, v2, v3, v4 = st.columns(4)

def draw_stat(col, label, value, icon):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size: 1.5rem; margin-bottom: 5px;">{icon}</div>
            <div class="label-tag">{label}</div>
            <div class="value-text">{value}</div>
        </div>
        """, unsafe_allow_html=True)

draw_stat(v1, tr("Ideal Temp", "आदर्श तापमान"), data['Temp'], "🌡️")
draw_stat(v2, tr("Water Need", "पाण्याची गरज"), data['Water'], "💧")
draw_stat(v3, tr("Soil Type", "मातीचा प्रकार"), data['Soil'], "🏜️")
draw_stat(v4, tr("Yield Potential", "उत्पादन क्षमता"), "High", "📈")

# --- CALENDAR TIMELINE ---
st.write("")
st.markdown(f"**{tr('SEASONAL TIMELINE', 'हंगामी वेळापत्रक')}**")
st.markdown('<div class="timeline-bar"><div class="timeline-progress"></div></div>', unsafe_allow_html=True)

t1, t2, t3, t4 = st.columns(4)

def draw_step(col, stage, date, detail):
    with col:
        st.markdown(f"""
        <div class="stat-card" style="background: #F9FBF9;">
            <div class="label-tag">{stage}</div>
            <div class="value-text" style="font-size: 1rem;">{date}</div>
            <div style="font-size: 0.8rem; color: #757575; margin-top: 5px;">{detail}</div>
        </div>
        """, unsafe_allow_html=True)

draw_step(t1, tr("SOWING", "पेरणी"), data['Sowing'], tr("Planting Phase", "लागवड टप्पा"))
draw_step(t2, tr("GROWTH", "वाढ"), data['Irrigation'], tr("Watering Needs", "पाणी व्यवस्थापन"))
draw_step(t3, tr("NUTRIENTS", "खते"), data['Fertilizer'], tr("Soil Boost", "माती पोषण"))
draw_step(t4, tr("HARVEST", "कापणी"), data['Harvest'], tr("Collection", "कापणी वेळ"))

# --- DAILY MISSION SECTION ---
st.markdown("<div class='mission-box'>", unsafe_allow_html=True)
m1, m2 = st.columns([2, 1])
with m1:
    st.markdown(f"#### ⚡ {tr('Daily Task for', 'आजचे काम:')} {datetime.now().strftime('%B')}")
    st.write(tr(
        f"Check soil moisture levels today. If the top 2 inches are dry, trigger the **{data['Irrigation']}** protocol.",
        f"आज मातीतील ओलावा तपासा. वरचा २ इंच थर कोरडा असल्यास, **{data['Irrigation']}** सुरू करा."
    ))
with m2:
    st.checkbox(tr("Mission Completed", "काम पूर्ण झाले"))
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"<p style='text-align:center; color:#757575; margin-top:40px;'>{tr('Always consult local agriculture experts for precise dates.', 'अचूक तारखांसाठी स्थानिक कृषी तज्ज्ञांचा सल्ला घ्या.')}</p>", unsafe_allow_html=True)