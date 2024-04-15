# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 05:22:06 2024

@author:Iresha Sandamali
"""

# The main idea of deploying machine learning model in the form of API is that it will be easier for us to connect our UI
# The final result that we get from the API is URL
# Public API in the sense , Anyone on the internet can access the our API through URL. And they can use it for their purpose
# Once we deploy this model as this  public API so we get a URL. And anyone can post this input features to this API in order to find whether a person is diabetec or not   
# ngrok module is used in order to create a proxy URL for us. 
# For creating API we will be using fastapi library


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction :  float
    Age : int
    

# loading the saved model
diabetes_model = pickle.load(open('Diabetes_Pipeline.sav','rb'))


@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']


    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'The person is not Diabetic'
    
    else:
        return 'The person is Diabetic'
