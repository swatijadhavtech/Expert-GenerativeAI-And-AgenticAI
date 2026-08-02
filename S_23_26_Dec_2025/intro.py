import streamlit as st
st.title("My First Streamlit App")
st.write("Welcome! This app calculate the square of a number.")
st.header("Select a number")
number = st.slider("Select a number", 0, 100, 25)
st.subheader("Square of the selected number is:")
square = number ** 2
st.write(f"The square of {number} is {square}.")
