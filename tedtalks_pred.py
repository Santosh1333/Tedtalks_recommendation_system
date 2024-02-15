import pickle
import streamlit as st

tedtalks_recommendation_model = pickle.load(open('heart_disease_model.sav', 'rb'))

st.title('Ted Talks Recommendation')

# Collect user input
prompt = st.text_input('Enter your prompt here')

# Recommendation logic
tedtalk_recom = ''

if st.button('Get Recommendations'):
    # Call the loaded function directly with the input prompt
    tedtalk_recom = loaded_model(prompt)

st.success(tedtalk_recom)
