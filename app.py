import streamlit as st
import requests

st.title("My streamlit application")
st.header("Welcome to the app")


# Add a number input and display the square of the input
number = st.number_input("Enter a number", 0)
st.write("Square of the number:", number**2)

slider_val = st.slider("Select a value", 0, 100)
st.write("Slider value:", slider_val)

# Dropdown menu
option = st.selectbox("Choose a color", ["Red", "Green", "Blue"])
st.write("You selected:", option)

# Button interaction
if st.button("Click me"):
    st.write("Button clicked!")

user_input = st.text_input("Enter some text")

def callApi(blogTitle):
    url = "https://localhost:4000/posts"
    params = {"title" : blogTitle}
    response = requests.get(url, params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve data"}

if st.button("Fetch Data"):
    api_response = call_api(user_input)
    st.text_area("API response", value=str(api_response), height=200)