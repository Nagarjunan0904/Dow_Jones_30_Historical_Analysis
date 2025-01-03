# Dow Jones 30: Historical Analysis and Performance Metrics

## Author
**Nagarjunan Saravanan**

## Date
**10-12-2024**

## Description
This project analyzes historical data of the Dow Jones 30 stocks using Python and various libraries like `yfinance`, `matplotlib`, and `pandas`. The primary objective is to visualize stock performance and compute key performance metrics like cumulative returns, volatility, and average trading volume.

---

## Prerequisites
Ensure you have Python installed along with the following libraries:

- `yfinance`
- `matplotlib`
- `pandas`

You can install the dependencies using the following command:

```bash
pip install yfinance matplotlib pandas
```

---

## Data Sources
The historical stock data is fetched from **Yahoo Finance** for the Dow Jones 30 companies from January 1, 2020, to December 31, 2023.

---

## Dow Jones 30 Stocks
The following companies are included in the analysis:

```
AAPL, MSFT, JPM, V, UNH, JNJ, WMT, PG, DIS, INTC,
VZ, KO, CSCO, HD, MRK, TRV, CVX, GS, NKE, AXP,
IBM, MCD, BA, CAT, MMM, WBA, DOW, AMGN, CRM, HON
```

---

## Features
1. **Visualization:**
   - Line plots for comparing key metrics (`Open`, `Close`, `High`, `Low`, `Volume`) across all stocks.

2. **Performance Metrics:**
   - **Average Closing Price:** Mean of closing prices for each stock.
   - **Cumulative Returns:** Cumulative returns calculated using daily percentage changes in closing prices.
   - **Volatility:** Standard deviation of daily percentage changes in closing prices.
   - **Average Volume:** Mean of daily trading volumes for each stock.

---

## Code Walkthrough

### Fetching Historical Data
The historical data is fetched using `yfinance` for the Dow Jones 30 stocks from January 1, 2020, to December 31, 2023:

```python
import yfinance as yf

# Define stock groups
dow_jones_30 = [
    "AAPL", "MSFT", "JPM", "V", "UNH", "JNJ", "WMT", "PG", "DIS", "INTC",
    "VZ", "KO", "CSCO", "HD", "MRK", "TRV", "CVX", "GS", "NKE", "AXP",
    "IBM", "MCD", "BA", "CAT", "MMM", "WBA", "DOW", "AMGN", "CRM", "HON"
]

# Download historical data
data = yf.download(dow_jones_30, start="2020-01-01", end="2023-12-31", group_by="ticker")
```

### Visualization of Metrics
For each metric (`Open`, `Close`, `High`, `Low`, `Volume`), line plots are generated for comparison across all stocks:

```python
import matplotlib.pyplot as plt

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
```

### Average Closing Price
The mean closing price for each stock is calculated as follows:

```python
import pandas as pd

avg_closing_price = pd.DataFrame({
    ticker: data[ticker]["Close"].mean() for ticker in dow_jones_30 if ticker in data
}, index=["Average Closing Price"]).T

print(avg_closing_price)
```

### Cumulative Returns
Cumulative returns are computed using daily percentage changes in closing prices:

```python
cumulative_returns = data.xs("Close", level=1, axis=1).pct_change().add(1).cumprod()
print(cumulative_returns.tail())  # Show the last 5 rows of cumulative returns
```

### Volatility
Volatility is calculated as the standard deviation of daily percentage changes in closing prices:

```python
volatility = data.xs("Close", level=1, axis=1).pct_change().std()
print(volatility)
```

### Average Volume
The mean trading volume for each stock is calculated as follows:

```python
avg_volume = data.xs("Volume", level=1, axis=1).mean()
print(avg_volume)
```

---

## Output
Separate line plots for `Open`, `Close`, `High`, `Low`, and `Volume` metrics of Dow Jones 30 stocks, along with data tables for average closing prices, cumulative returns, volatility, and average volume.

---

## Example Results
### Average Closing Price:
```
       Average Closing Price
AAPL                 134.25
MSFT                 243.18
...
```

### Cumulative Returns (Last 5 Rows):
```
                 AAPL      MSFT       ...
2023-12-27  3.021654  2.659823    ...
...
```

### Volatility:
```
AAPL    0.0123
MSFT    0.0142
...
```

### Average Volume:
```
AAPL    98765432
MSFT    87654321
...
```

---

## How to Run
1. Clone the repository.
2. Install the required libraries.
3. Run the Python script to generate visualizations and metrics.

---

## License
This project is licensed under the MIT License.

