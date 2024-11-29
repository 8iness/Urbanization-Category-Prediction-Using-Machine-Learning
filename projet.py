#1-Importing the necessary libraries
import joblib
import streamlit as st
import numpy as np

#2-To load the model back
model = 'random_forest_model.joblib'
loaded_model = joblib.load(model)

#3-give a title to our app 
st.title('Prediction of urbanization category')

#4-Prediction function
def predict_urbanization_category(data):
    prediction = loaded_model.predict([data])
    return prediction[0]


#4-Add numeric input fields
urbanization_index = st.slider('Urbanization Index', min_value=0.0, max_value=1.0)
year= st.slider('Year', min_value=2020, max_value=2024)
avg_temp = st.number_input('Average Temperature (°C)', min_value=-5.0, max_value=35.0)
precipitation = st.number_input('Precipitation (mm)', min_value=0.0, max_value=200.0)
proximity_to_water = st.number_input('Proximity to Water (km)', min_value=15.0, max_value=5000.0)
vegetation_index = st.slider('Vegetation Index', min_value=0.0, max_value=1.0)

#5-When the user presses the predict button
if st.button('Predict'):
    input_data = [urbanization_index, year, avg_temp, precipitation, proximity_to_water, vegetation_index]
    prediction = predict_urbanization_category(input_data)
    
    st.write(f"The predicted urbanization category is: {prediction}")