import streamlit as st

def aus():

    st.title("Abstract")
    st.write("")
    st.write("")
    st.subheader("In the past years we have seen that price of cryptocurrency rapidly grow due to its great return. "
             "So, our team explored several cryptocurrencies and we have decided to make a web-app that will display all "
             "the necessary things (like Basic info of particular crypto, their live pricing, 7 days graph, etc) along with hourly, "
            "weekly and monthly forecasting of crypto coins for better understanding of the nature of cryptocurrencies.")
    st.write("---")

    col1, col2, col3 = st.columns([3, 1, 9])
    with col1:

        st.image("Images/DHAIRYA.jpg", use_column_width=True)

    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.title("DHAIRYA SHAH")
        st.caption("Languages : HTML, CSS, JavaScript, C, C++,  Java, Python")
        st.write("")
        st.subheader("I had completed my Bachelor's in Information Technology from ADIT" +
                     " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data. ")


    st.write("---")

    col4,col5,col6 = st.columns([9,1,3])
    with col4:
       st.write("")
       st.write("")
       st.write("")
       st.title("JAPAN PATEL")
       st.caption("Languages : HTML, CSS, JavaScript, C, C++, Java, PHP, Flutter, Python")
       st.write("")
       st.subheader("I had completed my Bachelor's in Information Technology from Birla Vishvakarma Mahavidyalaya" +
                    " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data. ")




    with col6:
        st.image("Images/japan.jpg", use_column_width=True)

    st.write("---")

    col7, ccl8, col9 = st.columns([3, 1, 9])
    with col7:
        st.image("Images/mihir.jpg", use_column_width=True)

    with col9:
        st.write("")
        st.write("")
        st.write("")
        st.title("MIHIR MATHUR")
        st.caption("Languages : HTML, CSS, JavaScript, C, C++,  Java, Python")
        st.write("")
        st.subheader("I had completed Bachelor's of Computer Science and Engineering from JECRC University" +
                     " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data.")



    st.write("---")

    col10, col11,col12 = st.columns([9,1,3])
    with col10:
        st.write("")
        st.write("")
        st.write("")
        st.title("RAVI PATEL")
        st.caption("Languages : HTML, CSS, JavaScript, Java, Python")
        st.write("")
        st.subheader("I had completed my Bachelor's in Computer Engineering from Gandhinagar Institute of Technology" +
                     " and currently pursuing Post-Graduation Certificate in Cloud Computing for Big Data. ")


    with col12:
        st.image("Images/ravi.jpg", use_column_width=True)

    hide_img_fs = '''
                    <style>
                    button[title="View fullscreen"]{
                        visibility: hidden;}
                    </style>
                    '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)