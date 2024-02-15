import pickle
import streamlit as st

tedtalks_recommendation_model = pickle.load(open('tedtalks_recommendation.sav', 'rb'))

st.title('Ted Talks Recommendation')

# Collect user input
prompt = st.text_input('Enter your prompt here')

# Recommendation logic


if st.button('Get Recommendations'):
    # Call the loaded function directly with the input prompt
    tedtalk_recom = tedtalks_recommendation_model(prompt)

st.success(tedtalk_recom)
