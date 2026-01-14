import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Croply | Knowledge Hub Pro", layout="wide")

# 2. Integrated CSS with Visibility Fixes
def apply_hub_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Lexend:wght@400;700&display=swap');

    /* Global Text Visibility Fix */
    .stApp {
        background-color: #F0F4F2;
    }
    
    /* Force dark text for standard Streamlit elements */
    .stApp, p, li, span, label, .stMarkdown {
        color: #2C3E50 !important;
    }

    /* Animations */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Card Container */
    .knowledge-card {
        background: #FFFFFF !important;
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-top: 5px solid #4CAF50;
        height: 100%;
        margin-bottom: 25px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        animation: fadeInUp 0.8s ease-out forwards;
    }
    
    .knowledge-card:hover {
        transform: translateY(-12px) scale(1.02);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        border-top-color: #1B5E20;
    }

    .card-icon {
        font-size: 2.8rem;
        margin-bottom: 15px;
        display: block;
    }

    .card-title {
        font-family: 'Lexend', sans-serif;
        font-size: 1.4rem;
        font-weight: 700;
        color: #1B5E20 !important;
        margin-bottom: 12px;
    }

    .card-text {
        font-family: 'Poppins', sans-serif;
        color: #4A5568 !important;
        line-height: 1.7;
        font-size: 0.95rem;
    }

    /* Advice Box Styling */
    .advice-section {
        background: white !important;
        padding: 35px;
        border-radius: 24px;
        margin: 40px 0;
        border-left: 10px solid #2E7D32;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        animation: fadeIn 1.5s ease-in;
    }

    /* Salute Box - Forced White Text */
    .salute-container {
        text-align: center;
        background: linear-gradient(135deg, #1B5E20 0%, #388E3C 100%);
        padding: 50px;
        border-radius: 30px;
        margin-top: 50px;
        box-shadow: 0 20px 40px rgba(27, 94, 32, 0.3);
    }
    
    .salute-container h2, 
    .salute-container p, 
    .salute-container div {
        color: #FFFFFF !important;
        opacity: 1 !important;
    }

    /* Section Headers */
    .section-header {
        font-family: 'Lexend', sans-serif;
        color: #1B5E20 !important;
        border-left: 4px solid #4CAF50;
        padding-left: 15px;
        margin: 30px 0 20px 0;
    }

    .block-container {
        padding-top: 2rem !important;
    }

    /* Language Radio Button Fix */
    div[data-testid="stWidgetLabel"] p {
        color: #1B5E20 !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

apply_hub_styles()

# 🌈 Language Logic
lang = st.radio("Language / भाषा", ["English", "मराठी"], horizontal=True)
def tr(en, mr): return mr if lang=="मराठी" else en

# Header Section
st.markdown(f"""
    <div style='text-align:center; margin-bottom: 50px; animation: fadeIn 1s;'>
        <h1 style='color:#1B5E20 !important; font-family: "Lexend"; font-size: 48px; margin-bottom: 10px;'>🌱 {tr("Farmer Intelligence Hub", "शेतकरी माहिती केंद्र")}</h1>
        <p style='color: #556B2F !important; font-size: 1.2rem; max-width: 800px; margin: 0 auto; font-weight: 500;'>
            {tr("Advanced agricultural science translated for the modern Indian field.", 
                "आधुनिक भारतीय शेतीसाठी प्रगत कृषी विज्ञानाचे सोप्या भाषेत विश्लेषण.")}
        </p>
    </div>
""", unsafe_allow_html=True)

# Helper function to create cards
def draw_card(icon, title, body):
    st.markdown(f"""
        <div class="knowledge-card">
            <span class="card-icon">{icon}</span>
            <div class="card-title">{title}</div>
            <div class="card-text">{body}</div>
        </div>
    """, unsafe_allow_html=True)

# --- SECTION 1: ENVIRONMENTAL VITALS ---
st.markdown(f"<h2 class='section-header'>{tr('Environmental Vitals', 'पर्यावरणीय घटक')}</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    draw_card("🌡️", tr("Temperature Management", "तापमान व्यवस्थापन"), tr(
        "<b>Goldilocks Zone:</b> 25–32°C. Above 35°C, pollen becomes sterile. Use <b>mulching</b> to keep soil 5°C cooler during heatwaves.",
        "<b>आदर्श तापमान:</b> २५–३२°C. ३५°C च्या वर परागकण निकामी होतात. उष्णतेत जमीन ५°C थंड ठेवण्यासाठी <b>आच्छादन (Mulching)</b> वापरा."
    ))

with col2:
    draw_card("💧", tr("Atmospheric Humidity", "हवेतील आर्द्रता"), tr(
        "High humidity (>75%) slows down 'Transpiration' (plant sweating), leading to nutrient deficiency. Ensure proper <b>row spacing</b> for airflow.",
        "जास्त आर्द्रता (>७५%) बाष्पोत्सर्जन मंदावते, ज्यामुळे अन्नाची कमतरता भासते. हवेच्या प्रवाहासाठी <b>दोन ओळींत योग्य अंतर</b> ठेवा."
    ))

with col3:
    draw_card("🧪", tr("Water pH Levels", "पाण्याचा सामू (pH)"), tr(
        "Ideal irrigation water pH is <b>6.5 to 7.0</b>. Hard water (High pH) blocks Phosphorus and Iron from reaching the roots.",
        "पाण्याचा आदर्श सामू <b>६.५ ते ७.०</b> असावा. जास्त सामू (क्षारयुक्त पाणी) स्फुरद आणि लोह मुळांपर्यंत पोहोचण्यापासून रोखते."
    ))

# --- SECTION 2: SOIL & NUTRITION ---
st.markdown(f"<h2 class='section-header'>{tr('Soil & Nutrition Science', 'माती आणि पोषण विज्ञान')}</h2>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    draw_card("🌍", tr("Texture & Drainage", "मातीची रचना आणि निचरा"), tr(
        "<b>Black Soil:</b> Holds water 3x longer; avoid over-irrigation.<br><b>Sandy Soil:</b> Low cation exchange; needs smaller, frequent fertilizer doses.",
        "<b>काळी माती:</b> ३ पट जास्त पाणी धरते; जास्त पाणी टाळा.<br><b>रेताड माती:</b> खताची क्षमता कमी; खताच्या छोट्या आणि वारंवार मात्रा द्या."
    ))

