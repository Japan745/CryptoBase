

import streamlit as st  # pip install streamlit

def callus():
    st.header(":mailbox: contact us from here!")
    st.write("we will reach out at you as soon as possible")


    contact_form = """
        <form action="https://formsubmit.co/ravipatel7636@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style\style.css.txt")

