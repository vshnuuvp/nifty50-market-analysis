import yfinance as yf

def get_stock_return(symbol, period):

    stock = yf.Ticker(symbol)

    df = stock.history(period=period)

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    return ((last_close - first_close) / first_close) * 100

def get_stock_volatility(symbol, period):

    stock = yf.Ticker(symbol)

    df = stock.history(period=period)

    daily_returns = df["Close"].pct_change()

    volatility = daily_returns.std() * 100

    return volatility


def compare_volatility():

    stocks = {
        "TCS": "TCS.NS",
        "Infosys": "INFY.NS",
        "Reliance": "RELIANCE.NS",
        "HDFC Bank": "HDFCBANK.NS",
        "ICICI Bank": "ICICIBANK.NS"
    }

    results = {}

    for company, symbol in stocks.items():

        volatility = get_stock_volatility(symbol, "1y")

        results[company] = volatility

    return results



def risk_return_dashboard():

    stocks = {
        "TCS": "TCS.NS",
        "Infosys": "INFY.NS",
        "Reliance": "RELIANCE.NS",
        "HDFC Bank": "HDFCBANK.NS",
        "ICICI Bank": "ICICIBANK.NS"
    }

    results = []

    for company, symbol in stocks.items():

        stock_return = get_stock_return(symbol, "1y")

        volatility = get_stock_volatility(symbol, "1y")

        results.append(
            (company, stock_return, volatility)
        )

    return results
