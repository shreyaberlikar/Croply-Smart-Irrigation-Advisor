import requests

# --- WMO Weather Code Mapper ---
def get_weather_description(code):
    mapping = {
        0: "Clear Sky ☀️", 1: "Mainly Clear 🌤️", 2: "Partly Cloudy ⛅", 3: "Overcast ☁️",
        45: "Foggy 🌫️", 48: "Depositing Rime Fog 🌫️", 51: "Light Drizzle 🌦️",
        61: "Slight Rain 🌧️", 63: "Moderate Rain 🌧️", 65: "Heavy Rain ⛈️",
        80: "Slight Rain Showers 🌦️", 95: "Thunderstorm 🌩️"
    }
    return mapping.get(code, "Cloudy ☁️")

# --- REAL-TIME WEATHER LOGIC ---
def fetch_live_weather(location_name):
    try:
        geo_url = f"https://nominatim.openstreetmap.org/search?q={location_name}&format=json&limit=1"
        geo_res = requests.get(geo_url, headers={'User-Agent': 'CroplyApp/1.0'}).json()
        if not geo_res: return None
        
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
    except:
        return None

# --- NUTRIENT COLOR LOGIC ---
def get_status_color(val):
    if val < 30: return "#e53935", "LOW"
    if val < 70: return "#43a047", "OPTIMAL"
    return "#fb8c00", "HIGH"

# --- CORE RECOMMENDATION LOGIC ---
def get_recommendation(moisture_val, f_pop):
    will_rain_soon = f_pop > 50
    if moisture_val < 50 and will_rain_soon:
        return f"⚠️ Wait for Rain: {f_pop}% probability detected.", "Postpone irrigation. Rain is expected soon, let nature water your crops."
    elif moisture_val < 50:
        return "💧 Water Now: Low rain probability and dry soil.", "Maintain steady irrigation. No significant rain forecast in the next few hours."
    else:
        return "✅ Optimal: Moisture is sufficient.", "Your soil moisture is at a healthy level. Continue monitoring."