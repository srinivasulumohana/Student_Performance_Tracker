# Student_Performance_Tracker
COMPANY : CODTECH IT SOLUTIONS PVT.LTD
NAME : Mohana Srinivasulu
INTERN ID : CITS1567
DOMAIN : Machine Learning 
DURATION : 6 Weeks
MENTOR : Neela Santhosh Kumar

🎓 Student Performance Tracker using Machine Learning
📌 Project Overview

The Student Performance Tracker is a complete end-to-end Machine Learning project developed using Python and Streamlit to analyze and predict student academic performance. The project demonstrates the practical implementation of Data Science and Machine Learning concepts using a real-world educational dataset. The system is designed to help analyze various factors affecting student performance and predict student average scores using Machine Learning algorithms.

The project uses the “Students Performance in Exams” dataset from Kaggle, which contains information related to student demographics, parental education, lunch type, test preparation course completion, and subject-wise marks. Using this dataset, the project performs data cleaning, preprocessing, exploratory data analysis, visualization, model training, prediction, and dashboard development.

This project is especially useful for beginners and students learning Data Science, Artificial Intelligence, and Machine Learning because it demonstrates the complete workflow of a real-world Machine Learning application.

📖 Introduction

Educational institutions generate a large amount of student-related data every year. Analyzing this data manually becomes difficult and time-consuming. Educational organizations require intelligent systems that can analyze academic data, identify performance patterns, and predict student outcomes accurately.

The Student Performance Tracker solves this problem by implementing Machine Learning techniques that can automatically predict student academic performance based on multiple input factors. The system also provides meaningful visual insights that help understand relationships between different educational variables.

The project combines Machine Learning, Data Visualization, and Dashboard Development into a single integrated application. It provides practical experience in working with real-world datasets and helps understand the importance of predictive analytics in the education sector.

🎯 Objectives of the Project

The major objectives of the project are:

To understand the complete Machine Learning lifecycle
To work with real-world educational datasets
To perform data preprocessing and cleaning
To analyze student performance trends using EDA
To build prediction models using Machine Learning algorithms
To evaluate model performance using standard evaluation metrics
To develop an interactive dashboard using Streamlit
To gain practical knowledge in Data Science and Machine Learning
❓ Problem Statement

Educational institutions often struggle to monitor and evaluate student academic performance efficiently. Manual analysis of student records becomes challenging as the amount of data increases. Identifying weak students and understanding factors affecting performance require intelligent systems that can analyze and predict student outcomes automatically.

The Student Performance Tracker addresses this issue by developing a Machine Learning-based prediction system capable of analyzing student information and predicting average academic scores. The project also helps identify factors that significantly influence student performance such as mathematics score, parental education level, and test preparation completion.

📂 Dataset Information

The project uses the “Students Performance in Exams” dataset downloaded from Kaggle. The dataset contains information about student demographics and subject scores.

The dataset includes the following features:

Gender of the student
Race/Ethnicity group
Parental level of education
Lunch type
Test preparation course status
Mathematics score
Reading score
Writing score

The dataset was stored in CSV format and loaded into Python using the Pandas library for preprocessing and analysis.

🛠 Technologies Used

The project was developed using the following technologies and tools:

Python
Visual Studio Code
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Joblib

Python was used as the programming language for implementing the entire project. Pandas and NumPy were used for data manipulation and preprocessing. Matplotlib and Seaborn were used for data visualization and exploratory data analysis. Scikit-learn was used for implementing Machine Learning algorithms and evaluation metrics. Streamlit was used to build an interactive web dashboard. Joblib was used for saving and loading the trained Machine Learning model.

⚙️ Project Workflow

The Student Performance Tracker follows a complete Machine Learning workflow consisting of multiple stages including data collection, preprocessing, exploratory data analysis, model training, prediction, and dashboard development.

1️⃣ Data Collection

The dataset was downloaded from Kaggle in CSV format. The dataset contains information about students and their examination scores. The CSV file was loaded into Python using Pandas for further analysis and preprocessing.

2️⃣ Data Cleaning

Data cleaning is one of the most important stages of any Machine Learning project. Several preprocessing operations were performed to improve data quality and prepare the dataset for Machine Learning algorithms.

The dataset was checked for missing values, duplicate rows, and inconsistent data. Missing values were handled using statistical techniques such as mean and mode replacement. Duplicate records were removed to avoid repeated information that could affect model accuracy.

Categorical columns such as gender, lunch type, and test preparation course were encoded into numerical format using Label Encoding because Machine Learning algorithms cannot process raw textual data directly.

3️⃣ Feature Engineering

A new feature called “average_score” was created by calculating the average of mathematics, reading, and writing scores. This feature acts as the target variable for prediction.

Feature engineering helps improve the predictive capability of Machine Learning models and creates more meaningful information from raw data.

4️⃣ Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset more effectively and identify hidden patterns and relationships among variables.

Several visualizations were created using Matplotlib and Seaborn, including:

