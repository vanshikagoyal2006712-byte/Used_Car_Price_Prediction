
import streamlit as st
import pickle 
import pandas as pd
df = pd.read_csv("car data.csv")

model=pickle.load(open("car_price_model.pkl","rb"))
st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details below to estimate its selling price.")
year=st.number_input("Manufacturing Year",min_value=1990,max_value=2026)
km_driven=st.number_input("Kilometers Driven")
fuel=st.selectbox("Fuel Type",["Petrol","Diesel","CNG","LPG"])
seller=st.selectbox("Seller Type",["Dealer","Individual"])
transmission=st.selectbox("Transmission",["Manual","Automatic"])
owner=st.selectbox("Owner",["First","Second","Third","Fourth or above"])
companies = sorted(df["company"].unique())
company = st.selectbox(
    "Select Company",
    companies
)
if st.button("Predict Price"):
    input_df = pd.DataFrame({
    "year":[year],
    "km_driven":[km_driven],
    "fuel":[fuel],
    "seller_type":[seller],
    "transmission":[transmission],
    "owner":[owner],
    "company":[company]
})
    prediction=model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]:,.2f}")


