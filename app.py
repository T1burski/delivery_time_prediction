import streamlit as st
import pickle
import numpy as np
import pandas as pd
from src.feature_engineering import FeatureEngineering

#loading the model and standardized pickle files

def load_model():
    with open('artifacts\model.pkl', 'rb') as model:
        regressor_model = pickle.load(model)
    return regressor_model

def load_standardizer():
    with open('artifacts\standardization.pkl', 'rb') as standardscaler:
        standardizer = pickle.load(standardscaler)
    return standardizer

regressor_model = load_model()

standardizer = load_standardizer()


# creates front-end of the Web App, adding visuals and the user interaction fields 

st.title("Time Taken To Make the Delivery Prediction (Minutes)")
st.divider()
st.write("""### This ML Web App Predicts The Time Taken For A Delivery To Be Completed Considering The Time Between When The Delivery Person Leaves The Restaurant And When The Delivery Person Reaches The Client's Location""")

st.divider()

age = st.slider("Delivery Person's Age", 0, 99, 1)

vehicle = st.selectbox("Type Of Vehicle Used", ("motorcycle", "scooter", "electric_scooter", "bicycle"))

ratings = st.number_input("Delivery Person's Rating (0 - 6)", min_value=0.0, max_value=6.0)

rest_lat = st.number_input("Restaurant's Latitude", format="%.6f")
rest_lon = st.number_input("Restaurant's Longitude", format="%.6f")
dest_lat = st.number_input("Delivery Locations's Latitude", format="%.6f")
dest_lon = st.number_input("Delivery Locations's Longitude", format="%.6f")

#creates the final buttton to use all data provided by the user

ok = st.button("Predicted Time To Make The Delivery (min)")
if ok:
    #engineers all the data provided so it can be ingested into the standardization
    #and model processors, returning the prediction.

    X_input_values = [[rest_lat, rest_lon, dest_lat, dest_lon, vehicle, age, ratings]]
    X_input_raw = pd.DataFrame(X_input_values, columns=['Restaurant_latitude', 'Restaurant_longitude', 'Delivery_location_latitude', 'Delivery_location_longitude', 'Type_of_vehicle', 'Delivery_person_Age', 'Delivery_person_Ratings'])
    engineered_data = FeatureEngineering(X_input_raw).engineer()
    X_input_treated = engineered_data[['Delivery_person_Age', 'Delivery_person_Ratings', 'is_motorcycle', 'Delivery_Distance_km']]
    X_input_standardized = standardizer.transform(X_input_treated)
    X_input_standardized = X_input_standardized.astype(float)

    time_taken = regressor_model.predict(X_input_standardized)
    st.subheader(f"The Estimated Time To Make The Delivery Is {time_taken[0]:.1f} Minutes")


