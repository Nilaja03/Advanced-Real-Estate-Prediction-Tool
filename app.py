import streamlit as st
import pandas as pd
import pickle

# Loading the trained Random Forest model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Loading the scaler and feature columns
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('feature_columns.pkl', 'rb') as f:
    feature_columns = pickle.load(f)  

st.set_page_config(layout="wide")  # Use the entire screen width

st.title("Advanced Real Estate Prediction Tool")
st.write("Enter the details of the house below to predict its price.")

# Splitting input features into 6 columns
cols = st.columns(6)

# Dynamically creating input fields for all 287 features
input_data = {}
for i, feature in enumerate(feature_columns):
    col = cols[i % 6]  # Distribute features evenly across 6 columns
    input_data[feature] = col.number_input(f"{feature}", value=0.0)

# Converting the input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Standardizing the input data
input_scaled = scaler.transform(input_df)

# Making prediction if the button is clicked
if st.button("Predict Price"):
    prediction = model.predict(input_scaled)
    st.success(f"The predicted house price is ${prediction[0]:,.2f}")
