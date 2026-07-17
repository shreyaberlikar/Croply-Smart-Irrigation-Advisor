import streamlit as st
from fpdf import FPDF
import random
from datetime import datetime

# =====================================
# 🌸 CUSTOM FLOWER ANIMATION
# =====================================
def show_flower_animation():
    flowers = ['🌸', '🌺', '🌻', '🌼', '🌷']
    html_elements = ""
    for i in range(35):
        f = random.choice(flowers)
        left = random.randint(0, 100)
        duration = random.uniform(3, 6)
        delay = random.uniform(0, 2)
        size = random.uniform(1.2, 2.5)
        html_elements += f'<div class="flower" style="left: {left}%; animation-duration: {duration}s; animation-delay: {delay}s; font-size: {size}rem;">{f}</div>'
    
    css = """
    <style>
    .flower { position: fixed; top: -10%; z-index: 99999; user-select: none; pointer-events: none; animation-name: fall; animation-timing-function: linear; animation-fill-mode: forwards; }
    @keyframes fall { 0% { transform: translateY(-10vh) rotate(0deg) scale(1); opacity: 1; } 100% { transform: translateY(110vh) rotate(360deg) scale(0.8); opacity: 0; } }
    </style>
    """
    st.markdown(css + html_elements, unsafe_allow_html=True)

# =====================================
# 📄 PDF GENERATION FUNCTION
# =====================================
def create_knowledge_pdf():
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_fill_color(27, 94, 32)
    pdf.rect(0, 0, 210, 40, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", 'B', 22)
    pdf.cell(0, 15, "FARMER INTELLIGENCE HUB", ln=True, align='C')
    pdf.set_font("Arial", '', 11)
    pdf.cell(0, 5, f"Advanced Agricultural Science Summary | {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='C')
    pdf.ln(20)
    
    pdf.set_text_color(27, 94, 32)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "1. Environmental Vitals", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, "- Temperature Management: Goldilocks Zone is 25-32C. Above 35C, pollen becomes sterile.\n- Atmospheric Humidity: High humidity (>75%) slows transpiration.\n- Water pH Levels: Ideal is 6.5 to 7.0.")
    pdf.ln(5)

    pdf.set_text_color(27, 94, 32)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "2. Soil & Nutrition Science", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, "- Texture & Drainage: Black soil holds water 3x longer. Sandy soil needs frequent doses.\n- NPK Deep-Dive: Nitrogen (Growth), Phosphorus (Roots), Potassium (Immunity).\n- Pest Prevention: Use Neem Oil sprays as preventive measure.")
    pdf.ln(5)

    pdf.set_text_color(27, 94, 32)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "3. The Master Farmer's Protocol", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, "- The 10 AM Rule: Always irrigate before 10 AM to minimize evaporation loss.\n- Diminishing Returns: Extra fertilizer beyond soil capacity poisons the soil.")
    pdf.ln(15)

    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(46, 125, 50)
    pdf.multi_cell(0, 8, "To the Guardians of the Earth:\nWhile the world sleeps, you work. While the world eats, it's because of you. Vande Kisan!", align='C')

    return bytes(pdf.output(dest='S'))

# =====================================
# 1. Page Configuration & CSS
# =====================================
st.set_page_config(page_title="Croply | Knowledge Hub Pro", layout="wide")

