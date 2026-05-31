import yfinance as yf

def fetch_nifty_data(period):

    nifty = yf.Ticker("^NSEI")

    return nifty.history(period=period)


nifty = yf.Ticker("^NSEI")

print("Fetching data...")

df = fetch_nifty_data("10y")

print("Data received!")

print(df.head())
print(df.columns)
