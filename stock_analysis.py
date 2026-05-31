import yfinance as yf

def get_stock_return(symbol, period):

    stock = yf.Ticker(symbol)

    df = stock.history(period=period)

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    return ((last_close - first_close) / first_close) * 100
