import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import joblib

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Debt Stress Radar™",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("debt_stress_radar_model.pkl")

# ---------------------------
# Helper Functions
# ---------------------------
def get_risk_zone(score):
    if score < 35:
        return "🟢 Safe"
    elif score < 65:
        return "🟡 Watch"
    else:
        return "🔴 Critical"

def gauge_chart(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        number={'suffix': " / 100"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'thickness': 0.25},
            'steps': [
                {'range': [0, 35], 'color': "#2ecc71"},
                {'range': [35, 65], 'color': "#f1c40f"},
                {'range': [65, 100], 'color': "#e74c3c"},
            ],
        },
        title={'text': "Debt Stress Score"}
    ))
    fig.update_layout(height=350)
    return fig

# ---------------------------
# Sidebar Inputs
# ---------------------------
st.sidebar.title("📥 Borrower Financial Inputs")

monthly_income = st.sidebar.number_input(
    "Monthly Income (₹)", min_value=20000, max_value=500000, value=60000
)

fixed_expenses = st.sidebar.number_input(
    "Fixed Expenses (₹)", min_value=5000, max_value=300000, value=25000
)

total_emi = st.sidebar.number_input(
    "Total EMI (₹)", min_value=0, max_value=300000, value=20000
)

credit_card_outstanding = st.sidebar.number_input(
    "Credit Card Outstanding (₹)", min_value=0, max_value=300000, value=15000
)

avg_interest_rate = st.sidebar.slider(
    "Average Interest Rate (%)", min_value=5.0, max_value=45.0, value=18.0
)

active_loans = st.sidebar.slider(
    "Active Loans", min_value=0, max_value=10, value=2
)

# ---------------------------
# Feature Engineering (MUST MATCH TRAINING)
# ---------------------------
emi_income_ratio = total_emi / max(monthly_income, 1)
expense_ratio = fixed_expenses / max(monthly_income, 1)
credit_utilization = credit_card_outstanding / max(monthly_income, 1)
interest_burden = avg_interest_rate / 100
loan_density = active_loans / max(monthly_income / 10000, 1)

X_input = pd.DataFrame([{
    "monthly_income": monthly_income,
    "fixed_expenses": fixed_expenses,
    "total_emi": total_emi,
    "credit_card_outstanding": credit_card_outstanding,
    "avg_interest_rate": avg_interest_rate,
    "active_loans": active_loans,
    "emi_income_ratio": emi_income_ratio,
    "expense_ratio": expense_ratio,
    "credit_utilization": credit_utilization,
    "interest_burden": interest_burden,
    "loan_density": loan_density
}])

# 🔒 Enforce correct column order
X_input = X_input[model.feature_names_in_]

# ---------------------------
# Prediction
# ---------------------------
score = model.predict(X_input)[0]
score = float(np.clip(score, 0, 100))
zone = get_risk_zone(score)

# ---------------------------
# Main Dashboard
# ---------------------------
st.title("📊 Debt Stress Radar™")
st.caption("AI-Powered Early Warning System for Indian Borrowers")

col1, col2 = st.columns([1.2, 1])

with col1:
    st.plotly_chart(gauge_chart(score), use_container_width=True)
    st.markdown(f"### Risk Zone: **{zone}**")

with col2:
    st.subheader("🔍 What’s Increasing Your Risk?")
    st.markdown("""
    - **High EMI burden** relative to income  
    - **Credit card utilization pressure**  
    - **Multiple active loans** increasing obligations  
    """)

    st.subheader("💡Recommended Solutions")
    if zone == "🟢 Safe":
        st.success(
            "Your debt profile is healthy. Maintain discipline and avoid unnecessary credit."
        )
    elif zone == "🟡 Watch":
        st.warning(
            "Early stress signals detected. Consider expense optimization or EMI restructuring."
        )
    else:
        st.error(
            "High financial stress detected. Debt consolidation or loan transfer is strongly recommended."
        )

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("⚠️ This tool provides decision support, not financial advice.")
st.caption("© 2026 Vinit Limkar. All rights reserved.")