import base64

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_eth_info():

    st.header("Ethereum")

    st.write("Ethereum is a platform powered by blockchain technology that is best known for its native cryptocurrency,"
             " called ether, or ETH, or simply ethereum. The distributed nature of blockchain technology is what makes "
             "the Ethereum platform secure, and that security enables ETH to accrue value.")
    st.write("The Ethereum platform supports ether in addition to a network of decentralized apps, otherwise known as "
             "dApps. Smart contracts, which originated on the Ethereum platform, are a central component of how the "
             "platform operates. Many decentralized finance (DeFi) and other applications use smart contracts in "
             "conjunction with blockchain technology. As a cryptocurrency, Ethereum is second in market value only to "
             "Bitcoin as of January 2022.")
    st.write("Ethereum, like other cryptocurrencies, uses blockchain technology. Imagine a very long chain of blocks linked "
             "together, with all of the information about each block known to every member of the blockchain network. "
             "With every member of the network having the same knowledge of the blockchain, which functions like an "
             "electronic ledger, distributed consensus can be created and maintained about the status of the blockchain.")

    st.write("Blockchain technology creates distributed consensus about the state of the Ethereum network. New blocks are"
             " added to the very long Ethereum blockchain to process Ethereum transactions and mint new ether coins, or "
             "to execute smart contracts for Ethereum dApps.")

    st.write("The Ethereum network derives its security from the decentralized nature of blockchain technology. A vast network of computers "
             "worldwide maintains the Ethereum blockchain network, and the network requires distributed consensus—majority"
             " agreement—for any changes to be made to the blockchain. An individual or group of network participants "
             "would need to gain majority control of the Ethereum platform’s computing power—a task that would be "
             "gargantuan, if not impossible—to successfully manipulate the Ethereum blockchain.")

    st.write("The Ethereum platform can support many more applications than ETH and other cryptocurrencies. The network’s "
             "users can create, publish, monetize, and use a diverse range of applications on the Ethereum platform, and "
             "can use ETH or another cryptocurrency as payment.")

    st.header("History")

    st.write("Vitalik Buterin, who is credited with conceiving the original Ethereum concept, published a white paper "
             "to introduce Ethereum in 2013. The Ethereum platform was launched in 2015 by Buterin and Joe Lubin, "
             "founder of the blockchain software company ConsenSys. The founders of Ethereum were among the first to "
             "consider the full potential of blockchain technology, beyond just enabling the secure trading of virtual "
             "currency.")

    st.write("One notable event in Ethereum’s history is the hard fork, or split, of Ethereum and Ethereum Classic. "
             "In 2016, a group of network participants gained majority control of the Ethereum blockchain to steal more "
             "than $50 million worth of ether, which had been raised for a project called the DAO. The success of the "
             "raid was attributed to involvement by a third-party developer for the new project. While the majority of "
             "the Ethereum community opted to reverse the theft by invalidating the existing Ethereum blockchain and "
             "approving a blockchain with a revised history, a fraction of the community chose to maintain the original "
             "version of the Ethereum blockchain. That unaltered version of Ethereum permanently split to become the "
             "cryptocurrency Ethereum Classic, or ETC.")

    st.write("Since the launch of Ethereum, ether as a cryptocurrency has risen to become the second-largest cryptocurrency "
             "by market value. It is outranked only by Bitcoin.")

    st.header("The Future of Ethereum")

    st.write("Ethereum’s transition to the proof of stake protocol, which enables users to validate transactions and mint"
             " new ETH based on their ether holdings, is part of a major upgrade to the Ethereum platform known as Eth2."
             " The upgrade also adds capacity to the Ethereum network to support its growth, which helps to address chronic"
             " network congestion problems that have driven up gas fees.")

    data = yf.download("ETH-CAD")
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
    st.header("Ethereum All time graph")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Ethereum White Paper")

    with open("Ethereum_White_Paper_-_Buterin_2014.pdf", "rb") as file:
        btn = st.download_button(
            label="Click me! to download white paper",
            data=file,
            file_name="Ethereum_White_Paper_-_Buterin_2014.pdf",
            mime="application/octet-stream")

    def st_display_pdf(pdf_file):
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        # pdf_display = f'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    with st.expander(" 👁  Ethereum white paper "):
        st_display_pdf("Ethereum_White_Paper_-_Buterin_2014.pdf")