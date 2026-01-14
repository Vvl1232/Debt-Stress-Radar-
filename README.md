📌 Overview

Debt Stress Radar™ is a decision support system based on artificial intelligence, designed to give early warning signs of financial stress to borrowers before defaults.
It generates a Debt Stress Score (0-100) from income and debt patterns, visualizes risk on a user dashboard with radar / gauge and explains the reason for the risk using explainable AI (SHAP).

So that it can be:
Visual and intuitive
Explainable (non-black-box)
Advisor-friendly
Product-grade (not a chatbot)

❓ Problem Statement
Most of the times borrowers realize their financial difficulties too late after:
EMI defaults.
Credit score drop occurs.
Legal or recovery notices arrive.

Almost all of the systems are directed towards post-failure detection rather than pre-outlying prevention. It needs to be clear-headed, proactive, and explainable - a way of interpreting early debt stress.

💡 Solution
Debt Stress Radar™ acts as early alert for:
Monitoring incomes, expenses, EMIs, credit usage, and loan structure
Showing a constant Debt Stress Score.
Plotting the score into clear-risk areas.
Explaining key risk drivers using SHAP.
Showing insights through a clean visual dashboard.
The system will help us make a decision not substitute human advisors.

⚙️ How It Works Financial inputs ↓ Feature Engineering (Ratios & Indicators) ↓ Regression ML Model ↓ Debt Stress Score (0-100) ↓ Risk Zone Classification ↓ Explainable Insights & Suggested Solutions

🧠 Model & Approach
🔹 Model Used
RandomForestRegressor

🔹 Why Regression?
Gives continuous stress score
supports gauge / radar visualization
generates risk zones through transparent thresholds
enhances interpretability and business control

📊 Features Used
The model uses the following features for training:
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

Since its really very minimal
R² Score: ~0.90
Mean Absolute Error (MAE): ~3 points
This indicates strong generalization and reliable stress estimation for an MVP-level financial risk system.

Explainability (SHAP)
The system uses SHAP (SHapley Additive exPlanations) to explain predictions.

Key Risk Drivers Identified:

EMI-to-Income ratio
Credit Utilization
Number of Active Loans 
This will ensure interpretability for the model, transparency in asacy as well as audit friendly. 

Risk Zones 
Zone Description
  Safe 🟢  Financially stable 
  Watch 🟡  Signals early stress detected 
  Critical 🔴  Financial tension is highly probable 

Risk Zones are derived through rule based thresholds, not black-box classification. 

User Interface 

This Streamlit dashboard has included: 
Radar / gauge Visualization 
Single Debt Stress Score 
Color-coded Risk Zones Clear Explanation Of Risk Drivers Neutral Recommended Solutions 

The UI is: 
Visual-first 
Minimal 
Professional 
Non-chatbot 

Tech Stack 
Layer Technology 
Frontend Streamlit 
Machine learning scikit-learn 
Explainability SHAP 
Visualization Plotly 
Backend Python 
Model Storage joblib 

Project Structure 
debt-stress-radar/ 
│ 
├── app.py 
├── debt_stress_radar_model.pkl 
├── requirements.txt 
└── README.md 

Disclaimer 
This is only intended to give decision support. This does not give any financial advice, guarantees, or recommendations, and final decisions should always be made with the assistance of a qualified financial professional. 

Author 
Vinit Limkar 
- All Rights Reserved - 2026 

Final Note 
This project is a testament to: 
Real ML usage (not rule-based and hard scoring) 
Explainable AI in Finance 
Product-grade UI thinking 
Internship-ready engineering practices
