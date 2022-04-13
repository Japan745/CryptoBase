import base64

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go

def get_dot_info():
    st.header("Polkadot")
    st.write("Polkadot is an open-source sharded multichain protocol that connects and secures"
             " a network of specialized blockchains, facilitating cross-chain transfer of any "
             "data or asset types, not just tokens, thereby allowing blockchains to be interoperable"
             " with each other. Polkadot was designed to provide a foundation for a decentralized internet"
             " of blockchains, also known as Web3.")
    st.write("Polkadot is known as a layer-0 metaprotocol because it underlies and describes"
             " a format for a network of layer 1 blockchains known as parachains (parallel chains)."
             " As a metaprotocol, Polkadot is also capable of autonomously and forklessly updating "
             "its own codebase via on-chain governance according to the will of its token holder community.")
    st.write("Polkadot provides a foundation to support a decentralized web, controlled by its users, "
             "and to simplify the creation of new applications, institutions and services.")
    st.write("The Polkadot protocol can connect public and private chains, "
             "permissionless networks, oracles and future technologies, allowing "
             "these independent blockchains to trustlessly share information and"
             " transactions through the Polkadot Relay Chain (explained further down.")
    st.write("Polkadot’s native DOT token serves three clear purposes: staking for operations and security, "
             "facilitating network governance, and bonding tokens to connect parachains .")
    st.header("History")
    st.write("Polkadot is the flagship protocol of Web3 Foundation, a Swiss Foundation with"
             " a mission to facilitate an open-source, fully functional and user-friendly "
             "decentralized web.Polkadot’s founders are Dr. Gavin Wood, Robert Habermeier and Peter Czaban."
             "Wood, Web3 Foundation’s president, is the most well-known of the trio thanks to his industry "
             "influence as Ethereum co-founder, Parity Technologies founder and the creator of the smart "
             "contract coding language Solidity. Wood is also credited with coining the term Web3.Habermeier is a Thiel Fellow and "
             "accomplished blockchain and cryptography researcher and developer. Czaban is the former Technology "
             "Director at Web3 Foundation, with a wealth of experience across highly specialized fintech industries.")
    st.header("What Makes Polkadot Unique?")
    st.write("Polkadot is a sharded multichain network, meaning it can process many transactions on several chains in parallel "
             "(“parachains”). This parallel processing power improves scalability.Custom blockchains are quick "
             "and easy to develop using the Substrate framework and Substrate blockchains are designed to"
             " be easy to connect to Polkadot's network. The network is also highly flexible and adaptive,"
             " allowing the sharing of information and functionality between participants. Polkadot can "
             "be automatically upgraded without the need for a fork in order to implement new features or"
             " remove bugs.The network has a highly sophisticated user-driven governance "
             "system where all token holders have a vote in how the network is run. "
             "Teams can customize their own blockchain’s governance on Polkadot based on their "
             "needs and evolving conditions. Nominators, validators, and collators all fulfil "
             "various duties to help secure and maintain the network and eradicate bad behavior.")
    data = yf.download("DOT-CAD")
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
    st.header("Polkadot All time graph")
    st.plotly_chart(fig, use_container_width=True)

    st.header("Polkadot White Paper")

    with open("Polkadot-DOT-Whitepaper.pdf", "rb") as file:
        btn = st.download_button(
            label="Click me! to download white paper",
            data=file,
            file_name="Polkadot-DOT-Whitepaper.pdf",
            mime="application/octet-stream")

    def st_display_pdf(pdf_file):
        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    with st.expander(" 👁  Polkadot white paper "):
        st_display_pdf("Polkadot-DOT-Whitepaper.pdf")