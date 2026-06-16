import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open(model_path, "rb"))

st.title("🚗 Car Price Prediction")
st.write("Enter car details to predict the selling price.")

# Inputs
present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0,
    value=5.0
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0, 1, 2, 3]
)

car_age = st.number_input(
    "Car Age (Years)",
    min_value=0,
    value=5
)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

# Encoding
fuel_diesel = 1 if fuel_type == "Diesel" else 0
fuel_petrol = 1 if fuel_type == "Petrol" else 0

seller_individual = 1 if seller_type == "Individual" else 0

trans_manual = 1 if transmission == "Manual" else 0

# Prediction
if st.button("Predict Price"):

    input_df = pd.DataFrame([[
        present_price,
        kms_driven,
        owner,
        car_age,
        fuel_diesel,
        fuel_petrol,
        seller_individual,
        trans_manual
    ]], columns=[
        'Present_Price',
        'Kms_Driven',
        'Owner',
        'Car_Age',
        'Fuel_Type_Diesel',
        'Fuel_Type_Petrol',
        'Seller_Type_Individual',
        'Transmission_Manual'
    ])

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Selling Price: ₹ {prediction[0]:.2f} Lakhs"
    )
