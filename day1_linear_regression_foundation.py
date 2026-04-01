import streamlit as st
from sklearn.linear_model import LinearRegression
from babel.numbers import format_currency

st.title("House Price Predictor 🏠")
st.write("Enter the square footage of a house to estimate its price in Kurmannapalem, Visakhapatnam.")

# Train the model
house_sizes = [[1000], [1200], [1500], [1800]]
house_prices = [4000000, 4800000, 6000000, 7200000]

model = LinearRegression()
model.fit(house_sizes, house_prices)

# User input
user_size = st.number_input(
    label="House Size (sq ft):",
    min_value=500,
    max_value=10000,
    value=1300,
    step=50
)

# Prediction button
if st.button("Predict Price"):
    prediction = model.predict([[user_size]])
    estimated_price = prediction[0]
    
    # Format the price using Babel for the Indian numbering system (Lakhs/Crores)
    indian_price = format_currency(estimated_price, 'INR', locale='en_IN')
    
    # Display the beautifully formatted price
    st.success(f"The estimated price is: **{indian_price}**")
