import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Among Three Numbers : ")
st.write("Enter three numbers below :")
num1 = st.number_input("Enter 1st number", value=0)
num2 = st.number_input("Enter 2nd number", value=0)
num3 = st.number_input("Enter 3rd number", value=0)
if st.button("Find Largest"):
  largest = find_largest(num1, num2, num3)
  st.write(f"The largest number is: {largest}")

