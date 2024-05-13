# heart-disease-prediction
machine learning project to predict heart disease
Project Description:

This project aims to develop a machine learning-based predictive model for heart disease classification using a dataset obtained from Kaggle. The dataset comprises various health indicators and risk factors associated with heart disease, such as age, gender, blood pressure, cholesterol levels, and more.

The project follows a structured approach starting with exploratory data analysis (EDA) to understand the dataset's characteristics, including data distribution, missing values, and outlier detection. Exploratory data analysis techniques such as histograms, bar charts, pair plots, and correlation matrices are employed to gain insights into the relationships between different variables.

Subsequently, data preprocessing steps are applied, including handling missing values, outlier detection, and feature standardization, to prepare the dataset for model training. The dataset is then split into training and testing sets, and various classification algorithms are trained and evaluated for their performance in classifying individuals as either having or not having heart disease.

The trained model with the highest accuracy, determined through rigorous evaluation, is selected for deployment. The selected model, a Naive Bayes classifier, is serialized and saved using the pickle library. A web application using Streamlit is developed to allow users to input their health information and obtain predictions regarding their likelihood of having heart disease based on the trained model.

Overall, this project demonstrates the application of machine learning techniques in healthcare for predictive analytics, aiming to assist healthcare professionals in early detection and prevention of heart disease. The project's codebase, dataset, and documentation are hosted on GitHub for accessibility and collaboration.
