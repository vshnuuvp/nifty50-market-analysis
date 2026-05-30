import yfinance as yf

print("Starting...")

nifty = yf.Ticker("^NSEI")

print("Fetching data...")

df = nifty.history(period="1mo")

print("Data received!")

print(df.head())
print(df.columns)

# first_close = df["Close"].iloc[0]
#
# last_close = df["Close"].iloc[-1]
#
# print("First Close:", first_close)
# print("Last Close:", last_close)
#
# return_pct = ((last_close - first_close) / first_close) * 100
#
# print("Return %:", round(return_pct, 2))


def calculate_return(period):

    df = nifty.history(period=period)

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    return ((last_close - first_close) / first_close) * 100


# print("1 Month:", round(calculate_return("1mo"),2))
# print("6 Month:", round(calculate_return("6mo"),2))
# print("1 Year:", round(calculate_return("1y"),2))
# print("5 Year:", round(calculate_return("5y"),2))
# print("10 Year:", round(calculate_return("10y"),2))

def market_overview():

    print("\n" + "="*40)
    print("NIFTY 50 MARKET OVERVIEW")
    print("="*40)

    print(f"1 Month Return : {round(calculate_return('1mo'),2)}%")
    print(f"6 Month Return : {round(calculate_return('6mo'),2)}%")
    print(f"1 Year Return  : {round(calculate_return('1y'),2)}%")
    print(f"5 Year Return  : {round(calculate_return('5y'),2)}%")
    print(f"10 Year Return : {round(calculate_return('10y'),2)}%")

# market_overview()

def calculate_cagr(period, years):

    df = nifty.history(period=period)

    first_close = df["Close"].iloc[0]
    last_close = df["Close"].iloc[-1]

    cagr = ((last_close / first_close) ** (1 / years) - 1) * 100

    return cagr

print("5 Year CAGR:", round(calculate_cagr("5y", 5), 2))
print("10 Year CAGR:", round(calculate_cagr("10y", 10), 2))