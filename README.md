🥤🥗🍔🍗🍟🥓Global Food Waste Analytics & Insights

A data-driven case study that analyzes global food waste patterns using Python, Pandas, NumPy, Matplotlib, and Streamlit, and provides country-level insights, risk prediction, and actionable recommendations.

📌 Project Overview

Food waste is a serious global issue that impacts food security, economy, and sustainability.
This project transforms raw food waste data into meaningful insights and a decision-support dashboard.

The dashboard helps to:

Understand where and why food waste occurs

Compare countries and food categories

Identify high-risk countries

Provide real-world recommendations

🎯 Objectives of the Study :

🌍 Country-Level Insights

Identify countries generating the highest food waste

Analyze waste per million population

Compare food waste across countries

🍎 Category-Level Insights

Identify most wasted food categories

Analyze category-wise contribution to total waste

📅 Time-Based Insights

Year-wise global food waste trend

Identify increasing or decreasing waste patterns

🧠 Predictive Insight

Predict which countries need urgent food waste management

Classify countries into Low, Medium, High priority

🛠️ Tech Stack Used
Tool	Purpose
Python	Core programming
Pandas	Data cleaning & analysis
NumPy	Numerical operations
Matplotlib	Data visualization
Streamlit	Interactive dashboard

Google colab notebook : 
https://colab.research.google.com/drive/1yiI8J6ewxZaflRQgP0XGMnoE1E1iThHf?usp=sharing

📂 Dataset Description
The dataset contains food waste information across countries and years.

Key Columns:

Country

Year

Food Category

Total Waste (Thousand Tonnes)

Economic Loss (Million USD)

Population (Million)

Derived Column:

Waste per Million Population

📊 Dashboard Features :

📄 Dataset Overview

Preview raw data

Understand dataset structure

📅 Year-wise Analysis

Line chart showing global food waste trend

Identify peak and low waste years

🌍 Country Insights

Top waste-generating countries

Waste per million population comparison

💰 Economic Impact

Country-wise economic loss due to food waste

🍎 Food Category Insights

Pie chart of category-wise food waste contribution

🧠 Risk Prediction Model

Rule-based risk scoring using:

Total waste

Per-capita waste

Economic loss

Countries classified as:

Low Priority

Medium Priority

High Priority

✅ Country-Specific Recommendations

Recommendations change based on selected country

Practical, real-world food waste reduction strategies

📈 Risk Scoring Logic (Simple & Explainable)
Risk Score =
0.4 × Total Waste (normalized)
+ 0.4 × Waste per Million Population (normalized)
+ 0.2 × Economic Loss (normalized)


This helps identify countries requiring immediate food waste management.

💡 Key Insights

A small number of countries contribute most of the food waste

Perishable food categories dominate global waste

Food waste leads to massive economic losses

Targeted interventions can significantly reduce waste

🌱 Real-World Recommendations

High Priority Countries

Improve cold storage & supply chain efficiency

Implement national food waste monitoring systems

Encourage food donation & redistribution

Run public awareness campaigns

Medium Priority Countries

Promote household food planning

Reduce retail-level waste

Improve packaging solutions

Low Priority Countries

Maintain current best practices

Invest in food preservation technology

Promote sustainability education

▶️ How to Run the Project

1️⃣ Install Dependencies
pip install streamlit pandas numpy matplotlib

2️⃣ Run the App
streamlit run app..py

📥 Download Feature

Users can download filtered data directly from the dashboard for further analysis.

🧠 Learning Outcomes

Hands-on experience with Pandas & NumPy

Real-world data storytelling

Building interactive dashboards using Streamlit

Understanding how data supports policy decisions

🚀 Future Enhancements

Add machine learning models for prediction

Deploy dashboard on Streamlit Cloud

Integrate real-time data sources

Add CO₂ impact estimation of food waste

⭐ If you find this project useful, consider giving it a star on GitHub! ⭐