Histograms
Scatterplots
Correlation Heatmaps
Boxplots

Histograms were used to analyze the distribution of student scores. Scatterplots helped identify relationships between subject scores. Correlation heatmaps showed relationships between features and helped identify highly correlated variables. Boxplots were used to compare student performance across different categories.

EDA provided several important insights regarding student performance and academic trends.

📊 Insights from EDA

Several meaningful observations were identified during analysis:

Reading and writing scores are highly correlated
Students completing test preparation courses perform better
Mathematics score strongly affects overall average performance
Parent education level influences student academic scores
Some student groups consistently achieve higher performance

These insights help better understand the factors affecting student academic success.

5️⃣ Machine Learning Model Development

The project implements Machine Learning algorithms for predicting student average performance scores.

Initially multiple Machine Learning models were considered, including:

Linear Regression
Decision Tree Regressor
Random Forest Regressor

Among these models, the Random Forest Regressor provided the best prediction accuracy and performance.

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

The dataset was divided into training and testing sets using train_test_split from Scikit-learn. The model was trained using training data and evaluated using testing data.

📈 Model Evaluation

The model performance was evaluated using standard Machine Learning evaluation metrics:

RMSE (Root Mean Square Error)
R² Score

RMSE measures prediction error. Lower RMSE values indicate better model performance.

R² Score measures prediction accuracy. Values closer to 1 indicate excellent prediction capability.

The Random Forest model achieved excellent performance with:

RMSE ≈ 1.17
R² Score ≈ 0.99

These results indicate that the model predicts student performance with very high accuracy.

🤖 Prediction System

The project includes a prediction system where users can input student details such as:

Gender
Race/Ethnicity Group
Parent Education Level
Lunch Type
Test Preparation Status
Mathematics Score
Reading Score
Writing Score

The trained Machine Learning model predicts the student average performance score based on the provided input values.

The prediction system demonstrates practical implementation of Machine Learning in educational analytics.

🌐 Streamlit Dashboard

An interactive dashboard was developed using Streamlit to convert the Machine Learning project into a professional web application.

The dashboard provides an easy-to-use interface where users can:

View dataset preview
Analyze statistical summaries
Explore visualizations
Predict student performance
Interact with the Machine Learning system

The dashboard includes interactive components such as sliders, dropdown menus, buttons, charts, and input fields to improve usability and user experience.

📊 Dashboard Features

The Streamlit dashboard includes the following features:

Dataset Preview
Statistical Summary
Average Score Distribution Graph
Correlation Heatmap
Interactive Prediction Form
Real-Time Student Score Prediction
Project Insights

The dashboard transforms the Machine Learning model into a practical and user-friendly application.

💡 Advantages of the Project

The Student Performance Tracker provides several advantages:

Easy-to-use interface
High prediction accuracy
Real-world educational analysis
Interactive visualizations
Practical implementation of Machine Learning
Beginner-friendly project structure
Useful for academic analytics

The project demonstrates how Machine Learning can improve educational analysis and assist institutions in monitoring student performance effectively.

⚠️ Limitations of the Project

Although the project performs well, it has some limitations:

The dataset size is limited
Predictions depend only on available features
Real-world academic performance may depend on additional factors such as attendance, stress, extracurricular activities, health conditions, and family environment

Future versions of the project can include additional features and larger datasets to improve prediction capability further.

🚀 Future Enhancements

Several future improvements can be implemented in this project:

Deep Learning integration
Database connectivity
User authentication system
Cloud deployment
Mobile application development
Student report generation
Multiple Machine Learning model comparison
Real-time analytics
CSV upload support

These enhancements can make the system more scalable and production-ready.

🧠 Learning Outcomes

This project provides practical understanding of:

Data Cleaning
Data Preprocessing
Feature Engineering
Exploratory Data Analysis
Data Visualization
Machine Learning Algorithms
Model Evaluation
Prediction Systems
Dashboard Development using Streamlit
End-to-End Machine Learning Workflow

The project helps students understand how Machine Learning applications are developed in real-world scenarios.

📌 Applications of the Project

The Student Performance Tracker can be used in:

Schools
Colleges
Educational institutions
Academic monitoring systems
Educational analytics platforms
Data Science learning projects
Machine Learning portfolio projects

The project demonstrates practical application of Machine Learning in the education sector.

📚 Conclusion

The Student Performance Tracker successfully demonstrates how Machine Learning can be applied in the education domain to analyze and predict student academic performance. The project integrates data preprocessing, visualization, Machine Learning modeling, prediction systems, and dashboard deployment into a single application.

The Random Forest model achieved excellent prediction accuracy, making the system reliable for educational analytics and academic performance prediction. The Streamlit dashboard further improves usability by providing an interactive interface for visualization and prediction.

Overall, this project serves as a complete real-world Machine Learning application and provides valuable practical experience in Data Science, Machine Learning, and Dashboard Development using Python and Streamlit.


