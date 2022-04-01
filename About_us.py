import streamlit as st

def aus():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header("Japan Patel")
        st.image("Images/japan.jpg",width=200)

    with col2:
        st.header("Ravi D Patel")
        st.image("Images/ravi.jpg",width=200)

    with col3:
        st.header("Dhairya Shah")
        st.image("Images/DHAIRYA.jpg",width=200)

    with col4:
        st.header("Mihir Mathur")
        st.image("Images/mihir.jpg",width=200)