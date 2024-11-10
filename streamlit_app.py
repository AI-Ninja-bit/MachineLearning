import streamlit as st
import joblib
import pandas as pd

st.markdown("""
<style>
.stMainMenu.st-emotion-cache-hwawmg.e16jpq800{
    visibility:hidden;
}
_terminalButton_rix23_138{
    visibility:hidden;
}
</style>
""",unsafe_allow_html=True)

# Load the trained model
model = joblib.load('model.pkl')  # Ensure model.pkl is in the same directory

# Set up the app title and description
st.title("Calories Prediction App")
st.write("This app predicts calories burned based on steps, distance, and active minutes.")

# Define user inputs for the features
steps = st.number_input("Steps:", min_value=0, max_value=100000, value=1000, step=100)
distance = st.number_input("Distance (in km):", min_value=0.0, max_value=100.0, value=1.0, step=0.1)
active_minutes = st.number_input("Total Active Minutes:", min_value=0, max_value=1440, value=30, step=5)

# Predict calories when the button is clicked
if st.button("Predict Calories"):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame([[steps, distance, active_minutes]], columns=['Steps', 'Distance', 'Total_Active_Minutes'])
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f"Estimated Calories Burned: {prediction[0]:.2f}")
