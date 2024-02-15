import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models



Tedtalks_recommendation_model = pickle.load(open('tedtalks_recommendation.sav', 'rb'))

st.title('Heart Disease Prediction using ML')

col1 = st.columns(1)
    
    with col1:
        prompt = st.text_input('prompt')\
# code for Prediction
    tedtalk_recom = ''
    
    
    
    if st.button('result'):
        tedtalk_recom = Tedtalks_recommendation_model.predict(prompt)                          
        
        
        
    st.success(tedtalk_recom)
