'''
Title: Dow Jones 30: Historical Analysis and Performance Metrics
Author: Nagarjunan Saravanan
Date: 10-12-2024
Output: Separate line plots for Open, Close, High, Low, and Volume metrics of Dow Jones 30 stocks, along with data tables for average closing prices, cumulative returns, volatility, and average volume.
'''

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define stock groups (Dow Jones 30 as an example)
dow_jones_30 = [
    "AAPL", "MSFT", "JPM", "V", "UNH", "JNJ", "WMT", "PG", "DIS", "INTC",
    "VZ", "KO", "CSCO", "HD", "MRK", "TRV", "CVX", "GS", "NKE", "AXP",
    "IBM", "MCD", "BA", "CAT", "MMM", "WBA", "DOW", "AMGN", "CRM", "HON"
]

# Fetch historical data for Dow Jones stocks
data = yf.download(dow_jones_30, start="2020-01-01", end="2023-12-31", group_by="ticker")

# Plot comparison graphs for specific columns
columns_to_compare = ["Open", "Close", "High", "Low", "Volume"]
for column in columns_to_compare:
    plt.figure(figsize=(14, 7))
    for ticker in dow_jones_30:
        try:
            plt.plot(data[ticker][column], label=ticker)
        except KeyError:
            print(f"Data for {ticker} is unavailable for {column}")
    plt.title(f'Comparison of {column} for Dow Jones 30 Stocks')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0), fontsize='small')
    plt.tight_layout()
    plt.show()

# Example Calculation: Average Closing Price for Dow Jones
avg_closing_price = pd.DataFrame({
    ticker: data[ticker]["Close"].mean() for ticker in dow_jones_30 if ticker in data
}, index=["Average Closing Price"]).T

print(avg_closing_price)

#calculating cumulative returns
cumulative_returns = data.xs("Close", level=1, axis=1).pct_change().add(1).cumprod()
print(cumulative_returns.tail())  # Show the last 5 rows of cumulative returns

# calculating Volatility
volatility = data.xs("Close", level=1, axis=1).pct_change().std()
print(volatility)

#Calculating Average Volume
avg_volume = data.xs("Volume", level=1, axis=1).mean()
print(avg_volume)
