import base64

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_shib_info():
    st.header("Shiba Inu")
    st.write("Shiba Inu (SHIBUSD) is an Ethereum-based altcoin (a cryptocurrency other than Bitcoin) that features the Shiba Inu—a Japanese breed of hunting dog—as its mascot. Shiba Inu is widely considered to be an alternative to Dogecoin; "
             "in fact, proponents of Shiba Inu tout it as the Dogecoin killer.Shiba Inu and Dogecoin are meme coins, which are cryptocurrencies that are associated with some theme—like the Shiba Inu dog in the case of Shiba Inu and Dogecoin—but are often launched as a parody or inside joke rather than as a digital product that actually has some utility. While Dogecoin was launched in December 2013, Shiba Inu was created in August 2020 "
             "by an anonymous individual or group called Ryoshi.Shiba Inu's price soared more than tenfold in October 2021, giving it a peak market capitalization of 41 billion dollar (on October 29, 2021) and became one of the top ten meme cryptocurrencies by this measure. A tweet from Tesla founder Elon Musk on Oct. 3, 2021, featuring a picture of his new Shiba Inu puppy Floki provided the initial impetus for the meme coin's price surge. Because Musk is one of the most high-profile supporters of Dogecoin and the self-proclaimed Dogefather, his cryptic tweets often result "
             "in heightened volatility in the cryptocurrency space.Shiba Inu's price surge in October 2021 resulted in it almost catching up to Dogecoin's $36.9 billion market capitalization (as of Oct. 31, 2021), after briefly surpassing it at one point. It remains to be seen whether Shiba Inu will indeed become the Dogecoin killer that its growing community of supporters—known as the SHIBArmy—expects. But at least in October 2021, the stunning price gains of this previously obscure altcoin made " 
             "Shiba Inu the tail that wagged the Dog(ecoin).")
    st.header("Understanding Shiba Inu")
    st.write("The guiding tenets of the Shiba Inu ecosystem are spelled out in a woof paper presumably a play on white paper),"
             " available at the ShibaToken.com website.According to the paper, Shiba Inu was developed as the answer to a simple question: What would happen if a cryptocurrency project was 100% run by its community? Its founder Ryoshi attributes its origins to an experiment in decentralized spontaneous community building.According to Ryoshi, the power of collective decentralization can build something stronger " \
             "than a centralized team ever could create.Because Shiba Inu is an Ethereum-based ERC-20 token, it is created on and hosted by the Ethereum blockchain, instead of its own blockchain. Ryoshi states in the paper that he chose to build the Shiba Inu ecosystem on Ethereum because it was already secure and well-established, "
             "and it allowed the project to stay decentralized.")

    data = yf.download("SHIB-CAD")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(data.index), y=list(data['Adj Close']), line=dict(color="#76D714")))
    fig.update_layout(
                      xaxis_title="Date",
                      yaxis_title="P rice in Canadian dollar", )
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=1,
                         label="1m",
                         step="month",
                         stepmode="backward"),
                    dict(count=3,
                         label="3m",
                         step="month",
                         stepmode="backward"),
                    dict(count=6,
                         label="6m",
                         step="month",
                         stepmode="backward"),
                    dict(count=1,
                         label="1y",
                         step="year",
                         stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    st.header("Shiba Inu All time graph")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Shiba Inu White Paper")

    with open("SHIBAINU_Ecosystem_WOOF_Paper.pdf", "rb") as file:
        btn = st.download_button(
            label="Click me! to download white paper",
            data=file,
            file_name="SHIBAINU_Ecosystem_WOOF_Paper.pdf",
            mime="application/octet-stream")

    def st_display_pdf(pdf_file):
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    with st.expander(" 👁  Shiba Inu white paper "):
        st_display_pdf("SHIBAINU_Ecosystem_WOOF_Paper.pdf")