from data_fetcher import fetch_nifty_data

def calculate_return(period):

    df = fetch_nifty_data(period)

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    return ((last_close - first_close) / first_close) * 100


def calculate_cagr(period, years):

    df = fetch_nifty_data(period)

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    return ((last_close / first_close) ** (1 / years) - 1) * 100
