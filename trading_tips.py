import plotly.graph_objs as go
import yfinance as yf
import streamlit as st
import pandas as pd


def trading_tips():
    st.warning("NOTE :-  The Predicted values of cryptocurrencies are forecasted and are for your reference so it doesn't guarantee future values."
               "Please do a research before taking any further decision based on this forecasted values.")

    with st.form(key='my_form'):
            crypto = st.selectbox('Select Cryptocurrency',
                              ['BTC', 'ETH', 'XLM', 'USDT', 'BCH', 'LTC', 'DOT', 'DOGE', 'ADA', 'SHIB'])
            submit_button = st.form_submit_button(label='Submit')

    if submit_button:

        if crypto == "BTC":
                st.info("Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='BTC-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_layout( title="Bitcoin trading",
                    xaxis_title="Date",
                     yaxis_title="Canadian dollar",)
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "ETH":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='ETH-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "XLM":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='XLM-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "USDT":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='USDT-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "BCH":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='BCH-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "LTC":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='LTC-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "DOT":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='DOT-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "DOGE":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='DOGE-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "ADA":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='ADA-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)

        if crypto == "SHIB":
                st.info(
                "Info : If yellow line uppercrosses the line blue line means it's time to BUY and if yellow line lowercrosses the blue line means its time to SELL")
                data = yf.download(tickers='SHIB-CAD', period='8d', interval='90m')
                data['MA5'] = data['Close'].rolling(5).mean()
                data['MA20'] = data['Close'].rolling(20).mean()
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                             open=data['Open'],
                             high=data['High'],
                             low=data['Low'],
                             close=data['Close'], name='market data'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], line=dict(color='blue', width=1.5), name='Long Term MA'))
                fig.add_trace(go.Scatter(x=data.index, y=data['MA5'], line=dict(color='orange', width=1.5), name='Short Term MA'))
                fig.update_xaxes(
                     rangeslider_visible=True,
                     rangeselector=dict(
                      buttons=list([
                         dict(count=3, label="3d", step="day", stepmode="backward"),
                         dict(count=5, label="5d", step="day", stepmode="backward"),
                         dict(count=7, label="WTD", step="day", stepmode="todate"),
                         dict(step="all")
                         ])
                    )
                 )

                st.plotly_chart(fig,use_container_width=True)