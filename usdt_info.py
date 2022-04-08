import base64

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go


def get_usdt_info():
    st.header("Tether")
    st.write("Tether (USDT) was one of the first cryptocurrencies to peg its market value to a fiat currency. "
             "Tether, originally called Realcoin, valued each token at $1 to reduce the friction of"
             "moving real currency throughout the cryptocurrency ecosystem. Because of that peg to a "
             "stable fiat currency, Tether and other similar")
    st.write("cryptocurrencies have been dubbed stablecoins."
             "Tether is the largest stablecoin by market capitalization, and its users "
             "can redeem tethers for dollars. It also issues a cryptocurrency tied to the "
             "price of gold known as tether gold, whose value is backed by physical gold bars.")

    st.header("USDT Price")
    st.write("The primary purpose of a stablecoin like USDT is to maintain its value of dollar 1 at all times."
             " Maintaining that value should be straightforward as every USDT is backed by "
             "reserves held by the Tether Treasury."
             " However,Tether's asset has seen some price fluctuations over the years."
             "USDT hit an all-time high value of $'\'1.32 in July 2018."
             "The all-time low of $'/'0.57"
             "came in March 2015. The price swings occur when demand for the token changes."
             "When the crypto market is surging, demand for stablecoins like tether is typically low."
             "Tether's history of lawsuits has also played a part in reducing demand for the crypto asset."
             " When the New York Attorney General's office (NYAG) first took legal action against"
             "the project, USDT was pushed off its dollar peg by 3%."
             " With the exception of those low and high prices, Tether's price has generally "
             "remained close to $1. There can be a minor deviation of $0.01 or $0.02 at times, "
             "although those are usually short-lived. There is no known maximum supply for Tether's USDT, "
             "as new coins are issued based on user demand and ")
    st.header("History")
    st.write("Tether was founded in 2014 by American software developer Craig Sellars,"
             "Bittinex Chief Financial Officer Glancarlo Devasini and Phillp Potter, "
             "a former executive at Bitfinex. All three men are still with the company."
             " Jean-Louis van der Velde, Bitfinex's CEO, is also the CEO of Tether Holdings,"
             " Tether's parent company")
    st.header("How Does it Work")
    st.write("Tether and the tokens it create are designed to be stablecoins pegged to real-life "
             "assets or commodities to provide stability in value, particularly in volatile markets. "
             "Tether's USDT is pegged to the U.S, dollar, but whether the crypto's reserves consist of actual "
             "dollars, Or similarly safe assets, has been the subject of contention."
             "In October 2021, Tether paid a $41 million fine to settle allegations by the U.S. "
             "Commodity Futures Trading. Commision that it lied about its digital currency being supported "
             "by fiat currencies. Tether has agreed to provide regular attestations and audits of its reserves,"
             " which were found to be held in such risky investments as loans"
             "and other cryptocurrencies, instead of cash or cash equivalents. "
             "Tether launched on Bitcoin's Omni Layer, but continues to expand to other protocols, "
             "including Ethereum, Bitcoin Cash, TRON, EOS, Liquid Network, Algorand, SLP, and Solana."
             " Ethereum and TRON are the blockchains with the most USDT supply. Tether is often used "
             "to buy and sell different cryptocurrencies.")
    data = yf.download("USDT-CAD")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(data.index), y=list(data['Adj Close']), line=dict(color="#76D714")))
    '''fig.add_trace(go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'], name='market data'))'''
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
    st.header("Tether All time graph")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Tether White Paper")

    with open("Tether-White-Paper-PDF.pdf", "rb") as file:
        btn = st.download_button(
            label="Click me! to download white paper",
            data=file,
            file_name="Tether-White-Paper-PDF.pdf",
            mime="application/octet-stream")

    def st_display_pdf(pdf_file):
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # pdf_display = f'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    with st.expander(" 👁  Tether white paper "):
        st_display_pdf("Tether-White-Paper-PDF.pdf")
