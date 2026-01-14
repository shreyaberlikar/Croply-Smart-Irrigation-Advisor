import streamlit as st
import plotly.graph_objects as go
import os
import requests
import joblib 
import pandas as pd
from datetime import datetime

# =====================================
# 🛠️ BACKEND LINK (Logic Untouched)
# =====================================
try:
    model = joblib.load('random_forest_irrigation_model.pkl')
    target_enc = joblib.load('target_encoder.pkl')
    crop_enc = joblib.load('crop_encoder.pkl')
    soil_enc = joblib.load('soil_encoder.pkl')
    fert_enc = joblib.load('fert_encoder.pkl')
except Exception as e:
    st.error(f"⚠️ Model files missing: {e}")

# 1. Page Configuration
st.set_page_config(page_title="Croply | Recommendation", layout="wide")

# 2. Enhanced CSS for Attraction
def load_enhanced_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;700&family=Poppins:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    h1, h2, h3 { font-family: 'Lexend', sans-serif; }

    /* The Hero Recommendation Box */
    .hero-recommendation {
        background: linear-gradient(135deg, #1B5E20 0%, #388E3C 100%);
        color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(27, 94, 32, 0.2);
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.1);
        animation: fadeInDown 0.8s ease-out;
    }

    .hero-label { font-size: 1.2rem; opacity: 0.9; text-transform: uppercase; letter-spacing: 2px; }
    .hero-action { font-size: 2.8rem; font-weight: 700; margin: 10px 0; }

    /* Glass Cards */
    .analysis-card, .weather-card-new {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.04);
        border: 1px solid #E8F5E9;
        margin-bottom: 20px;
    }

    .rec-header {
        font-family: 'Lexend';
        color: #1B5E20;
        font-weight: 700;
        font-size: 1.3rem;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-weight: 600;
        transition: all 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if os.path.exists("style.css"):
        with open("style.css") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # if os.path.exists("navbar.html"):
    #     with open("navbar.html") as f:
    #         st.markdown(f.read(), unsafe_allow_html=True)

load_enhanced_styles()

# 3. Data Retrieval & Logic (Untouched)
if "farm_inputs" not in st.session_state:
    st.error("⚠️ Please enter farm data on the Input Page first!")
    st.stop()

data = st.session_state.farm_inputs
moisture_val = data['Moisture']
city = data.get('Location', 'Mumbai')

# Weather Fetch (Untouched)
def get_weather_description(code):
    mapping = {0: "Clear Sky ☀️", 1: "Mainly Clear 🌤️", 2: "Partly Cloudy ⛅", 3: "Overcast ☁️", 61: "Slight Rain 🌧️", 95: "Thunderstorm 🌩️"}
    return mapping.get(code, "Cloudy ☁️")

def fetch_live_weather(location_name):
    try:
        geo_url = f"https://nominatim.openstreetmap.org/search?q={location_name}&format=json&limit=1"
        geo_res = requests.get(geo_url, headers={'User-Agent': 'CroplyApp/1.0'}).json()
        lat, lon = geo_res[0]['lat'], geo_res[0]['lon']
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m,weather_code&hourly=precipitation_probability&forecast_days=1"
        w_data = requests.get(weather_url).json()
        return {
            "temp": w_data['current']['temperature_2m'],
            "humidity": w_data['current']['relative_humidity_2m'],
            "pressure": w_data['current']['surface_pressure'],
            "wind": w_data['current']['wind_speed_10m'],
            "condition": get_weather_description(w_data['current']['weather_code']),
            "pop": w_data['hourly']['precipitation_probability'][0]
        }
    except: return None

with st.spinner(f"Analyzing {city}..."):
    weather = fetch_live_weather(city)

f_temp, f_humid, f_pres, f_wind, f_cond, f_pop = (weather["temp"], weather["humidity"], weather["pressure"], weather["wind"], weather["condition"], weather["pop"]) if weather else (25, 50, 1013, 10, "Clear Sky ☀️", 0)

# AI PREDICTION (Untouched Logic)
soil_num = soil_enc.transform([data['Soil Type']])[0]
crop_num = crop_enc.transform([data['Crop Type']])[0]
fert_num = fert_enc.transform([data.get('Fertilizer Name', 'Urea')])[0]

input_df = pd.DataFrame([[f_temp, f_humid, moisture_val, soil_num, crop_num, data['Nitrogen'], data['Potassium'], data['Phosphorous'], fert_num]], 
                        columns=["Temparature","Humidity","Moisture","Soil Type","Crop Type","Nitrogen","Potassium","Phosphorous","Fertilizer Name"])

prediction = model.predict(input_df)[0]
ai_label = target_enc.inverse_transform([prediction])[0]
will_rain_soon = f_pop > 50

# Action Logic
if ai_label == "NONE":
    hero_msg = "✅ MOISTURE OPTIMAL"
    sub_msg = "No irrigation required at this time."
    status_icon = "🌿"
elif will_rain_soon:
    hero_msg = "⚠️ POSTPONE FOR RAIN"
    sub_msg = f"Model suggests irrigation, but {f_pop}% rain chance detected."
    status_icon = "🌦️"
else:
    hero_msg = f"💧 {ai_label} IRRIGATION"
    sub_msg = f"AI recommends applying water based on {data['Crop Type']} needs."
    status_icon = "🚜"

# =====================================
# 🚀 VISUAL OUTPUT
# =====================================

# 1. THE HERO SECTION (First thing user notices)
st.markdown(f"""
    <div class="hero-recommendation">
        <div class="hero-label">AI Smart Recommendation</div>
        <div class="hero-action">{status_icon} {hero_msg}</div>
        <div style="font-size: 1.2rem; opacity: 0.9;">{sub_msg}</div>
    </div>
""", unsafe_allow_html=True)

# 2. Main Analysis Grid
col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    # GAUGE
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = moisture_val,
        title = {'text': "Current Soil Moisture", 'font': {'family': 'Lexend', 'size': 20}},
        number = {'suffix': "%", 'font': {'color': '#1B5E20'}},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#2E7D32"},
            'steps': [{'range': [0, 30], 'color': "#FFEBEE"}, {'range': [30, 70], 'color': "#FFFDE7"}, {'range': [70, 100], 'color': "#E8F5E9"}]
        }
    ))
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20), paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

    # WEATHER
    st.markdown(f"""
        <div class="weather-card-new">
            <div class="rec-header">☁️ Local Forecast: {city}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="font-size: 2rem;">{f_cond.split()[-1]}</span>
                <span style="font-size: 1.5rem; font-weight: bold; color: #1B5E20;">{f_temp}°C</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; font-size: 0.9rem; color: #666;">
                <span>💧 Humidity: <b>{f_humid}%</b></span>
                <span>💨 Wind: <b>{f_wind} km/h</b></span>
                <span>🌧️ Rain Chance: <b>{f_pop}%</b></span>
                <span>⏲️ Pressure: <b>{f_pres} hPa</b></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # NUTRIENTS
    def get_status_html(val, label_name):
        color = "#e53935" if val < 30 else "#43a047" if val < 70 else "#fb8c00"
        status = "LOW" if val < 30 else "OPTIMAL" if val < 70 else "HIGH"
        return f"""<div style="text-align: center;">
            <div style="color: #666; font-size: 0.8rem;">{label_name}</div>
            <div style="font-size: 1.2rem; font-weight: bold;">{val}</div>
            <div style="background: {color}; color: white; font-size: 0.7rem; padding: 2px 8px; border-radius: 10px; display: inline-block;">{status}</div>
        </div>"""

    st.markdown(f"""
        <div class="analysis-card">
            <div class="rec-header">🧬 Soil Nutrient Profile</div>
            <div style="display: flex; justify-content: space-around; padding: 10px 0;">
                {get_status_html(data['Nitrogen'], 'Nitrogen (N)')}
                {get_status_html(data['Phosphorous'], 'Phosphorous (P)')}
                {get_status_html(data['Potassium'], 'Potassium (K)')}
            </div>
            <div style="margin-top: 20px; font-size: 0.9rem; color: #444; border-top: 1px solid #eee; padding-top: 10px;">
                <b>Soil Type:</b> {data['Soil Type']} | <b>Fertilizer Base:</b> {data.get('Fertilizer Name', 'Urea')}
            </div>
        </div>
        
        <div class="analysis-card" style="border-left: 5px solid #1B5E20;">
            <div class="rec-header">📝 Detailed Action Plan</div>
            <p style="font-size: 0.95rem; line-height: 1.6; color: #333;">
                The analysis for <b>{data['Crop Type']}</b> indicates that watering is 
                <b>{"not needed" if ai_label == "NONE" or will_rain_soon else "urgently required"}</b>. 
                {sub_msg} Keep monitoring soil moisture every 24 hours.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- BUTTONS WITH ANIMATION LOGIC ---
    st.write("###")
    
    # 1. Prepare the report content
    report_content = f"""
    CROPLY SMART REPORT
    -------------------
    Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    Location: {city}
    Crop: {data['Crop Type']}
    Moisture: {moisture_val}%
    AI Recommendation: {hero_msg}
    Action Plan: {sub_msg}
    """

    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        # The download button itself
        if st.download_button(
            label="📥 Download Full Report",
            data=report_content,
            file_name=f"Croply_Report_{city}.txt",
            mime="text/plain"
        ):
            # This part will execute on the next rerun after click
            st.session_state.downloaded = True

    with btn_col2:
        if st.button("🔄 New Analysis"):
            st.switch_page("pages/1_input_page.py")

    # 2. Trigger Animation if downloaded
    if st.session_state.get('downloaded'):
        st.balloons()
        st.toast("Report saved successfully!", icon="✅")
        # Reset the state so it doesn't repeat on every interaction
        st.session_state.downloaded = False