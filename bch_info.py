import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_bch_info():
    st.header("Bitcoin Cash")
    st.write("Bitcoin Cash is a peer-to-peer electronic cash system that aims to become sound global"
             " money with fast payments, micro fees, privacy, and high transaction capacity (big blocks)."
             " In the same way that physical money, such as a dollar bill, is handed directly to the person "
             "being paid, Bitcoin Cash payments are sent directly from one person to another.”.")
    st.write("As a permissionless, decentralized cryptocurrency, Bitcoin Cash requires "
             "no trusted third parties and no central bank. Unlike traditional fiat money,"
             " Bitcoin Cash does not depend on monetary middlemen such as banks and payment processors."
             " Transactions cannot be censored by governments or other centralized corporations."
             " Similarly, funds cannot be seized or frozen — because financial third parties have "
             "no control over the Bitcoin Cash network.")
    st.header("Use of Bitcoin Cash")
    st.write("Bitcoin Cash combines gold-like scarcity with the spendable nature of cash. "
             "With a limited total supply of 21 million coins, Bitcoin Cash is provably scarce and, "
             "like physical cash, can be easily spent. Transactions are fast with transaction fees "
             "typically less than a tenth of a cent. Anybody can accept Bitcoin Cash payments with a "
             "smartphone or computer.Bitcoin Cash has various use cases. "
             "In addition to peer-to-peer payments between individuals, Bitcoin Cash "
             "can be used to pay participating merchants for goods and services in-store and online."
             " Very low fees enable new micro-transaction economies, such as tipping content creators "
             "and rewarding app users a few cents. Bitcoin Cash also reduces the fees and settlement"
             " times for remittances and cross-border trade. Other use cases include tokens, simplified "
             "smart contracts, and private payments with tools such as CashShuffle and CashFusion.Bitcoin Cash"
             " has various use cases. In addition to peer-to-peer payments between individuals,"
             " Bitcoin Cash can be used to pay participating merchants for goods and services in-store and online."
             "Very low fees enable new micro-transaction economies, such as tipping content creators and "
             "rewarding app users a few cents. Bitcoin Cash also reduces the fees and settlement times for"
             " remittances and cross-border trade. Other use cases include tokens, simplified smart contracts, "
             "and private payments with tools such as CashShuffle and CashFusion.")
    st.header("Is Bitcoin Cash different from Bitcoin?")
    st.write("In 2017, the Bitcoin project and its community split in two over concerns about Bitcoin’s scalability."
             " The result was a hard fork which created Bitcoin Cash, a new cryptocurrency considered by "
             "supporters to be the legitimate continuation of the Bitcoin project as peer-to-peer electronic cash. "
             "All Bitcoin holders at the time of the fork (block 478,558) automatically became owners of Bitcoin Cash."
             " Bitcoin, which was invented by the pseudonymous Satoshi Nakomoto remains a separate cryptocurrency.")
    st.write("Unlike Bitcoin (BTC), Bitcoin Cash aims to scale so it can meet the demands of a global payment system."
             " At the time of the split, the Bitcoin Cash block size was increased from 1MB to 8MB. "
             "An increased block size means Bitcoin Cash can now handle significantly more transactions "
             "er second (TPS) while keeping fees extremely low, solving the issues of payment delays and high fees"
             " experienced by some users on the Bitcoin BTC network.As of October 2021, Bitcoin Cash has a block size of 32MB,"
             " compared to Bitcoin’s block size of 1MB.")

    data = yf.download("BCH-CAD")
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
    st.header("Bitcoin Cash All time graph")
    st.plotly_chart(fig, use_container_width=True)