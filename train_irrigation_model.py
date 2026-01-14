# ===============================
# 🌾 SMART IRRIGATION MODEL TRAINING
# ===============================

# 📌 STEP 1: Load Data
import pandas as pd
import numpy as np

df = pd.read_csv('crop_data.csv')
print("Initial Rows:", df.shape)
print(df.head())

# 📌 STEP 2: EDA & Basic Information
print("\n===== DATA INFO =====")
print(df.info())


print("\n===== DESCRIBE =====")
print(df.describe())

print("\nUnique Soil Types:", df['Soil Type'].unique())
print("Soil Count:", df['Soil Type'].nunique())

print("\nUnique Crop Types:", df['Crop Type'].unique())
print("Crop Count:", df['Crop Type'].nunique())

print("\n===== VALUE COUNTS =====")
print(df['Soil Type'].value_counts())
print(df['Crop Type'].value_counts())
print(df['Fertilizer Name'].value_counts())

print("\nMissing Values:\n", df.isnull().sum())

# ==========================
# 🎯 REMOVE DUPLICATES
# ==========================
print("\nDuplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

# ==========================
# 🎯 LABEL ENCODING
# ==========================
from sklearn.preprocessing import LabelEncoder

categorical_cols = ['Soil Type', 'Crop Type', 'Fertilizer Name']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

df.to_csv('encoded_crop_data.csv', index=False)

# ==========================
# 🎯 CREATE FACTOR MAPPINGS
# ==========================
soil_factor = {
    'Sandy': 1.3,
    'Red': 1.2,
    'Loamy': 1.1,
    'Black': 1.0,
    'Clayey': 0.9
}

crop_factor = {
    'Paddy': 1.4,
    'Sugarcane': 1.3,
    'Cotton': 1.2,
    'Maize': 1.1,
    'Oil seeds': 1.0,
    'Millets': 0.9,
    'Wheat': 0.9,
    'Pulses': 0.8,
    'Barley': 0.8,
    'Ground Nuts': 0.8,
    'Tobacco': 1.1
}

# Map encoded labels back to factors
soil_map = {i: soil_factor[s] for i, s in enumerate(label_encoders['Soil Type'].classes_)}
crop_map = {i: crop_factor[c] for i, c in enumerate(label_encoders['Crop Type'].classes_)}

# ==========================
# 🎯 IRRIGATION SCORE FUNCTION
# ==========================
def irrigation_score(row):
    base = (50 - row['Moisture'])

    base *= soil_map.get(row['Soil Type'], 1.0)
    base *= crop_map.get(row['Crop Type'], 1.0)

    # Temperature effect (correct column name Temp vs Temparature)
    if row['Temparature'] > 32:
        base *= 1.2
    elif row['Temparature'] < 25:
        base *= 0.9

    # Humidity effect
    if row['Humidity'] < 50:
        base *= 1.2
    elif row['Humidity'] > 60:
        base *= 0.9

    return base

df['irrigation_score'] = df.apply(irrigation_score, axis=1)

# ==========================
# 🎯 LABEL: HIGH/MED/LOW/NONE
# ==========================
def irrigation_need(score):
    if score > 40:
        return "HIGH"
    elif score > 20:
        return "MEDIUM"
    elif score > 5:
        return "LOW"
    else:
        return "NONE"

df['irrigation_need'] = df['irrigation_score'].apply(irrigation_need)

# Encode final target
target_enc = LabelEncoder()
df['irrigation_need'] = target_enc.fit_transform(df['irrigation_need'])

# ==========================
# 🎯 TRAIN-TEST SPLIT
# ==========================
X = df.drop(['irrigation_need','irrigation_score'], axis=1)
y = df['irrigation_need']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True)


# ==========================
# 🎯 TRAIN RANDOM FOREST
# ==========================
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

print("\n===== RANDOM FOREST RESULTS =====")
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# ==========================
# 🎯 SAVE MODELS
# ==========================
import joblib

joblib.dump(rf_model, 'random_forest_irrigation_model.pkl')
joblib.dump(target_enc, 'target_encoder.pkl')
joblib.dump(label_encoders['Crop Type'], 'crop_encoder.pkl')
joblib.dump(label_encoders['Soil Type'], 'soil_encoder.pkl')
joblib.dump(label_encoders['Fertilizer Name'], 'fert_encoder.pkl')

print("\nSAVED FILES:")
print("random_forest_irrigation_model.pkl")
print("target_encoder.pkl")
print("crop_encoder.pkl")
print("soil_encoder.pkl")
print("fert_encoder.pkl")