with col5:
    draw_card("🧬", tr("NPK Deep-Dive", "NPK सखोल माहिती"), tr(
        "<b>Nitrogen (N):</b> The engine for growth.<br><b>Phosphorus (P):</b> The root architect.<br><b>Potassium (K):</b> The immunity booster against pests.",
        "<b>नत्र (N):</b> वाढीचे इंजिन.<br><b>स्फुरद (P):</b> मुळांचा निर्माता.<br><b>पालाश (K):</b> कीड-रोगाविरुद्ध प्रतिकारशक्ती वाढवणारे."
    ))

with col6:
    draw_card("🛡️", tr("Pest Prevention", "कीड प्रतिबंध"), tr(
        "Healthy plants resist pests better. Use <b>Neem Oil</b> sprays as a systemic preventive measure before the infestation peaks.",
        "निरोगी पिके कीडीला चांगला प्रतिकार करतात. प्रादुर्भाव वाढण्यापूर्वी प्रतिबंधात्मक उपाय म्हणून <b>निंबोळी अर्काची</b> फवारणी करा."
    ))

# Advice Box
st.markdown(f"""
    <div class="advice-section">
        <h3 style="color: #1B5E20 !important; margin-top: 0; font-family: 'Lexend';">🎯 {tr("The Master Farmer's Protocol", "प्रगत शेतकरी नियमावली")}</h3>
        <div style="display: flex; gap: 30px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 280px;">
                <h4 style="color:#2E7D32 !important; margin-bottom:10px;">🕒 {tr("The 10 AM Rule", "सकाळचा १० चा नियम")}</h4>
                <p>{tr("Always irrigate before 10 AM to minimize evaporation loss and fungal growth on wet leaves at night.", 
                        "बाष्पीभवन आणि रात्री पानांवर होणारी बुरशी टाळण्यासाठी नेहमी सकाळी १० पूर्वी पाणी द्या.")}</p>
            </div>
            <div style="flex: 1; min-width: 280px;">
                <h4 style="color:#2E7D32 !important; margin-bottom:10px;">📉 {tr("Diminishing Returns", "घटते उत्पन्न नियम")}</h4>
                <p>{tr("Adding extra fertilizer beyond soil capacity doesn't increase yield; it poisons the soil and burns the roots.", 
                        "क्षमतेपेक्षा जास्त खत घातल्याने उत्पन्न वाढत नाही; उलट माती विषारी होते आणि मुळे जळतात.")}</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Salute
st.markdown(f"""
    <div class="salute-container">
        <h2 style="margin-top:0; font-family: 'Lexend'; font-size: 2.5rem;">🚜 {tr("To the Guardians of the Earth", "धरतीपुत्रांना नमन")}</h2>
        <p style="font-size: 1.3rem; line-height: 1.6; max-width: 800px; margin: 0 auto;">
            {tr("While the world sleeps, you work. While the world eats, it's because of you. We believe that with the right science, your hard work will double your prosperity.", 
                "जेव्हा जग झोपलेले असते, तेव्हा तुम्ही काम करता. जग जेवते, कारण तुम्ही कष्ट करता. आमचा विश्वास आहे की योग्य विज्ञानामुळे तुमची भरभराट दुप्पट होईल.")}
        </p>
        <div style="font-weight: bold; font-size: 1.6rem; margin-top: 25px; letter-spacing: 1px;">
            {tr("Vande Kisan! 🌾🇮🇳", "वंदे किसान! 🌾🇮🇳")}
        </div>
    </div>
""", unsafe_allow_html=True)

# Interactive "Next Step" for the user
st.write("---")
if st.button(tr("✨ Generate PDF Knowledge Summary", "✨ माहितीचा सारांश PDF मध्ये मिळवा")):
    st.balloons()
    st.success(tr("Feature coming soon! Your personalized report is being prepared.", "हे वैशिष्ट्य लवकरच येत आहे! तुमचा अहवाल तयार केला जात आहे."))