import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_xlm_info():

    st.header("Stellar (XLM)")

    st.write("Stellar Lumens (XLM) is the native cryptocurrency of Stellar, which is a blockchain-based payment network "
             "whose leaders see it as a faster and cheaper way to make global payments than the likes of remittance "
             "giants. MoneyGram and Western Union. Those companies charge high fees and can take days to process a "
             "transaction.")

    st.header("History")

    st.write("In 2021, Stellar even said it was interested in buying MoneyGram.The platform also boasts its own "
             "decentralized exchange for trading crypto and other assets. For non-crypto assets like gold, verified "
             "financial institutions known as \"Stellar Anchors\" act like banks and hold the deposits.")

    st.write("The platform then issues tokens tied to those assets to the depositor and returns the assets upon "
             "withdrawal/redemption of the tokens. That all takes place on the Stellar ledger.")

    st.write("In 2014, Stellar raised $35 million in its initial token sale of its native token, XLM. Stellar's supply "
             "is managed by the nonprofit Stellar Development Foundation (SDF), which steers development of the protocol."
             " When Stellar started, 100 billion XLMs were created with an annual inflation rate of 1 percent. The "
             "inflation rate has since been removed.")
    st.write("In 2019, Stellar burned, or removed, more than 50 percent of its supply, slashing its total supply cap to "
             "50 billion. Prices jumped by more than 14% within an hour of the announcement, as the remaining tokerls "
             "in circulation became scarcer. XLM's price hit an all-time high of dollar 0.86 during the 2017 crypto bull "
             "run. In the following bear market, XLM's price sank to a low of dollar 0.03. Not long after bitcoin's price "
             "hit a then-high of 63,500, XLM's price reached another peak of 0.73 in May 2021.")

    st.header("How Stellar Work?")

    st.write("Though Stellar borrows its ideas from Bitcoin, its main distinction from Bitcoin is that it's secured by a "
             "different consensus protocol. Bitcoin uses proof-of-work to secure the blockchain and make sure that the "
             "decentralized network is able to come to an agreement over which transactions are valid.")

    st.write("Instead of proof-of-work, Stellar deploys the \"Stellar Consensus Protocol\" (SCP), which was invented "
             "by Stellar chief scientist David Mazières in 2015. Under SC, a set group of \"trustworthy\" nodes are "
             "responsible for validating transactions and blocks, making sure no one is printing free money for themselves.")

    st.write("This set of trustworthy nodes is voted on periodically. Anyone on the network can participate by running a"
             " node. Each node votes on whom they believe is trustworthy. The winners (whoever gets the majority of votes) "
             "are responsible for validating transactions. Because SC doesn't require costly mining machines running "
             "computations all day, it's a far more eco-friendly blockchain project than other blockchains. SC is also "
             "how Stellar can support faster and cheaper transactions.")

    st.write("Still, some researchers argue that algorithms like Stellar's aren't as secure and open as Bitcoin's proof-of-work."
             "For instance, one research paper from South Korea's Advanced Institute of Science and Technology, called "
             "Stellar \"significantly centralized.\" Because of those issues, the Stellar network has crashed at least "
             "twice over the last couple of years, preventing users from sending payments across the network.")

    st.header("Key Events and management")

    st.write("Jed McCaleb, a computer programmer and former chief technology officer at Ripple, left Ripple in 2013 "
             "due to a disagreement about the cryptocurrency company's proposed direction. He started Stellar by forming"
             " a new blockchain that split off from Ripple's blockchain.")
    st.write("In 2014, McCaleb launched the Stellar Development Fund in collaboration with Patrick Collison, the CEO "
             "of payment software company Stripe, and Stripe invested $3 million in Stellar. With its ambitions to "
             "compete with big remittance companies, Stellar has joined forces with several global financial "
             "institutions over the years, and in 2020, German bank Bankhaus von der Heydt, one of the oldest banks in "
             "the world, issued a stablecoin based on Stellar.")




    data = yf.download("XLM-CAD")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(data.index), y=list(data['Adj Close'])))
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
    st.header("Stellar (XLM) All time graph")
    st.plotly_chart(fig, use_container_width=True)