import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_doge_info():
    st.header("Dogecoin")
    st.write("Dogecoin (DOGE) is a peer-to-peer, open-source cryptocurrency. "
             "It is considered an altcoin and an almost sarcastic meme coin. "
             "Launched in December 2013, Dogecoin has the image of a Shiba Inu dog as its logo."
             "While it was created seemingly as a joke, Dogecoin's blockchain still has merit."
             " Its underlying technology is derived from Litecoin. Notable features of Dogecoin, "
             "which uses a scrypt algorithm, are its low price and unlimited supply.Dogecoin started as something of a joke, but after it was created, "
             "it gained a following. By late 2017, it was participating in the cryptocurrency "
             "bubble that sent the values of many coins up significantly. After the bubble burst in 2018, Dogecoin lost much of its value, "
             "but it still has a core of supporters who trade it and use it to tip for content on Twitter and Reddit.2 can Users   "
             "buy and sell Dogecoin on digital currency exchanges. They can opt to store their Dogecoin on " 
             "an exchange or in a Dogecoin wallet.Dogecoin's infrastructure has not been a central focus for the coin's developers, who are volunteers. "
             "One reason Dogecoin continues to operate and trade is its active community of miners."
             " As Zachary Mashiach of CryptoIQ puts it:")
    st.write("Numerous Scrypt miners still prefer Dogecoin (DOGE) over other Scrypt PoW cryptocurrencies. "
             "Indeed, the Dogecoin (DOGE) hash rate is roughly 150 TH/s. This is just below the "
             "Litecoin (LTC) hash rate of 170 TH/s, likely because Dogecoin (DOGE) can be merge "
             "mined with Litecoin (LTC), meaning miners can mine both cryptos simultaneously using "
             "the same work. Essentially, practically everyone who mines Litecoin (LTC) chooses to"
             " mine Dogecoin (DOGE) as well, because merge mining Dogecoin (DOGE) increases profits.Musk has openly"
             " supported Dogecoin in 2021, tweeting in May that he was working with the coin's developers"
             " to improve transaction efficiency. Earlier in the year, the SpaceX founder even ran a poll"
             " on social media asking if Tesla should accept Dogecoin as a form of payment. In October, "
             "cinema chain AMC Entertainment Holdings, Inc. (AMC) announced that it would accept Dogecoin"
             " for digital gift card purchases by the end of the year, further adding utility to the meme-based"
             " cryptocurrency.As of Oct. 8, 2021, Dogecoin's market cap ranking was number 10, with a market"
             " capitalization of $31.9 billion, substantially higher than its year-ago position of 48 and $339"
             " million market value.")
    st.header("History")
    st.write("Jackson Palmer, a product manager at the Sydney, Australia, office of Adobe Inc.,"
             " created Dogecoin in 2013 as a way to satirize the hype surrounding cryptocurrencies. "
             "Palmer has been described as a skeptic-analytic observer of the emerging technology," 
            " and his initial tweets about his new cryptocurrency venture were done tongue-in-cheek." 
            "But after getting positive feedback on social media, he bought the domain dogecoin.com."
             "Meanwhile in Portland, Oregon, Billy Markus, a software developer at IBM who wanted to create a "
             "igital currency but had trouble promoting his efforts, discovered the Dogecoin buzz. "
             "Markus reached out to Palmer to get permission to build the software behind an actual Dogecoin."
             "Markus based Dogecoin's code on Luckycoin, which is itself derived from Litecoin, and initially "
             "used a randomized reward for block mining, although that was changed to a static reward in March 2014."
             " Dogecoin uses Litecoin's scrypt technology and is a Proof-of-Work (PoW) coin.Palmer and Markus launched "
             "the coin on Dec. 6, 2013. Two weeks later on Dec. 19, the value of Dogecoin jumped 300%, "
             "perhaps due to China forbidding its banks from investing in cryptocurrency")
    data = yf.download("DOGE-CAD")
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
    st.header("Dogecoin All time graph")
    st.plotly_chart(fig, use_container_width=True)