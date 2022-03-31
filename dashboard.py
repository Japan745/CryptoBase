import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


base = "dark"

st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
     page_icon="🧊",
     layout="wide",
    # initial_sidebar_state="expanded",
     #menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
     #    'Report a bug': "https://www.extremelycoolapp.com/bug",
     #    'About': "# This is a header. This is an *extremely* cool app!"
     #}
 )




#with st.sidebar:
     #st.title('Home')
     #st.subheader('Prediction')
     #st.subheader('Live price')
     #st.subheader('Comparison')
     #st.subheader('Crypto Info')
     #st.subheader('Contact Us')
selected = option_menu(
         menu_title=None,
         options=["Home","Live pricing","Basic Info","Trading tips", "Comparison","Contact us"],
         default_index=0,
         orientation="horizontal"
     )
if selected == "Home":
        st.title("home page")
elif selected =="Live pricing":
        st.title("This is live pricing section")
elif selected == "Basic Info":
        st.title("This is Basic Info page")
elif selected == "Trading tips":
        st.title("This is trading tips pAGE")
elif selected == "Comparison":
        st.title("This is comparison page")
elif selected == "Contact us":
        st.title("This is contact us page")


