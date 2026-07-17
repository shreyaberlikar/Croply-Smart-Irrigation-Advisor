# 🌱 Croply – Smart Irrigation Advisor

An AI-powered Smart Irrigation Advisor that helps farmers make informed irrigation decisions by analyzing crop, soil, and environmental parameters. The system predicts irrigation requirements using a Machine Learning model and provides intelligent recommendations through an interactive web application.

---

## 🚀 Features

- 💧 Predicts irrigation requirements using Machine Learning
- 🌾 Crop-specific irrigation recommendations
- 🌱 Supports multiple crop and soil types
- 📊 Interactive and user-friendly interface
- 🤖 Random Forest-based prediction model
- 📚 Knowledge Hub for farming information
- 📝 Crop recommendation and advisory pages
- ⚡ Fast and responsive Streamlit application

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Random Forest Classifier
- Joblib
- HTML & CSS
- Git & GitHub

---

## 📂 Project Structure

```
Croply-Smart-Irrigation-Advisor/
│
├── Home.py
├── backend.py
├── train_irrigation_model.py
├── crop_data.csv
├── encoded_crop_data.csv
├── random_forest_irrigation_model.pkl
├── crop_encoder.pkl
├── soil_encoder.pkl
├── fert_encoder.pkl
├── target_encoder.pkl
├── style.css
├── pages/
│   ├── 1_Input_Page.py
│   ├── 2_Recommendation.py
│   ├── 3_Crop Master.py
│   ├── 4_The Knowledge Hub.py
│   └── 5_About Us.py
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/shreyaberlikar/Croply-Smart-Irrigation-Advisor.git
```

### Navigate to the project

```bash
cd Croply-Smart-Irrigation-Advisor
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run Home.py
```

---

## 📊 Machine Learning Workflow

1. Load and preprocess agricultural dataset
2. Encode categorical features
3. Train Random Forest model
4. Save trained model using Joblib
5. Accept user inputs through Streamlit
6. Predict irrigation requirement
7. Display irrigation recommendation

---

## 📸 Application Screens

- 🏠 Home Page
- 🌾 Input Page
- 💧 Irrigation Recommendation
- 📚 Knowledge Hub
- 👨‍💻 About Us

> Add screenshots here for a better GitHub presentation.

---

## 🎯 Future Enhancements

- 🌦️ Live weather API integration
- 🛰️ Satellite-based crop monitoring
- 📱 Mobile application
- 🌍 Multi-language support
- 🤖 AI chatbot for farmers
- 📈 Real-time analytics dashboard

---

## 👩‍💻 Developed By

**Shreya Berlikar**

- GitHub: https://github.com/shreyaberlikar
- LinkedIn: https://www.linkedin.com/in/shreyaberlikar

---

## ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub!
