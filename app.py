# =========================================
# STUDENT PERFORMANCE TRACKER DASHBOARD
# STREAMLIT PROJECT
# =========================================

# =========================================
# IMPORT LIBRARIES
# =========================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

# =========================================
# PAGE CONFIGURATION
# =========================================

st.set_page_config(
    page_title="Student Performance Tracker",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("🎓 Student Performance Tracker")

st.write(
    "Machine Learning Dashboard using Random Forest"
)

# =========================================
# FILE PATHS
# =========================================

DATA_PATH = r"C:\Users\arunt\Downloads\cleaned_students.csv"

MODEL_PATH = r"C:\Users\arunt\Downloads\random_forest_model.pkl"

# =========================================
# CHECK FILES EXIST
# =========================================

if not os.path.exists(DATA_PATH):

    st.error(
        "Cleaned dataset file not found!"
    )

    st.stop()

if not os.path.exists(MODEL_PATH):

    st.error(
        "Model file not found!"
    )

    st.stop()

# =========================================
# LOAD DATASET
# =========================================

try:

    df = pd.read_csv(DATA_PATH)

    st.success("Dataset Loaded Successfully!")

except Exception as e:

    st.error(f"Error Loading Dataset: {e}")

    st.stop()

# =========================================
# LOAD MODEL
# =========================================

try:

    model = joblib.load(MODEL_PATH)

    st.success("Model Loaded Successfully!")

except Exception as e:

    st.error(f"Error Loading Model: {e}")

    st.stop()

# =========================================
# DATASET PREVIEW
# =========================================

st.header("📊 Dataset Preview")

st.dataframe(df.head())

# =========================================
# DATASET STATISTICS
# =========================================

st.header("📈 Dataset Statistics")

st.write(df.describe())

# =========================================
# SCORE DISTRIBUTION GRAPH
# =========================================

st.header("📉 Average Score Distribution")

try:

    fig1, ax1 = plt.subplots(figsize=(10, 5))

    sns.histplot(
        df['average_score'],
        kde=True,
        ax=ax1
    )

    ax1.set_title(
        "Distribution of Average Scores"
    )

    st.pyplot(fig1)

except Exception as e:

    st.error(f"Error Creating Histogram: {e}")

# =========================================
# CORRELATION HEATMAP
# =========================================

st.header("🔥 Correlation Heatmap")

try:

    fig2, ax2 = plt.subplots(figsize=(12, 8))

    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        cmap='coolwarm',
        ax=ax2
    )

    ax2.set_title("Correlation Heatmap")

    st.pyplot(fig2)

except Exception as e:

    st.error(f"Error Creating Heatmap: {e}")

# =========================================
# PREDICTION SECTION
# =========================================

st.header("🤖 Predict Student Performance")

# =========================================
# INPUT COLUMNS
# =========================================

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    race = st.number_input(
        "Race/Ethnicity Group",
        min_value=0,
        max_value=5,
        value=2
    )

    education = st.number_input(
        "Parent Education Level",
        min_value=0,
        max_value=5,
        value=3
    )

    lunch = st.selectbox(
        "Lunch Type",
        ["Free", "Standard"]
    )

with col2:

    test_prep = st.selectbox(
        "Test Preparation Completed",
        ["No", "Yes"]
    )

    math_score = st.slider(
        "Math Score",
        0,
        100,
        80
    )

    reading_score = st.slider(
        "Reading Score",
        0,
        100,
        85
    )

    writing_score = st.slider(
        "Writing Score",
        0,
        100,
        90
    )

# =========================================
# ENCODE INPUT VALUES
# =========================================

gender_value = 1 if gender == "Male" else 0

lunch_value = 1 if lunch == "Standard" else 0

test_prep_value = 1 if test_prep == "Yes" else 0

# =========================================
# CREATE INPUT DATAFRAME
# =========================================

input_data = pd.DataFrame([{

    'gender': gender_value,

    'race/ethnicity': race,

    'parental level of education': education,

    'lunch': lunch_value,

    'test preparation course': test_prep_value,

    'math score': math_score,

    'reading score': reading_score,

    'writing score': writing_score

}])

# =========================================
# PREDICTION BUTTON
# =========================================

if st.button("Predict Performance"):

    try:

        prediction = model.predict(input_data)

        st.success(
            f"🎯 Predicted Average Score: "
            f"{prediction[0]:.2f}"
        )

    except Exception as e:

        st.error(f"Prediction Error: {e}")

# =========================================
# PROJECT INSIGHTS
# =========================================

st.header("💡 Project Insights")

st.write(
    "- Reading and writing scores are highly correlated"
)

st.write(
    "- Random Forest gives high prediction accuracy"
)

st.write(
    "- Student preparation improves performance"
)

st.write(
    "- Math score strongly affects final score"
)

# =========================================
# FOOTER
# =========================================

st.write("---")

st.write(
    "✅ Student Performance Tracker using "
    "Python, Machine Learning, and Streamlit"
)