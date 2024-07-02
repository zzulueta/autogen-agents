# filename: nvidia_stock.py

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the ticker symbol
tickerSymbol = 'NVDA'

# Get data for the past month
end_date = datetime(2024, 7, 1)
start_date = end_date - timedelta(days=30)

# Get the data
tickerData = yf.Ticker(tickerSymbol)
hist_data = tickerData.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

# Print the data
print(hist_data)

# Visualize the closing prices
plt.figure(figsize=(14, 7))
plt.plot(hist_data['Close'], label='Close Price')
plt.title('Nvidia Stock Price Performance in the Past Month')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()