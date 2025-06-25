# Stock Price Trend Analysis - Basic EDA

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Disable warnings
import warnings
warnings.filterwarnings("ignore")

# Set the stock and date range
ticker = 'RELIANCE.NS'  # You can try 'TCS.NS', 'AAPL', 'TSLA', etc.
start_date = '2022-01-01'
end_date = '2023-12-31'

# Download stock data
df = yf.download(ticker, start=start_date, end=end_date)

# Show the first 5 rows
print("📊 Data Preview:")
print(df.head())

# Plot the closing price trend
plt.figure(figsize=(12,6))
sns.lineplot(x=df.index, y=df['Close'].squeeze())
plt.title(f'{ticker} - Stock Price Trend (Close)', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Closing Price (₹)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("price_trend.png")
plt.show()


# Moving Average (50-day)
df['MA50'] = df['Close'].rolling(window=50).mean()

# Plot with MA
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['MA50'], label='50-day MA', color='orange')
plt.title(f'{ticker} - Close Price vs 50-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("MA.png")
plt.show()


# Calculate Daily Returns
df['Daily Return (%)'] = df['Close'].pct_change() * 100

# Plot Volatility (Daily Returns)
plt.figure(figsize=(12,6))
sns.histplot(df['Daily Return (%)'].dropna(), bins=100, kde=True, color='skyblue')
plt.title(f'{ticker} - Daily Return % Distribution')
plt.xlabel('Daily Return (%)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig("volt.png")
plt.show()

# Plot trading volume over time
plt.figure(figsize=(12,6))
sns.lineplot(x=df.index, y=df['Volume'].squeeze(), color='green')
plt.title("Stock Volume Traded Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.tight_layout()
plt.savefig("volume_trend.png")
plt.show()


import plotly.graph_objects as go

# Candlestick Chart
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close']
)])
fig.update_layout(title=f'{ticker} Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
plt.savefig("candle.png")