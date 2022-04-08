import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_lite_info():
    st.header("Lite coin")
    st.write("Litecoin (LTC) is a cryptocurrency that was designed to provide fast, secure and"
             " low-cost payments by leveraging the unique properties of blockchain technology.")
    st.header("History")
    st.write("The cryptocurrency was created based on the Bitcoin (BTC) protocol, "
             "but it differs in terms of the hashing algorithm used, hard cap, "
             "block transaction times and a few other factors.")
    st.write( "Litecoin has a block time of just 2.5 minutes and extremely low transaction fees, making it suitable for micro-transactions"
             " and point-of-sale payments.Litecoin was released via an open-source client on GitHub "
             "on Oct. 7, 2011, and the Litecoin Network went live five days later on Oct. 13, 2011. "
             "Since then, it has exploded in both usage and acceptance among merchants and has counted"
             " among the top ten cryptocurrencies by market capitalization for most of its existence."
             "The cryptocurrency was created by Charlie Lee, a former Google employee, who intended Litecoin to be"
             "a lite version of Bitcoin,in that it features many of the same properties as "
             "Bitcoin—albeit  lighter in weight.")
    st.header("Founders of Litecoin")
    st.write("As we previously touched on, Litecoin was founded by Charlie Lee, an early cryptocurrency"
             " adopter and a name held in high regard in the cryptocurrency industry.")
    st.write("Charlie Lee, also known as “Chocobo,” is an early Bitcoin miner and computer scientist, "
             "who was a former software engineer for Google. In addition, Charlie Lee held the role"
             " of director of engineering at Coinbase between 2015 and 2017 before moving on to other"
             " ventures.Today, Charlie Lee is an outspoken advocate of cryptocurrencies and is the "
             "managing director of the Litecoin Foundation—a ""non-profit organization that"
             " works alongside the Litecoin Core Development team to help advance Litecoin.")
    st.write("Besides Lee, the Litecoin Foundation also includes three other individuals on "
             "the board of directors: Xinxi Wang, Alan Austin and Zing Yang — all of which are "
             "accomplished in their own right.")
    st.header("Secure Network")
    st.write("As a blockchain-based cryptocurrency, Litecoin is secured by incredibly"
             " strong cryptographic defenses — making it practically impossible to crack.Like Bitcoin "
             "and several other cryptocurrencies, Litecoin uses the PoW consensus algorithm "
             "to ensure transactions are confirmed quickly and without errors. "
             "The combined strength of the Litecoin mining network prevents double-spends and a"
             " range of other attacks, while ensuring the network has 100% uptime.")
    data = yf.download("LTC-CAD")
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
    st.header("Litecoin All time graph")
    st.plotly_chart(fig, use_container_width=True)