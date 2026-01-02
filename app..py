import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Food Waste Analytics & Insights",
    layout="wide"
)

st.title("🥗🍔 Global Food Waste Analytics & Insights")
st.caption("From data to insights → prediction → real-world action")


df = pd.read_csv("global_food_waste.csv")


df["Waste per Million Population"] = (
    df["Total Waste (Thousand Tonnes)"] / df["Population (Million)"]
)

# SIDEBAR FILTERS

st.sidebar.header("🎛️ Filters")

years = st.sidebar.multiselect(
    "Select Year(s)",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

countries = st.sidebar.multiselect(
    "Select Country(s)",
    sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

filtered_df = df[
    (df["Year"].isin(years)) &
    (df["Country"].isin(countries))
]

# RISK SCORING MODEL (PREDICTION)
country_summary = df.groupby("Country").agg({
    "Total Waste (Thousand Tonnes)": "sum",
    "Waste per Million Population": "mean",
    "Economic Loss (Million USD)": "sum"
}).reset_index()

# Normalize (0–1 scale)
for col in [
    "Total Waste (Thousand Tonnes)",
    "Waste per Million Population",
    "Economic Loss (Million USD)"
]:
    country_summary[col + "_norm"] = (
        country_summary[col] - country_summary[col].min()
    ) / (country_summary[col].max() - country_summary[col].min())

# Risk Score
country_summary["Risk Score"] = (
    0.4 * country_summary["Total Waste (Thousand Tonnes)_norm"] +
    0.4 * country_summary["Waste per Million Population_norm"] +
    0.2 * country_summary["Economic Loss (Million USD)_norm"]
)

# Risk Level
country_summary["Risk Level"] = pd.qcut(
    country_summary["Risk Score"],
    q=[0, 0.3, 0.7, 1],
    labels=["Low Priority", "Medium Priority", "High Priority"]
)


# TABS

tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📄 Dataset",
    "📅 Year-wise Analysis",
    "🌍 Country Insights",
    "💰 Economic Impact",
    "🍎 Food Categories",
    "🧠 Risk Prediction",
    "✅ Recommendations"
])
# TAB 0: DATASET

with tab0:
    st.header("📄 Dataset Overview")
    st.dataframe(df.head(10))

    st.info("""
    **What we understand from this:**
    - The dataset includes country, year, food category, waste amount,
      economic loss, and population.
    - These variables help analyze food waste from multiple perspectives.
    """)
# TAB 1: YEAR-WISE ANALYSIS

with tab1:
    st.header("📅 Year-wise Global Food Waste Trend")

    yearly_waste = filtered_df.groupby("Year")["Total Waste (Thousand Tonnes)"].sum()

    fig, ax = plt.subplots()
    ax.plot(yearly_waste.index, yearly_waste.values, marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("Waste (Thousand Tonnes)")
    st.pyplot(fig)

    st.info("""
    **What we understand from this:**
    - Food waste is not constant across years.
    - Certain years show spikes due to changes in consumption and supply chains.
    """)

# TAB 2: COUNTRY INSIGHTS

with tab2:
    st.header("🌍 Country-Level Food Waste Insights")

    country_waste = filtered_df.groupby("Country")["Total Waste (Thousand Tonnes)"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))
    country_waste.sort_values(ascending=False).head(10).plot(kind="bar", ax=ax)
    ax.set_ylabel("Waste (Thousand Tonnes)")
    st.pyplot(fig)

    st.info("""
    **What we understand from this:**
    - A small number of countries contribute most of the food waste.
    - These countries need focused waste management strategies.
    """)

    st.subheader("🌍 Waste per Million Population")

    per_capita = filtered_df.groupby("Country")["Waste per Million Population"].mean()
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    per_capita.sort_values(ascending=False).head(10).plot(kind="barh", ax=ax2)
    ax2.set_xlabel("Waste per Million Population")
    st.pyplot(fig2)

# TAB 3: ECONOMIC IMPACT

with tab3:
    st.header("💰 Economic Impact of Food Waste")

    loss_by_country = filtered_df.groupby("Country")["Economic Loss (Million USD)"].sum()

    fig, ax = plt.subplots(figsize=(10, 5))
    loss_by_country.sort_values(ascending=False).head(10).plot(
        kind="bar", ax=ax, color="red"
    )
    ax.set_ylabel("Economic Loss (Million USD)")
    st.pyplot(fig)

    st.warning("""
    **What we understand from this:**
    - Food waste causes massive financial losses.
    - Reducing waste can redirect funds to healthcare, education, and food security.
    """)

# TAB 4: FOOD CATEGORIES
with tab4:
    st.header("🍎 Food Category Waste Distribution")

    category_waste = filtered_df.groupby("Food Category")["Total Waste (Thousand Tonnes)"].sum()

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        category_waste,
        labels=category_waste.index,
        autopct="%1.1f%%",
        startangle=90
    )
    st.pyplot(fig)

    st.info("""
    **What we understand from this:**
    - Perishable food categories dominate waste.
    - Shelf life and storage are major contributors to wastage.
    """)

# TAB 5: RISK PREDICTION

with tab5:
    st.header("🧠 Food Waste Risk Prediction Model")

    fig, ax = plt.subplots(figsize=(10, 5))
    country_summary.sort_values("Risk Score", ascending=False).head(10).plot(
        x="Country",
        y="Risk Score",
        kind="bar",
        ax=ax,
        color="orange"
    )
    ax.set_ylabel("Risk Score")
    st.pyplot(fig)

    st.info("""
    **What we understand from this:**
    - Countries with high waste, high per-capita waste,
      and high economic loss need urgent intervention.
    - This risk model helps prioritize food waste management.
    """)

# TAB 6: RECOMMENDATIONS
with tab6:
    st.header("✅ Country-Specific Recommendations")

    selected_country = st.selectbox(
        "Select Country",
        country_summary["Country"].sort_values()
    )

    row = country_summary[country_summary["Country"] == selected_country].iloc[0]

    st.subheader(f"🌍 {selected_country}")
    st.write(f"**Risk Level:** {row['Risk Level']}")
    st.write(f"**Risk Score:** {row['Risk Score']:.2f}")

    if row["Risk Level"] == "High Priority":
        st.error("""
        🔴 **Urgent Action Required**
        - National food waste tracking systems
        - Improve cold storage and logistics
        - Mandatory food donation policies
        - Public awareness campaigns
        """)
    elif row["Risk Level"] == "Medium Priority":
        st.warning("""
        🟡 **Moderate Action Required**
        - Improve household food planning
        - Reduce retail-level wastage
        - Promote better packaging solutions
        """)
    else:
        st.success("""
        🟢 **Maintain & Optimize**
        - Continue efficient practices
        - Invest in food preservation technology
        - Promote sustainability education
        """)

    st.info("""
    **What we understand from this:**
    - Food waste management must be country-specific.
    - Data-driven recommendations lead to better policies.
    """)


# DOWNLOAD OPTION

st.sidebar.download_button(
    "⬇️ Download Filtered Data",
    filtered_df.to_csv(index=False),
    "filtered_food_waste_data.csv",
    "text/csv"
)

