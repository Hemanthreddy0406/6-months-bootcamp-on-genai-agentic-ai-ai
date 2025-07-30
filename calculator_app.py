import streamlit as st
import math

st.title("Advanced Calculator App")

# Calculator logic
def calculate(op, num1, num2=None):
    try:
        if op == "Add":
            return num1 + num2
        elif op == "Subtract":
            return num1 - num2
        elif op == "Multiply":
            return num1 * num2
        elif op == "Divide":
            return num1 / num2 if num2 != 0 else "Error: Division by zero"
        elif op == "Power":
            return num1 ** num2
        elif op == "Modulus":
            return num1 % num2
        elif op == "Logarithm":
            if num1 > 0:
                return math.log(num1, num2) if num2 else math.log(num1)
            else:
                return "Error: Logarithm of non-positive number"
        elif op == "Square Root":
            return math.sqrt(num1) if num1 >= 0 else "Error: Negative input"
        elif op == "Sine":
            return math.sin(math.radians(num1))
        elif op == "Cosine":
            return math.cos(math.radians(num1))
        elif op == "Tangent":
            return math.tan(math.radians(num1))
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Error: {e}"

# UI
operations = [
    "Add", "Subtract", "Multiply", "Divide", "Power", "Modulus", "Logarithm", "Square Root", "Sine", "Cosine", "Tangent"
]

operation = st.selectbox("Select Operation", operations)

# Operations that need two inputs
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus", "Logarithm"]:
    num1 = st.number_input("Enter first number", value=0.0, format="%f")
    num2 = st.number_input("Enter second number", value=0.0, format="%f")
    if st.button("Calculate"):
        result = calculate(operation, num1, num2)
        st.success(f"Result: {result}")
# Operations that need only one input
else:
    num1 = st.number_input("Enter number", value=0.0, format="%f")
    if st.button("Calculate"):
        result = calculate(operation, num1)
        st.success(f"Result: {result}")