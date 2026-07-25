# Croply – AI-Powered Smart Irrigation Advisor

> An end-to-end Machine Learning application that predicts irrigation requirements based on crop, soil, and environmental conditions to optimize water usage and support sustainable agriculture.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red)
![License](https://img.shields.io/badge/License-Educational-green)

---

# Table of Contents

- Overview
- Problem Statement
- Objectives
- Proposed Solution
- Key Features
- System Architecture
- Machine Learning Workflow
- Technology Stack
- Project Structure
- Model Information
- Installation
- Applications
- Future Enhancements
- Author
- License

---

# Overview

Croply is an AI-powered Smart Irrigation Advisor designed to assist farmers in making data-driven irrigation decisions. The system predicts irrigation requirements using Machine Learning by analyzing crop characteristics, soil properties, fertilizer composition, and environmental conditions.

The application promotes efficient water management, reduces unnecessary irrigation, and supports sustainable agricultural practices through an interactive Streamlit-based web application.

---

# Problem Statement

Agriculture accounts for a significant portion of global freshwater consumption. Traditional irrigation practices often result in excessive water usage due to the lack of data-driven decision-making.

Farmers require an intelligent solution capable of:

- Predicting irrigation requirements accurately
- Optimizing water consumption
- Improving crop productivity
- Supporting sustainable farming practices
- Simplifying irrigation planning

---

# Objectives

- Predict irrigation requirements using Machine Learning.
- Assist farmers in optimizing water usage.
- Analyze crop and soil conditions for better recommendations.
- Provide an easy-to-use web interface for irrigation prediction.
- Encourage sustainable and precision agriculture.

---

# Proposed Solution

Croply utilizes a Random Forest Machine Learning model trained on agricultural data to predict irrigation requirements.

The application processes user inputs related to crop type, soil conditions, fertilizer composition, and environmental parameters. After preprocessing and feature encoding, the trained model predicts the irrigation requirement and presents the result through an interactive Streamlit dashboard.

---

# Key Features

## Irrigation Prediction

- AI-based irrigation requirement prediction
- Crop-specific recommendations
- Water optimization support

## Agricultural Analysis

- Crop information analysis
- Soil condition evaluation
- Fertilizer parameter analysis
- Environmental factor assessment

## Machine Learning

- Data preprocessing
- Feature encoding
- Random Forest Classification
- Model serialization using Joblib

## User Interface

- Interactive Streamlit dashboard
- Simple prediction workflow
- Knowledge Hub for farmers
- Responsive user experience

---

# System Architecture

```text
                 User Input
                      │
                      ▼
             Data Validation
                      │
                      ▼
          Data Preprocessing
                      │
                      ▼
          Feature Engineering
                      │
                      ▼
          Random Forest Model
                      │
                      ▼
        Irrigation Prediction
                      │
                      ▼
       Streamlit Web Dashboard
```

---

# Machine Learning Workflow

```text
Agricultural Dataset
         │
         ▼
Data Cleaning
         │
         ▼
Feature Encoding
         │
         ▼
Feature Selection
         │
         ▼
Train-Test Split
         │
         ▼
Random Forest Training
         │
         ▼
Model Evaluation
         │
         ▼
Model Serialization
         │
         ▼
Streamlit Deployment
```

---

# Input Parameters

The prediction model considers multiple agricultural parameters, including:

- Crop Type
- Soil Type
- Soil Moisture
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Rainfall
- Irrigation Method
- Farm Area (if applicable)

---

# Output

The application generates:

- Irrigation Requirement Prediction
- Water Requirement Recommendation
- Crop-based Irrigation Guidance
- Sustainable Irrigation Insights

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Framework | Streamlit |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Algorithm | Random Forest |
| Model Persistence | Joblib |
| Frontend | HTML, CSS |
| Version Control | Git, GitHub |

---

# Model Information

| Attribute | Value |
|-----------|-------|
| Learning Type | Supervised Learning |
| Algorithm | Random Forest |
| Feature Encoding | Label Encoding |
| Data Preprocessing | Pandas |
| Model Serialization | Joblib |

> Include model evaluation metrics such as Accuracy, Precision, Recall, and F1-Score if available.

---

# Project Structure

```text
Croply-Smart-Irrigation-Advisor/
│
├── Home.py
├── backend.py
├── train_irrigation_model.py
├── pages/
├── models/
│   └── *.pkl
├── dataset/
│   └── crop_data.csv
├── style.css
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/shreyaberlikar/Croply-Smart-Irrigation-Advisor.git
```

Navigate to the project directory

```bash
cd Croply-Smart-Irrigation-Advisor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run Home.py
```

---

# Applications

- Precision Agriculture
- Smart Irrigation Planning
- Water Resource Optimization
- Sustainable Farming
- Agricultural Decision Support
- Crop Management

---

# Future Enhancements

- Real-time Weather API integration
- IoT-based soil moisture sensor integration
- AI-powered agricultural chatbot
- Multi-language support
- Mobile application
- Satellite and remote sensing integration
- Crop disease detection module
- Fertilizer recommendation system

---

# Author

**Shreya Berlikar**

Computer Engineering Student | AI & Machine Learning Enthusiast

**GitHub:** https://github.com/shreyaberlikar

**LinkedIn:** https://www.linkedin.com/in/shreyaberlikar

---

# License

This project is developed for educational and research purposes.
