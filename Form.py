import streamlit as st

st.title("Form")
name = st.text_input("Enter your name")
country = st.selectbox("Select your country", ["USA", "Canada", "UK", "Australia"])
gender = st.radio("Select your gender", ["Male", "Female", "Other"])
birthdate = st.date_input("Enter your birthdate")
if st.button("Submit"):
  st.success(f"Name: {name}, Country: {country}, Gender: {gender}, Birthdate: {birthdate}")
