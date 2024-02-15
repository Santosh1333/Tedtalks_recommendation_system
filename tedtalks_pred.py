import pickle
import streamlit as st

# Attempt to load the saved model
try:
    with open('tedtalks_recommendation.sav', 'rb') as f:
        Tedtalks_recommendation_model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please ensure that the file path is correct.")
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")

st.title('Ted Talks Recommendation')

# Collect user input
prompt = st.text_input('Enter your prompt here')

# Prediction logic
tedtalk_recom = ''

if st.button('Get Recommendations'):
    # You need to define what kind of input the model expects
    # For example, if it's text, you might need to preprocess it before prediction
    # Replace 'input_data' with the correct preprocessing of 'prompt' based on your model's requirements
    
    tedtalk_recom = Tedtalks_recommendation_model.predict(prompt)

st.success(tedtalk_recom)
