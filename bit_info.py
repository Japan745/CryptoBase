import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import base64

def get_bit_info():
    st.header("Bitcoin")
    st.write("Bitcoin is a digital currency which operates free of any central control or the oversight of banks "
             "or governments. Instead, it relies on peer-to-peer software and cryptography. Bitcoins can currently"
             " be subdivided by seven decimal places: a thousandth of a bitcoin is known as a milli and a hundred "
             "millionth of a bitcoin is known as a satoshi. In truth there is no such thing as a bitcoin or a wallet, "
             "just agreement among the network about ownership of a coin. A private key is used to prove ownership of "
             "funds to the network when making a transaction. A person could simply memorise their private key and need"
             " nothing else to retrieve or spend their virtual cash, a concept which is known as a “brain wallet”.")
    st.header("History")
    st.write("The word bitcoin was defined in a white paper published on 31 October 2008. On 31 October 2008, "
             "a link to a paper authored by Satoshi Nakamoto titled Bitcoin: A Peer-to-Peer Electronic Cash System"
             " was posted to a cryptography mailing list. Nakamoto implemented the bitcoin software as open-source"
             " code and released it in January 2009.  Nakamoto's identity remains unknown. On 3 January 2009, the"
             " bitcoin network was created when Nakamoto mined the starting block of the chain, known as the "
             "genesis block")
    st.header("Block Chain")
    st.write("Bitcoin is a network that runs on a protocol known as the blockchain. While it does not mention "
             "the word blockchain, a 2008 paper by a person or people calling themselves Satoshi Nakamoto first "
             "described the use of a chain of blocks to verify transactions and engender trust in a network.The "
             "bitcoin blockchain is a public ledger that records bitcoin transactions. It is implemented as a "
             "chain of blocks, each block containing a hash of the previous block up to the genesis blockin the "
             "chain. A network of communicating nodes running bitcoin software maintains the blockchain. "
             "Transactions of the form payer X sends Y bitcoins to payee Z are broadcast to this network using "
             "readily available software applications. In the blockchain, bitcoins are registered to bitcoin "
             "addresses. Creating a bitcoin address requires nothing more than picking a random valid private "
             "key and computing the corresponding bitcoin address. Blockchain's versatility has caught the eye "
             "of governments and private corporations; indeed, some analysts believe that blockchain technology "
             "will ultimately be the most impactful aspect of the cryptocurrency craze.")
    st.header("Software Implementation")
    st.write("Bitcoin Core is free and open-source software that serves as a bitcoin node (the set of which form"
             " the bitcoin network) and provides a bitcoin wallet which fully verifies payments. It is considered"
             " to be bitcoin's reference implementation. Initially, the software was published by Satoshi Nakamoto"
             " under the name Bitcoin, and later renamed to Bitcoin Core to distinguish it from the network."
             " It is also known as the Satoshi client. Bitcoin Core includes a transaction verification engine and "
             "connects to the bitcoin network as a full node. Moreover, a cryptocurrency wallet, which can be used to "
             "transfer funds, is included by default. The wallet allows for the sending and receiving of bitcoins. "
             "It does not facilitate the buying or selling of bitcoin. It allows users to generate QR codes to receive "
             "payment. The software validates the entire blockchain, which includes all bitcoin transactions ever. "
             "This distributed ledger which has reached more than 235 gigabytes in size as of Jan 2019, must be"
             " downloaded or synchronized before full participation of the client may occur. Although the complete "
             "blockchain is not needed all at once since it is possible to run in pruning mode.")
    data = yf.download("BTC-CAD")
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
    st.header("Bitcoin All time graph")
    st.plotly_chart(fig, use_container_width=True)


    st.header("Bitcoin White Paper")

    with open("bitcoin.pdf", "rb") as file:
        btn=st.download_button(
        label="Click me! to download white paper",
        data=file,
        file_name="bitcoin.pdf",
        mime="application/octet-stream")


    def st_display_pdf(pdf_file):
        with open(pdf_file,"rb") as f:
            base64_pdf=base64.b64encode(f.read()).decode('utf-8')
        #pdf_display = f'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display,unsafe_allow_html=True)


    with st.expander(" 👁  Bitcoin white paper "):
        st_display_pdf("bitcoin.pdf")

    # def show_pdf(file_path):
    #     with open(file_path, "rb") as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #     pdf_display = f'<iframe src="bitcoin/pdf;base64,{base64_pdf}" width="800" height="800" type="bitcoin/pdf"></iframe>'
    #     st.markdown(pdf_display, unsafe_allow_html=True)
    #
    # show_pdf('bitcoin.pdf')