import streamlit as st
st.title('Calculator')
num1 = st.number_input('Enter the first number:')
operation = st.selectbox('Select operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])
num2 = st.number_input('Enter the second number:')
result = 0
if operation == 'Addition':
  result = num1 + num2
elif operation == 'Subtraction':
  result = num1 - num2
elif operation == 'Multiplication':
  result = num1 * num2
elif operation == 'Division':
  if num2 != 0:
    result = num1 / num2
  else:
    st.error("Cannot divide by zero.")
st.write('Result:', result)
