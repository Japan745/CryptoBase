import streamlit as st
import base64

def get_ada_info():
    st.header("Cardano White Paper")

    with open("Ada-whitepaper.pdf", "rb") as file:
        btn = st.download_button(
            label="Click me! to download white paper",
            data=file,
            file_name="Ada-whitepaper.pdf",
            mime="application/octet-stream")

    def st_display_pdf(pdf_file):
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # pdf_display = f'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    with st.expander(" 👁  Cardano white paper "):
        st_display_pdf("Ada-whitepaper.pdf")