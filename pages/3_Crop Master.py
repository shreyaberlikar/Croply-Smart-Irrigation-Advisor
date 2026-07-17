import streamlit as st
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
    .stApp { background-color: #F0F4F2; color: #2C3E50 !important; }
    .stMarkdown, p, span, label { color: #2C3E50 !important; }
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Quicksand:wght@300;500;700&display=swap');
    html, body, [class*="css"] { font-family: 'Quicksand', sans-serif; }

    /* Game-Style Header */
    .game-header { background: white; padding: 15px 30px; border-radius: 20px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; box-shadow: 0 8px 20px rgba(0,0,0,0.05); border-bottom: 4px solid #81C784; }
    
    /* Card Styling */
    .stat-card { background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); border: 1px solid #E8F5E9; text-align: center; transition: transform 0.2s ease; }
    .stat-card:hover { transform: translateY(-5px); border-color: #81C784; }
    .label-tag { font-family: 'Montserrat', sans-serif !important; font-size: 0.7rem !important; font-weight: 700 !important; color: #757575 !important; text-transform: uppercase; }
    .value-text { font-size: 1.1rem !important; font-weight: 700 !important; color: #2E7D32 !important; }

    /* Timeline */
    .timeline-bar { background: #E0E0E0; height: 12px; border-radius: 10px; margin: 20px 0; }
    .timeline-progress { background: linear-gradient(90deg, #66BB6A, #AED581); height: 100%; border-radius: 10px; width: 65%; }

    /* Mission Box */
    .mission-box { background: #E8F5E9; border-left: 5px solid #4CAF50; padding: 15px; border-radius: 10px; margin-top: 20px; color: #1B5E20 !important; }
    .stSelectbox label, .stRadio label { color: #2C3E50 !important; font-weight: bold !important; }
    .stButton>button { border-radius: 10px; background-color: #FFFFFF; color: #2E7D32 !important; border: 2px solid #2E7D32; }
    </style>
    """, unsafe_allow_html=True)

apply_light_game_ui()

# ============================================
# ⚙️ Upgraded Data Engine (Crop -> Region)
# ============================================
cal = {
    "Paddy": {
        "North India (Kharif)": {"Sowing": "June–July", "Irrigation": "Standing Water", "Fertilizer": "N, P & K Splits", "Harvest": "Oct–Nov", "Temp": "22-32°C", "Water": "High", "Soil": "Clayey/Loamy", "Icon": "🌾"},
        "South/East India (Rabi)": {"Sowing": "Nov–Dec", "Irrigation": "Standing Water", "Fertilizer": "N, P & K Splits", "Harvest": "March–April", "Temp": "22-32°C", "Water": "High", "Soil": "Clayey", "Icon": "🌾"}
    },
    "Sugarcane": {
        "North India (Spring)": {"Sowing": "Feb–March", "Irrigation": "10-15 days", "Fertilizer": "Monthly NPK", "Harvest": "10–12 Mon", "Temp": "20-30°C", "Water": "Extreme", "Soil": "Deep Rich", "Icon": "🎋"},
        "West/South India (Adsali)": {"Sowing": "July–Aug", "Irrigation": "7–10 days", "Fertilizer": "Monthly NPK", "Harvest": "16–18 Mon", "Temp": "20-35°C", "Water": "Extreme", "Soil": "Black Cotton", "Icon": "🎋"}
    },
    "Cotton": {
        "North India": {"Sowing": "April–May", "Irrigation": "20 days", "Fertilizer": "NPK + Micro", "Harvest": "Oct–Nov", "Temp": "21-35°C", "Water": "Medium", "Soil": "Sandy Loam", "Icon": "☁️"},
        "Central/South India": {"Sowing": "June–July", "Irrigation": "15 days", "Fertilizer": "NPK + Micro", "Harvest": "Nov–Jan", "Temp": "21-35°C", "Water": "Medium", "Soil": "Black Cotton", "Icon": "☁️"}
    },
    "Maize": {
        "North/Central India": {"Sowing": "June–July", "Irrigation": "Flowering", "Fertilizer": "High Nitrogen", "Harvest": "Sept–Oct", "Temp": "18-27°C", "Water": "Medium", "Soil": "Well-drained", "Icon": "🌽"},
        "South India (Rabi)": {"Sowing": "Oct–Nov", "Irrigation": "Flowering", "Fertilizer": "High Nitrogen", "Harvest": "Feb–March", "Temp": "18-27°C", "Water": "Medium", "Soil": "Well-drained", "Icon": "🌽"}
    },
    "Wheat": {
        "North India": {"Sowing": "Nov", "Irrigation": "Medium", "Fertilizer": "NPK 3 Splits", "Harvest": "March–April", "Temp": "10-25°C", "Water": "Medium", "Soil": "Clayey/Loamy", "Icon": "🍞"},
        "Central India (Late)": {"Sowing": "Dec", "Irrigation": "Medium", "Fertilizer": "NPK 3 Splits", "Harvest": "April", "Temp": "15-25°C", "Water": "Medium", "Soil": "Heavy Clay", "Icon": "🍞"}
    },
    "Millets": {
        "North India": {"Sowing": "June–July", "Irrigation": "Low", "Fertilizer": "Organic", "Harvest": "Sept–Oct", "Temp": "25-35°C", "Water": "Low", "Soil": "Sandy/Poor", "Icon": "🥣"},
        "South India": {"Sowing": "July–Aug", "Irrigation": "Low", "Fertilizer": "Organic", "Harvest": "Oct–Nov", "Temp": "25-35°C", "Water": "Low", "Soil": "Red/Sandy", "Icon": "🥣"}
    }
}

# ============================================
# 📚 Tooltip Dictionary (Soil Science)
# ============================================
def get_soil_tooltip(soil_type, lang):
    tooltips_en = {
        "Black Cotton": "High clay content, holds water like a sponge. Cracks in summer for natural aeration.",
        "Deep Rich": "Deep fertile soil with high organic matter. Excellent for deep roots.",
        "Clayey": "Sticky when wet, holds water very well for crops like Paddy.",
        "Clayey/Loamy": "Balanced mix of sand, silt, and clay. The gold standard for farming.",
        "Sandy Loam": "Good drainage, warms up quickly in the sun.",
        "Well-drained": "Water doesn't collect here, which prevents root rot.",
        "Heavy Clay": "Dense soil, holds nutrients tightly but needs good tilling.",
        "Sandy/Poor": "Low nutrients, drains quickly. Needs hardy crops like Millets.",
        "Red/Sandy": "Rich in iron, needs frequent watering and organic matter."
    }
    tooltips_mr = {
        "Black Cotton": "जास्त चिकणमाती, स्पंजसारखे पाणी धरून ठेवते. उन्हाळ्यात भेगा पडून नैसर्गिक वायुविजन होते.",
        "Deep Rich": "सेंद्रिय पदार्थांनी समृद्ध असलेली खोल सुपीक माती.",
        "Clayey": "ओली असताना चिकट असते, भातासारख्या पिकांसाठी उत्तम पाणी धरून ठेवते.",
        "Clayey/Loamy": "वाळू, गाळ आणि चिकणमाती यांचे संतुलित मिश्रण. शेतीसाठी सर्वोत्तम.",
        "Sandy Loam": "पाण्याचा चांगला निचरा होतो आणि लवकर गरम होते.",
        "Well-drained": "पाण्याचा उत्तम निचरा होणारी माती, मुळे कुजण्यापासून वाचवते.",
        "Heavy Clay": "दाट माती, पोषक घटक घट्ट धरून ठेवते पण चांगली मशागत लागते.",
        "Sandy/Poor": "कमी पोषक, वेगाने पाणी वाहून जाते. बाजरीसारख्या काटक पिकांसाठी योग्य.",
        "Red/Sandy": "लोहयुक्त, वारंवार पाणी आणि खत देण्याची गरज असते."
    }
    
    if lang == "मराठी":
        return tooltips_mr.get(soil_type, "या मातीचा प्रकार पिकासाठी योग्य आहे.")
    return tooltips_en.get(soil_type, "This soil type is suitable for the crop.")

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
c1, c2, c3 = st.columns([1.5, 1.5, 1.5])
with c1:
    crop = st.selectbox("🎯 SELECT CROP / पीक निवडा", list(cal.keys()), key="crop_select")
with c2:
    available_regions = list(cal[crop].keys())
    region = st.selectbox("🗺️ SELECT REGION / प्रदेश", available_regions, key="region_select")
with c3:
    lang = st.radio("LANGUAGE / भाषा", ["English", "मराठी"], horizontal=True, key="lang_cropmaster")

def tr(en, mr): return mr if lang=="मराठी" else en

# Fetch specific data for the chosen Crop AND Region
data = cal[crop][region]

# --- VITAL STATS GRID ---
st.markdown(f"### {data['Icon']} {tr('Crop Profile:', 'पिकाची माहिती:')} {crop} ({region})")
v1, v2, v3, v4 = st.columns(4)

def draw_stat(col, label, value, icon, tooltip=None):
    # If a tooltip exists, we add a title attribute and change the mouse cursor to 'help'
    tooltip_html = f'title="{tooltip}"' if tooltip else ""
    cursor_style = "cursor: help;" if tooltip else ""
    info_icon = ' <span style="font-size:0.8rem;" title="Hover for info">ℹ️</span>' if tooltip else ''
    
    with col:
        st.markdown(f"""
        <div class="stat-card" {tooltip_html} style="{cursor_style}">
            <div style="font-size: 1.5rem; margin-bottom: 5px;">{icon}</div>
            <div class="label-tag">{label}{info_icon}</div>
            <div class="value-text">{value}</div>
        </div>
        """, unsafe_allow_html=True)

draw_stat(v1, tr("Ideal Temp", "आदर्श तापमान"), data['Temp'], "🌡️")
draw_stat(v2, tr("Water Need", "पाण्याची गरज"), data['Water'], "💧")

# 🔥 Fetch the tooltip and pass it to the Soil stat card
soil_tip = get_soil_tooltip(data['Soil'], lang)
draw_stat(v3, tr("Soil Type", "मातीचा प्रकार"), data['Soil'], "🏜️", tooltip=soil_tip)

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

# --- EXPERT INSIGHTS DICTIONARY ---
# We add this small dictionary just above the UI section
expert_data = {
    "Paddy": {
        "Pest": tr("Stem Borer & Leaf Folder", "खोडकिडा आणि पाने गुंडाळणारी अळी"), 
        "Tip": tr("Maintain 5cm standing water to suppress weeds, but drain completely before applying fertilizer.", "तण कमी करण्यासाठी ५ सेमी पाणी साठवून ठेवा, पण खत देण्यापूर्वी शेत पूर्णपणे कोरडे करा.")
    },
    "Sugarcane": {
        "Pest": tr("Early Shoot Borer & White Grub", "खोडकिडा आणि हुमणी अळी"), 
        "Tip": tr("Perform 'earthing up' (mounding soil around the base) to prevent tall stalks from falling in strong winds.", "वाऱ्यामुळे ऊस पडू नये म्हणून वेळेवर 'भरणी' (बुंध्याला माती लावणे) करा.")
    },
    "Cotton": {
        "Pest": tr("Pink Bollworm & Whitefly", "गुलाबी बोंडअळी आणि पांढरी माशी"), 
        "Tip": tr("Install Pheromone traps early in the season to monitor adult moth activity before they lay eggs.", "अंडी घालण्यापूर्वी पतंगांच्या हालचालींवर लक्ष ठेवण्यासाठी हंगामाच्या सुरुवातीलाच कामगंध सापळे लावा.")
    },
    "Maize": {
        "Pest": tr("Fall Armyworm", "लष्करी अळी"), 
        "Tip": tr("Apply the third split of nitrogen just before the tasseling stage to significantly boost grain weight.", "धान्याचे वजन लक्षणीयरीत्या वाढवण्यासाठी तुरे येण्यापूर्वी नत्राची तिसरी मात्रा द्या.")
    },
    "Wheat": {
        "Pest": tr("Termites & Rust Disease", "वाळवी आणि तांबेरा रोग"), 
        "Tip": tr("The 'Crown Root Initiation' (CRI) stage at 21 days is the most critical time for the first irrigation.", "पेरणीनंतर २१ दिवसांनी येणारी 'मुकुट मुळे फुटण्याची अवस्था' (CRI) पहिल्या पाण्यासाठी सर्वात महत्त्वाची असते.")
    },
    "Millets": {
        "Pest": tr("Shoot Fly & Stem Borer", "खोडमाशी आणि खोडकिडा"), 
        "Tip": tr("Thin out the weak plants 15 days after sowing to reduce competition for soil moisture.", "जमिनीतील ओलाव्यासाठी स्पर्धा कमी करण्यासाठी पेरणीनंतर १५ दिवसांनी विरळणी करा.")
    }
}

# Fetch the insights for the currently selected crop
insight = expert_data.get(crop, expert_data["Paddy"])

# --- NEW EXPERT INSIGHTS SECTION ---
st.markdown("<div class='mission-box' style='border-left: 5px solid #FF9800; background: #FFF3E0;'>", unsafe_allow_html=True)
m1, m2 = st.columns([1, 1])

with m1:
    st.markdown(f"<h4 style='margin:0; color: #E65100;'>🚨 {tr('Pest Radar', 'कीड आणि रोग इशारा')}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #D84315; font-weight: 600;'>{tr('Watch out for:', 'यांच्यापासून सावध राहा:')} {insight['Pest']}</p>", unsafe_allow_html=True)

with m2:
    st.markdown(f"<h4 style='margin:0; color: #1565C0;'>💡 {tr('Master Secret', 'प्रगत शेतकऱ्याची युक्ती')}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0D47A1;'>{insight['Tip']}</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)