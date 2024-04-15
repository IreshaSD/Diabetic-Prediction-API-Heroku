# Diabetic-Prediction-API-Heroku
This repository contains code to deploy a machine learning model for diabetes prediction as an API on Heroku. The API is built using FastAPI in Python.

Model Description

The machine learning model used in this API is trained to predict the likelihood of a person having diabetes based on various input features such as:

Pregnancies
Glucose level
Blood pressure
Skin thickness
Insulin level
BMI (Body Mass Index)
Diabetes Pedigree Function
Age

Usage:

To use the API, send a POST request to the /diabetes_prediction endpoint with JSON data containing the input features. The API will return a prediction indicating whether the person is diabetic or not.

Key Features:

FastAPI Framework: Leverages the flexibility and performance of FastAPI for building the API.

Diabetes Prediction Model: Utilizes a pre-trained model to analyze user-provided data and predict diabetes risk.

User Input: Users can interact with the API by sending data through a POST request to the /diabetes_prediction endpoint.

CORS Support: The API includes CORS (Cross-Origin Resource Sharing) configuration to enable requests from different origins (adjustable in the origins list).

Heroku Deployment: Designed for easy deployment on Heroku, a cloud platform for web applications.
