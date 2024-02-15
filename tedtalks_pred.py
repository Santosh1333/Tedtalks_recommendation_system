import pickle
import streamlit as st

# Loading the saved function
try:
    with open('tedtalks_recommendation.sav', 'rb') as f:
        loaded_model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please ensure that the file path is correct.")
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")

st.title('Ted Talks Recommendation')

# Collect user input
prompt = st.text_input('Enter your prompt here')

# Recommendation logic
tedtalk_recom = ''

if st.button('Get Recommendations'):
    # Call the loaded function directly with the input prompt
    tedtalk_recom = loaded_model(prompt)

st.success(tedtalk_recom)
