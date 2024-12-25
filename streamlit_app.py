import streamlit as st
import pandas as pd

# Title
st.title("Calorie Prediction App")

# Sidebar inputs
st.sidebar.header("Input Features")
import pickle

# Load your trained model (adjust the path as necessary)
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

    gender_value = 1 if gender == "Male" else 0
    activity_map = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Extra active": 1.9,
    }
    activity_value = activity_map[activity_level]

    data = {
        "Age": age,
        "Gender": gender_value,
        "Height": height,
        "Weight": weight,
        "Activity Level": activity_value,
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Display input features
st.subheader("User Input Features")
st.write(input_df)

# Predict button
if st.button("Predict Calories"):
    prediction = model.predict(input_df) 
    st.subheader("Predicted Calorie Requirement")
    st.write(f"{prediction[0]:.2f} calories/day")
