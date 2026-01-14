📌 Overview

Debt Stress Radar™ is an AI-based decision-support system that identifies early signs of financial stress in borrowers before defaults occur.

The system predicts a Debt Stress Score (0–100) using income and debt patterns, visualizes risk through a radar / gauge dashboard, and explains why the risk exists using explainable AI (SHAP).

It is designed to be:

Visual and intuitive

Explainable (non-black-box)

Advisor-friendly

Product-grade (not a chatbot)

❓ Problem Statement

Borrowers usually realize financial trouble too late, after:

EMI defaults

Credit score drops

Legal or recovery notices

Most systems focus on post-failure detection, not early prevention.
There is a need for a transparent, proactive, and explainable way to detect early debt stress.

💡 Solution

Debt Stress Radar™ acts as an early warning system by:

Analyzing income, expenses, EMIs, credit usage, and loan structure

Predicting a continuous Debt Stress Score

Mapping the score into clear risk zones

Explaining key risk drivers using SHAP

Presenting insights through a clean visual dashboard

The system supports decision-making and does not replace human advisors.

⚙️ How It Works
Financial Inputs
      ↓
Feature Engineering (Ratios & Indicators)
      ↓
Regression ML Model
      ↓
Debt Stress Score (0–100)
      ↓
Risk Zone Classification
      ↓
Explainable Insights & Suggested Solutions

🧠 Model & Approach
🔹 Model Used

RandomForestRegressor

🔹 Why Regression?

Produces a continuous stress score

Suitable for gauge / radar visualization

Risk zones are derived using transparent thresholds

Improves interpretability and business control

📊 Features Used

The model is trained using the following features:

monthly_income

fixed_expenses

total_emi

credit_card_outstanding

avg_interest_rate

active_loans

emi_income_ratio

expense_ratio

credit_utilization

interest_burden

loan_density

These features reflect real financial risk indicators commonly used by CAs and financial analysts.

📈 Model Performance

R² Score: ~0.90
Mean Absolute Error (MAE): ~3 points
This indicates strong generalization and reliable stress estimation for an MVP-level financial risk system.

🔍 Explainability (SHAP)

The system uses SHAP (SHapley Additive exPlanations) to explain predictions.

Key Risk Drivers Identified:
EMI-to-Income Ratio
Credit Utilization
Number of Active Loans
This ensures the model is interpretable, transparent, and audit-friendly.

🚦 Risk Zones
Zone	Description
🟢 Safe	Financially stable
🟡 Watch	Early stress signals detected
🔴 Critical	High risk of financial stress

Risk zones are derived using rule-based thresholds, not black-box classification.

🖥️ User Interface

The Streamlit dashboard includes:
Radar / gauge visualization
Single Debt Stress Score
Color-coded risk zones
Clear explanation of risk drivers
Neutral recommended solutions

The UI is:
Visual-first
Minimal
Professional
Non-chatbot

🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Machine Learning	scikit-learn
Explainability	SHAP
Visualization	Plotly
Backend	Python
Model Storage	joblib

📂 Project Structure
debt-stress-radar/
│
├── app.py
├── debt_stress_radar_model.pkl
├── requirements.txt
└── README.md

⚠️ Disclaimer

This tool provides decision support only.
It does not offer financial advice, guarantees, or recommendations.
Final decisions should always involve a qualified financial professional.

👤 Author

Vinit Limkar
© 2026 — All rights reserved

⭐ Final Note

This project demonstrates:
Real ML usage (not rule-based or hardcoded)
Explainable AI in finance
Product-grade UI thinking
Internship-ready engineering practices