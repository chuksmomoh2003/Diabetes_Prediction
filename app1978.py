#!/usr/bin/env python
# coding: utf-8

# In[1]:


from catboost import CatBoostClassifier
import streamlit as st
import pandas as pd
import joblib


# In[2]:


model_cat = joblib.load('Diabetes_model.pkl')

#@st.cache()

# defining the function which will make the prediction using the data which the user inputs 

def predict(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
    
    

        
    
    
    
    

        

 
 
        
        
    prediction = model_cat.predict(pd.DataFrame([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]],
                                                columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']))
    
    if prediction == 0:
        prediction = 'No diabetes'
    else:
        prediction = 'Diabetes'
    return prediction

st.title('Diabetes Predictor')
st.header('Enter the Client Information:')
Pregnancies = st.number_input('Pregnancies', min_value=0.0, max_value=2000.0, value=0.0)
#country = st.selectbox('Country', ['France','Spain','Germany'])
#gender = st.selectbox('Gender', ['Male','Female'])
Glucose = st.number_input('Glucose', min_value=0.0, max_value=2000.0, value=0.0)
BloodPressure = st.number_input('BloodPressure', min_value=0.0, max_value=2000.0, value=0.0)
SkinThickness = st.number_input('SkinThickness', min_value=0.0, max_value=2000.0, value=0.0)
Insulin = st.number_input('Insulin', min_value=0.0, max_value=2000.0, value=0.0)
BMI = st.number_input('BMI', min_value=0.0, max_value=2000.0, value=0.0)
DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction', min_value=0.0, max_value=2000.0, value=0.0)
Age = st.number_input('Age', min_value=0, max_value=2000, value=0)
#tenure = st.number_input('Tenure', min_value=0, max_value=2000, value=0)
#balance = st.number_input('Balance', min_value=0.0, max_value=2000000.0, value=0.0)
#products_number = st.number_input('Product Number', min_value=0, max_value=200, value=0)
#credit_card = st.selectbox('Credit Card', ['No','Yes'])
#active_member = st.selectbox('Active Member', ['No','Yes'])
#estimated_salary = st.number_input('Estimated Salary', min_value=0.0, max_value=2000000.0, value=0.0)



            

if st.button('Predict Diabetes'):
    Diabetes = predict(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
    st.success(f'The prediction is {Diabetes}')
        
   
    

        


        
        

        

    
    
    
    

    
        
    
    
        
        
        

















    

        

        
        
    
        
        
        
        
        


# In[ ]:




