import streamlit as st

st.title("Form")
fname = st.text_input("Enter your first name")
mname = st.text_input("Enter your middle name")
lname = st.text_input("Enter your last name")
mobile = st.text_input("Enter your mobile number")
msg = st.text_input("Any message for us")

if st.button("Submit"):
  st.success(f"Name: {fname,mname,lname}, mobile: {mobile}, Message: {msg}")
