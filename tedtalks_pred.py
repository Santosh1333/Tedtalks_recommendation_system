import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
Tedtalks_recommendation_model = pickle.load(open('tedtalks_recommendation.sav', 'rb'))

st.title('Ted Talks Recommendation')

# Collect user input
prompt = st.text_input('Enter your prompt here')

# Prediction logic
tedtalk_recom = ''

if st.button('Get Recommendations'):
    # You need to define what kind of input the model expects
    # For example, if it's text, you might need to preprocess it before prediction
    # Replace 'input_data' with the correct preprocessing of 'prompt' based on your model's requirements
    input_data = preprocess_data(prompt)
    tedtalk_recom = Tedtalks_recommendation_model.predict(input_data)

st.success(tedtalk_recom)
