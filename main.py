from analysis import calculate_return
from analysis import calculate_cagr


def market_overview():

    print("\n" + "=" * 40)
    print("NIFTY 50 MARKET OVERVIEW")
    print("=" * 40)

    print(f"1 Month Return : {round(calculate_return('1mo'),2)}%")
    print(f"6 Month Return : {round(calculate_return('6mo'),2)}%")
    print(f"1 Year Return  : {round(calculate_return('1y'),2)}%")
    print(f"5 Year Return  : {round(calculate_return('5y'),2)}%")
    print(f"10 Year Return : {round(calculate_return('10y'),2)}%")

    print()

    print(f"5 Year CAGR : {round(calculate_cagr('5y',5),2)}%")
    print(f"10 Year CAGR : {round(calculate_cagr('10y',10),2)}%")


market_overview()

from stock_analysis import get_stock_return

print("TCS Return:")

print(round(get_stock_return("TCS.NS", "1y"), 2))

stocks = {
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "Reliance": "RELIANCE.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS"
}

results = {}

for company, symbol in stocks.items():

    stock_return = get_stock_return(symbol, "1y")

    results[company] = stock_return

print(results)

best_stock = max(results, key=results.get)

print("Best Stock:", best_stock)

worst_stock = min(results, key=results.get)

print("Worst Stock:", worst_stock)

sorted_stocks = sorted(
    results.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nTOP PERFORMERS")

for company, stock_return in sorted_stocks:

    print(f"{company}: {round(stock_return, 2)}%")


from stock_analysis import get_stock_volatility

print(get_stock_volatility("TCS.NS", "1y"))

from stock_analysis import compare_volatility

volatility_results = compare_volatility()

print("\nVOLATILITY ANALYSIS")
print("=" * 30)

for company, volatility in volatility_results.items():

    print(f"{company}: {round(volatility, 2)}%")

most_volatile = max(volatility_results, key=volatility_results.get)

least_volatile = min(volatility_results, key=volatility_results.get)

print("\nMost Volatile:", most_volatile)
print("Least Volatile:", least_volatile)


from stock_analysis import risk_return_dashboard

dashboard = risk_return_dashboard()

print("\nRISK VS RETURN ANALYSIS")
print("=" * 50)

for company, stock_return, volatility in dashboard:

    print(
        f"{company:<12} "
        f"{round(stock_return,2):>10}% "
        f"{round(volatility,2):>12}%"
    )