def apply_hub_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Lexend:wght@400;700&display=swap');
    .stApp { background-color: #F0F4F2; }
    .stApp, p, li, span, label, .stMarkdown { color: #2C3E50 !important; }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
    .knowledge-card { background: #FFFFFF !important; padding: 24px; border-radius: 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border-top: 5px solid #4CAF50; height: 100%; margin-bottom: 25px; transition: all 0.4s; animation: fadeInUp 0.8s ease-out forwards; }
    .knowledge-card:hover { transform: translateY(-12px) scale(1.02); box-shadow: 0 15px 35px rgba(0,0,0,0.1); border-top-color: #1B5E20; }
    .card-icon { font-size: 2.8rem; margin-bottom: 15px; display: block; }
    .card-title { font-family: 'Lexend', sans-serif; font-size: 1.4rem; font-weight: 700; color: #1B5E20 !important; margin-bottom: 12px; }
    .card-text { font-family: 'Poppins', sans-serif; color: #4A5568 !important; line-height: 1.7; font-size: 0.95rem; }
    .advice-section { background: white !important; padding: 35px; border-radius: 24px; margin: 40px 0; border-left: 10px solid #2E7D32; box-shadow: 0 4px 15px rgba(0,0,0,0.05); animation: fadeIn 1.5s ease-in; }
    .salute-container { text-align: center; background: linear-gradient(135deg, #1B5E20 0%, #388E3C 100%); padding: 50px; border-radius: 30px; margin-top: 50px; box-shadow: 0 20px 40px rgba(27, 94, 32, 0.3); }
    .salute-container h2, .salute-container p, .salute-container div { color: #FFFFFF !important; opacity: 1 !important; }
    .section-header { font-family: 'Lexend', sans-serif; color: #1B5E20 !important; border-left: 4px solid #4CAF50; padding-left: 15px; margin: 30px 0 20px 0; }
    div[data-testid="stWidgetLabel"] p { color: #1B5E20 !important; font-weight: 600 !important; }
    </style>
    """, unsafe_allow_html=True)

apply_hub_styles()

# =====================================
# 🌈 Language Logic & UI
# =====================================
lang = st.radio("Language / भाषा", ["English", "मराठी"], horizontal=True)
def tr(en, mr): return mr if lang=="मराठी" else en

# Header Section
st.markdown(f"""
    <div style='text-align:center; margin-bottom: 30px; animation: fadeIn 1s;'>
        <h1 style='color:#1B5E20 !important; font-family: "Lexend"; font-size: 48px; margin-bottom: 10px;'>🌱 {tr("Farmer Intelligence Hub", "शेतकरी माहिती केंद्र")}</h1>
        <p style='color: #556B2F !important; font-size: 1.2rem; max-width: 800px; margin: 0 auto; font-weight: 500;'>
            {tr("Advanced agricultural science translated for the modern Indian field.", "आधुनिक भारतीय शेतीसाठी प्रगत कृषी विज्ञानाचे सोप्या भाषेत विश्लेषण.")}
        </p>
    </div>
""", unsafe_allow_html=True)

# ☀️ DYNAMIC SEASONAL BANNER
current_month = datetime.now().month
if current_month in [3, 4, 5]: # Summer Months
    st.warning(tr("☀️ **Summer Alert:** Soil moisture evaporates rapidly this season. Use organic mulching (straw/dry leaves) to retain moisture and keep roots cool!", 
                  "☀️ **उन्हाळा इशारा:** या ऋतूत जमिनीतील ओलावा वेगाने बाष्पीभवन होतो. ओलावा टिकवून ठेवण्यासाठी आणि मुळे थंड ठेवण्यासाठी सेंद्रिय आच्छादन (पाचट/वाळलेली पाने) वापरा!"), icon="⚠️")

# 🌾 PERSONALIZED CROP ADVICE
if 'farm_inputs' in st.session_state:
    user_crop = st.session_state.farm_inputs.get('Crop Type', 'your crop')
    st.success(f"{tr('🌾 **Smart Tip for**', '🌾 **तुमच्या पिकासाठी खास सल्ला -**')} **{user_crop}**: {tr('Monitor the early growth stages closely. Proper spacing prevents fungal infections and boosts yield.', 'सुरुवातीच्या वाढीच्या टप्प्यावर बारकाईने लक्ष ठेवा. योग्य अंतरामुळे बुरशीजन्य संसर्ग टळतो आणि उत्पन्न वाढते.')}", icon="💡")

def draw_card(icon, title, body):
    st.markdown(f'<div class="knowledge-card"><span class="card-icon">{icon}</span><div class="card-title">{title}</div><div class="card-text">{body}</div></div>', unsafe_allow_html=True)

# --- SECTION 1 ---
st.markdown(f"<h2 class='section-header'>{tr('Environmental Vitals', 'पर्यावरणीय घटक')}</h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1: draw_card("🌡️", tr("Temperature Management", "तापमान व्यवस्थापन"), tr("<b>Goldilocks Zone:</b> 25–32°C. Above 35°C, pollen becomes sterile. Use <b>mulching</b> to keep soil 5°C cooler during heatwaves.", "<b>आदर्श तापमान:</b> २५–३२°C. ३५°C च्या वर परागकण निकामी होतात. उष्णतेत जमीन ५°C थंड ठेवण्यासाठी <b>आच्छादन (Mulching)</b> वापरा."))
with col2: draw_card("💧", tr("Atmospheric Humidity", "हवेतील आर्द्रता"), tr("High humidity (>75%) slows down 'Transpiration' (plant sweating), leading to nutrient deficiency. Ensure proper <b>row spacing</b> for airflow.", "जास्त आर्द्रता (>७५%) बाष्पोत्सर्जन मंदावते, ज्यामुळे अन्नाची कमतरता भासते. हवेच्या प्रवाहासाठी <b>दोन ओळींत योग्य अंतर</b> ठेवा."))
with col3: draw_card("🧪", tr("Water pH Levels", "पाण्याचा सामू (pH)"), tr("Ideal irrigation water pH is <b>6.5 to 7.0</b>. Hard water (High pH) blocks Phosphorus and Iron from reaching the roots.", "पाण्याचा आदर्श सामू <b>६.५ ते ७.०</b> असावा. जास्त सामू (क्षारयुक्त पाणी) स्फुरद आणि लोह मुळांपर्यंत पोहोचण्यापासून रोखते."))

# --- SECTION 2 ---
st.markdown(f"<h2 class='section-header'>{tr('Soil & Nutrition Science', 'माती आणि पोषण विज्ञान')}</h2>", unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)
with col4: draw_card("🌍", tr("Texture & Drainage", "मातीची रचना आणि निचरा"), tr("<b>Black Soil:</b> Holds water 3x longer; avoid over-irrigation.<br><b>Sandy Soil:</b> Low cation exchange; needs smaller, frequent fertilizer doses.", "<b>काळी माती:</b> ३ पट जास्त पाणी धरते; जास्त पाणी टाळा.<br><b>रेताड माती:</b> खताची क्षमता कमी; खताच्या छोट्या आणि वारंवार मात्रा द्या."))
with col5: draw_card("🧬", tr("NPK Deep-Dive", "NPK सखोल माहिती"), tr("<b>Nitrogen (N):</b> The engine for growth.<br><b>Phosphorus (P):</b> The root architect.<br><b>Potassium (K):</b> The immunity booster against pests.", "<b>नत्र (N):</b> वाढीचे इंजिन.<br><b>स्फुरद (P):</b> मुळांचा निर्माता.<br><b>पालाश (K):</b> कीड-रोगाविरुद्ध प्रतिकारशक्ती वाढवणारे."))
with col6: draw_card("🛡️", tr("Pest Prevention", "कीड प्रतिबंध"), tr("Healthy plants resist pests better. Use <b>Neem Oil</b> sprays as a systemic preventive measure before the infestation peaks.", "निरोगी पिके कीडीला चांगला प्रतिकार करतात. प्रादुर्भाव वाढण्यापूर्वी प्रतिबंधात्मक उपाय म्हणून <b>निंबोळी अर्काची</b> फवारणी करा."))


# --- NEW EXPANDED INTERACTIVE SECTION ---
st.markdown(f"<h2 class='section-header'>🧠 {tr('Interactive Learning', 'परस्परसंवादी शिक्षण')}</h2>", unsafe_allow_html=True)
faq_col, myth_col = st.columns([1.5, 1])

with faq_col:
    st.write(f"### {tr('Frequently Asked Questions', 'वारंवार विचारले जाणारे प्रश्न')}")
    
    with st.expander(tr("🌱 What is the cheapest way to increase soil carbon?", "🌱 जमिनीत सेंद्रिय कर्ब वाढवण्याचा सर्वात स्वस्त मार्ग कोणता?")):
        st.write(tr("Planting **Green Manure crops** like Dhaincha (धैंचा) or Sunhemp (ताग) and ploughing them back into the soil before they flower.", "ताग किंवा धैंचा यांसारखी **हिरवळीची खते** पेरणे आणि त्यांना फुले येण्यापूर्वी जमिनीत गाडणे हा सर्वात स्वस्त मार्ग आहे."))
    
    with st.expander(tr("🔍 How do I know if my soil is too acidic?", "🔍 माती जास्त आम्लयुक्त (Acidic) आहे हे कसे ओळखावे?")):
        st.write(tr("Signs include yellowing of leaves (chlorosis) and stunted root growth. The best way is to do a proper **Soil Test** at your local Krishi Vigyan Kendra.", "पाने पिवळी पडणे आणि मुळांची वाढ खुंटणे ही लक्षणे आहेत. स्थानिक कृषी विज्ञान केंद्रात **माती परीक्षण** करणे हा सर्वोत्तम मार्ग आहे."))
        
    with st.expander(tr("💦 Should I water a little bit every day, or a lot less often?", "💦 पिकांना दररोज थोडे पाणी द्यावे की कमी वेळा पण भरपूर पाणी द्यावे?")):
        st.write(tr("**Deep, infrequent watering is better.** It encourages plant roots to grow deeper into the soil searching for water, making them stronger and more drought-resistant.", "**कमी वेळा पण भरपूर पाणी देणे जास्त चांगले.** यामुळे पिकांची मुळे पाण्याच्या शोधात जमिनीत खोलवर वाढतात आणि पीक दुष्काळातही तग धरू शकते."))

    with st.expander(tr("🕒 When is the best time to spray pesticides?", "🕒 कीटकनाशके फवारणीची सर्वोत्तम वेळ कोणती?")):
        st.write(tr("**Late afternoon or early evening.** This prevents the sun from burning the wet leaves and protects friendly insects like bees, which are usually active in the morning.", "**दुपारनंतर किंवा संध्याकाळी.** यामुळे उन्हामुळे पाने जळत नाहीत आणि सकाळी सक्रिय असलेल्या मधमाश्यांसारख्या मित्र कीटकांचे रक्षण होते."))

with myth_col:
    st.write(f"### {tr('Myth vs Fact Checker', 'गैरसमज आणि सत्य')}")
    
    # Myth 1
    st.info(tr('**Myth 1:** "Applying more chemical fertilizer will always give a higher crop yield."', '**गैरसमज १:** "जास्त रासायनिक खत टाकल्याने नेहमी जास्त पीक येते."'))
    if st.button(tr("Reveal the Truth! 🔍", "सत्य जाणून घ्या! 🔍"), key="myth1"):
        st.error(tr('**FACT:** False! Excess fertilizer creates toxic salt buildup, burns plant roots, and destroys helpful earthworms in the soil.', '**सत्य:** हे खोटे आहे! अतिरिक्त खतामुळे जमिनीत क्षारांचे प्रमाण वाढते, मुळे जळतात आणि जमिनीतील उपयुक्त गांडुळे नष्ट होतात.'))

    # Myth 2
    st.info(tr('**Myth 2:** "Leaving soil bare and plowed between seasons gives the land a much-needed rest."', '**गैरसमज २:** "दोन पिकांच्या मध्ये जमीन नांगरून तशीच उघडी सोडल्याने जमिनीला विश्रांती मिळते."'))
    if st.button(tr("Reveal the Truth! 🔍", "सत्य जाणून घ्या! 🔍"), key="myth2"):
        st.error(tr('**FACT:** False! Bare soil leads to topsoil erosion from wind and rain. It also starves beneficial soil bacteria. Always use cover crops!', '**सत्य:** खोटे! उघड्या जमिनीवरील सुपीक माती वारा आणि पावसाने वाहून जाते. तसेच उपयुक्त जिवाणू मरतात. नेहमी आच्छादन पिके (Cover crops) घ्यावीत!'))

    # Myth 3
    st.info(tr('**Myth 3:** "Chemical pesticides only kill the bad bugs that eat my crops."', '**गैरसमज ३:** "कीटकनाशके फक्त माझ्या पिकांचे नुकसान करणाऱ्या कीटकांनाच मारतात."'))
    if st.button(tr("Reveal the Truth! 🔍", "सत्य जाणून घ्या! 🔍"), key="myth3"):
        st.error(tr('**FACT:** False! Most pesticides are broad-spectrum, meaning they also kill friendly insects like bees, butterflies, and ladybugs that pollinate and protect your farm.', '**सत्य:** खोटे! बहुतेक कीटकनाशके मित्र कीटकांना (उदा. मधमाश्या, फुलपाखरे, लेडीबग) देखील मारतात जे पिकांचे परागीभवन आणि रक्षण करतात.'))


# --- ADVICE BOX ---
st.markdown(f"""
    <div class="advice-section">
        <h3 style="color: #1B5E20 !important; margin-top: 0; font-family: 'Lexend';">🎯 {tr("The Master Farmer's Protocol", "प्रगत शेतकरी नियमावली")}</h3>
        <div style="display: flex; gap: 30px; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 280px;">
                <h4 style="color:#2E7D32 !important; margin-bottom:10px;">🕒 {tr("The 10 AM Rule", "सकाळचा १० चा नियम")}</h4>
                <p>{tr("Always irrigate before 10 AM to minimize evaporation loss and fungal growth on wet leaves at night.", "बाष्पीभवन आणि रात्री पानांवर होणारी बुरशी टाळण्यासाठी नेहमी सकाळी १० पूर्वी पाणी द्या.")}</p>
            </div>
            <div style="flex: 1; min-width: 280px;">
                <h4 style="color:#2E7D32 !important; margin-bottom:10px;">📉 {tr("Diminishing Returns", "घटते उत्पन्न नियम")}</h4>
                <p>{tr("Adding extra fertilizer beyond soil capacity doesn't increase yield; it poisons the soil and burns the roots.", "क्षमतेपेक्षा जास्त खत घातल्याने उत्पन्न वाढत नाही; उलट माती विषारी होते आणि मुळे जळतात.")}</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- SALUTE ---
st.markdown(f"""
    <div class="salute-container">
        <h2 style="margin-top:0; font-family: 'Lexend'; font-size: 2.5rem;">🚜 {tr("To the Guardians of the Earth", "धरतीपुत्रांना नमन")}</h2>
        <p style="font-size: 1.3rem; line-height: 1.6; max-width: 800px; margin: 0 auto;">
            {tr("While the world sleeps, you work. While the world eats, it's because of you. We believe that with the right science, your hard work will double your prosperity.", "जेव्हा जग झोपलेले असते, तेव्हा तुम्ही काम करता. जग जेवते, कारण तुम्ही कष्ट करता. आमचा विश्वास आहे की योग्य विज्ञानामुळे तुमची भरभराट दुप्पट होईल.")}
        </p>
        <div style="font-weight: bold; font-size: 1.6rem; margin-top: 25px; letter-spacing: 1px;">
            {tr("Vande Kisan! 🌾", "वंदे किसान! 🌾")}
        </div>
    </div>
""", unsafe_allow_html=True)

# =====================================
# 📥 DOWNLOAD SECTION WITH ANIMATION
# =====================================
st.write("---")
pdf_data = create_knowledge_pdf()

col_btn, _ = st.columns([1, 2])
with col_btn:
    if st.download_button(
        label=tr("📥 Download PDF Summary", "📥 माहितीचा सारांश PDF डाउनलोड करा"),
        data=pdf_data,
        file_name="Croply_Intelligence_Hub.pdf",
        mime="application/pdf"
    ):
        st.session_state.hub_downloaded = True

if st.session_state.get('hub_downloaded'):
    show_flower_animation()
    st.success(tr("✅ **Download Complete!** Your educational summary is ready.", "✅ **डाउनलोड पूर्ण झाले!** तुमचा शैक्षणिक सारांश तयार आहे."))
    st.toast("📄 Knowledge PDF saved successfully!", icon="✅")
    st.session_state.hub_downloaded = False