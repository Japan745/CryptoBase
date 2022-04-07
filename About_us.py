import streamlit as st

def aus():

    st.title("Abstract")
    st.write("")
    st.write("")
    st.write("")
    st.write("---")

    col1, col2, col3 = st.columns([3, 1, 9])
    with col1:

        st.image("Images/img/DHAIRYA.jpg", use_column_width=True)

    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.title("DHAIRYA SHAH")
        st.write("")
        st.subheader("I had completed my Bachleor's in Information Technology from ADIT" +
                     " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data. ")
    st.write("---")

    col4,col5,col6 = st.columns([9,1,3])
    with col4:
       st.write("")
       st.write("")
       st.write("")
       st.title("JAPAN PATEL")
       st.write("")
       st.subheader("I had completed my Bachleor's in Information Technology from Birla Vishvakarma Mahavidyalaya" +
                    " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data. ")


    with col6:
        st.image("Images/img/japan.jpg", use_column_width=True)

    st.write("---")

    col7, ccl8, col9 = st.columns([3, 1, 9])
    with col7:
        st.image("Images/img/mihir.jpg", use_column_width=True)

    with col9:
        st.write("")
        st.write("")
        st.write("")
        st.title("MIHIR MATHUR")
        st.write("")
        st.subheader("I had completed Bachleor's of Computer Science and Engineering from JECRC University" +
                     " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data.")

    st.write("---")

    col10, col11,col12 = st.columns([9,1,3])
    with col10:
        st.write("")
        st.write("")
        st.write("")
        st.title("RAVI PATEL")
        st.write("")
        st.subheader("I had completed my Bachleor's in Computer Engineering from Gandhinagar Institute of Technology" +
                     " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data. ")

    with col12:
        st.image("Images/img/ravi.jpg", use_column_width=True)

    hide_img_fs = '''
                    <style>
                    button[title="View fullscreen"]{
                        visibility: hidden;}
                    </style>
                    '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)