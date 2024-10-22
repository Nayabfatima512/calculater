import streamlit as st

# Streamlit app for a simple calculator

# Set the title of the app
st.title("Simple Calculator")

# Choose an operation
operation = st.selectbox(
    "Select an operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

# Input numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Perform the selected operation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} / {num2} = {result}")
        else:
            st.write("Error: Division by zero is not allowed.")

# Display the result
if result is not None:
    st.success(f"The result is: {result}")
