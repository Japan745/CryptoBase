import streamlit as st
from streamlit_option_menu import option_menu
import contactus
import About_us
import home
base = "dark"

st.set_page_config(
    # page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state='auto'
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
    #    'Report a bug': "https://www.extremelycoolapp.com/bug",
    #    'About': "# This is a header. This is an extremely cool app!"
    # }
)


# with st.sidebar:
# st.title('Home')
# st.subheader('Prediction')
#st.subheader('Live price')
# st.subheader('Comparison')
#st.subheader('Crypto Info')
#st.subheader('Contact Us')
selected = option_menu(


    menu_title=None,

    orientation="horizontal",
    img = st.image("Images/logo.jpg", use_column_width='Never',width=100),
    options=["Home", "Live pricing", "Basic Info",
             "Trading tips", "Comparison", "About Us","Contact us"],
    default_index=0
)

if selected == "Home":
    home.home()
elif selected == "Live pricing":
    st.title("This is live pricing section")
elif selected == "Basic Info":
    st.title("This is Basic Info page")
elif selected == "Trading tips":
    st.title("This is trading tips pAGE")
elif selected == "About Us":
     About_us.aus()
elif selected == "Comparison":
    st.title("This is comparison page")
elif selected == "Contact us":
    contactus.callus()
