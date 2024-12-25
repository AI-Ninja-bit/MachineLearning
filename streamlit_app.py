import streamlit as st
import pandas as pd
import pickle

# Title
st.title("Calorie Prediction App")

# Sidebar inputs
st.sidebar.header("Input Features")

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def user_input_features():
    age = st.sidebar.slider("Age", 10, 80, 25)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    height = st.sidebar.number_input("Height (cm)", 100, 250, 170)
    weight = st.sidebar.number_input("Weight (kg)", 30, 200, 70)
    activity_level = st.sidebar.selectbox("Activity Level", [
        "Sedentary",
        "Lightly active",
        "Moderately active",
        "Very active",
        "Extra active",
    ])

    # Map categorical inputs to numerical values
    gender_value = 1 if gender == "Male" else 0
    activity_map = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Extra active": 1.9,
    }
    activity_value = activity_map[activity_level]

    # Create a DataFrame for the input features
    data = {
        "Age": [age],
        "Gender": [gender_value],
        "Height": [height],
        "Weight": [weight],
        "Activity_Level": [activity_value],
    }
    return pd.DataFrame(data)

input_df = user_input_features()

# Display user input features
st.subheader("User Input Features")
st.write(input_df)

# Predict button
if st.button("Predict Calories"):
    try:
        # Make prediction
        prediction = model.predict(input_df)

        # Display prediction
        st.subheader("Predicted Calorie Requirement")
        st.write(f"{prediction[0]:.2f} calories/day")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
