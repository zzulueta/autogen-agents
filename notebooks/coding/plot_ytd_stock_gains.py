# filename: plot_ytd_stock_gains.py

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Define the stocks to download. We would like to see Tesla and Nvidia.
stocks = ["NVDA", "TSLA"]

# We want to see stocks from the beginning of this year to current date
start_date = '2024-01-01'
end_date = '2024-07-01'

# Use pandas_reader.data.DataReader to load the desired data.
data = yf.download(stocks, start=start_date, end=end_date)

# Getting just the adjusted closing prices. 
close = data['Adj Close']

# Getting all weekdays in the desired date range
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# Align existing prices series with our new all_weekdays series
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
close = close.fillna(method='ffill')

# calculate gains from the starting date
gains = close.pct_change().cumsum()

# plot the data
gains.plot()

# save figure to file
plt.savefig('ytd_stock_gains.png')
plt.show()