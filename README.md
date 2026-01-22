#  Croply – Smart Irrigation Advisor

Croply is an AI-driven irrigation recommendation system that helps farmers decide *when* and *how much* water crops need.  
Using soil data, crop type, and live weather inputs, Croply predicts irrigation levels to reduce water waste, boost yield, and enable climate-smart farming.

---

##  Features

✔️ Predicts irrigation levels: **High / Medium / Low / None**  
✔️ ML-based insights replacing guesswork  
✔️ Inputs: soil, crop, fertilizer, and weather  
✔️ Streamlit interactive UI  
✔️ Water-saving & farmer-friendly  
✔️ Deployable web app

---

##  Workflow

1. Collect soil, crop & fertilizer dataset  
2. Fetch live weather inputs (API)  
3. Preprocess & encode data  
4. Train Random Forest Classifier  
5. Save model + encoders as `.pkl`  
6. Deploy UI using Streamlit  
7. Recommend irrigation level

---

## 🧠 Tech Stack

**Machine Learning / Data**
- Python
- Pandas, NumPy
- Scikit-Learn

**App & Deployment**
- Streamlit
- Weather API
- Pickle (model persistence)

---

## 📁 Project Structure

```
Croply/
├── data/
├── model/
│   ├── croply_model.pkl
│   └── encoders.pkl
├── app.py
├── pages/
│   └── Recommendation.py
└── README.md
```

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 Output

- ML-based irrigation recommendation
- User-friendly input page
- Clear result display for farmers

---

## 🌱 Future Scope

🔹 IoT sensor integration  
🔹 Multi-region crop support  
🔹 Offline mobile app  
🔹 Advanced weather models

---

## 🤝 Contribution

Contributions, suggestions and improvements are welcome!  
Feel free to raise issues or submit PRs.

---

## 📝 License

Distributed under the **MIT License**.
