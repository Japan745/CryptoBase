import streamlit as st
import base64

def get_ada_info():

    st.header("What Is Cardano (ADA)?")
    st.write("Cardano is a proof-of-stake blockchain platform that says its goal is to allow “changemakers, innovators "
             "and visionaries” to bring about positive global change.")
    st.write("The open-source project also aims to “redistribute power from unaccountable structures to the margins to "
             "individuals” — helping to create a society that is more secure, transparent and fair.")
    st.write("Cardano was founded back in 2017, and named after the 16th century Italian polymath Gerolamo Cardano. "
             "The native ADA token takes its name from the 19th century mathematician Ada Lovelace, widely regarded as "
             "the world’s first computer programmer. The ADA token is designed to ensure that owners can participate in "
             "the operation of the network. Because of this, those who hold the cryptocurrency have the right to vote "
             "on any proposed changes to the software.")
    st.write("The team behind the layered blockchain say that there have already been some compelling use cases for its "
             "technology, which aims to allow decentralized apps and smart contracts to be developed with modularity.")
    st.write("In August 2021, Charles Hoskinson announced the launch of the Alonzo hard fork, causing Cardano price to "
             "surge, gaining 116% in the following month. On Sept. 12, 2021, the Cardano ‘Alonzo’ hard fork officially "
             "launched, bringing smart contract functionality to the blockchain. Over 100 smart contracts were deployed "
             "in the following 24 hours after the launch.")
    st.write("Cardano is used by agricultural companies to track fresh produce from field to fork, while other products "
             "built on the platform allow educational credentials to be stored in a tamper-proof way, and retailers to "
             "clamp down on counterfeit goods.")

    st.header("Who Are the Founders of Cardano?")
    st.write("Cardano was founded by Charles Hoskinson, who was also one of the co-founders of the Ethereum network. "
             "He is the CEO of IOHK, the company that built Cardano’s blockchain.")
    st.write("In an interview for CoinMarketCap’s Crypto Titans series, Hoskinson said that he got involved in "
             "cryptocurrencies back in 2011 — and dabbled in mining and trading. He explained that his first professional "
             "involvement in the industry came in 2013, when he created a course about Bitcoin that ended up being taken "
             "by 80,000 students.")
    st.write("As well as being a technology entrepreneur, Hoskinson is also a mathematician. In 2020, his technology "
             "company donated ADA worth $500,000 to the University of Wyoming’s Blockchain Research and Development Lab.")

    st.header("What Makes Cardano Unique?")

    st.write("Cardano is one of the biggest blockchains to successfully use a proof-of-stake consensus mechanism, which "
             "is less energy intensive than the proof-of-work algorithm relied upon by Bitcoin. Although the much larger "
             "Ethereum is going to be upgrading to PoS, this transition is only going to take place gradually.")
    st.write("The project has taken pride in ensuring that all of the technology developed goes through a process of "
             "peer-reviewed research, meaning that bold ideas can be challenged before they are validated. According to "
             "the Cardano team, this academic rigor helps the blockchain to be durable and stable — increasing the chance "
             "that potential pitfalls can be anticipated in advance.")
    st.write("In 2020, Cardano held a Shelley upgrade that aimed to make its blockchain “50 to 100 times more "
             "decentralized” than other large blockchains. At the time, Hoskinson predicted that this would pave the way "
             "for hundreds of assets to run on its network.")
    st.write("The Alonzo hard fork launch in September 2021 will bring an end to the Shelley era, and usher in the "
             "Goguen phase. Users can develop and deploy smart contracts on Cardano, allowing native decentralized "
             "applications (DApps) to be built on blockchain. Cardano price broke the 3 dollar mark and hit an all-time "
             "high of 3.101 dollar on Sept. 2, 2021, ahead of the launch.")
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