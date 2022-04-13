
import yfinance as yf
import plotly.graph_objects as go



def bitcoin_24_data():
                fig1 = go.Figure()
                data = yf.download(tickers='BTC-CAD', period='22h', interval='15m')
                fig1.add_trace(go.Candlestick(x=data.index,
                                             open=data['Open'],
                                             high=data['High'],
                                             low=data['Low'],
                                             close=data['Close'], name='market data'))
                fig1.update_layout(
                    title='Bitcoin live share price evolution',
                    yaxis_title='Bitcoin Price (CAD Dollars)')

                # X-Axes
                fig1.update_xaxes(
                    rangeslider_visible=True,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=15, label="15m", step="minute", stepmode="backward"),
                            dict(count=45, label="45m", step="minute", stepmode="backward"),
                            dict(count=1, label="HTD", step="hour", stepmode="todate"),
                            dict(count=6, label="6h", step="hour", stepmode="backward"),
                            dict(step="all")
                        ])
                    )
                )
                fig1.show()