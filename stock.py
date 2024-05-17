import pandas as pd
from alpha_vantage.timeseries import TimeSeries

import matplotlib.pyplot as plt

# Set your Alpha Vantage API key
api_key = 'YOUR_API_KEY'

# Define the stock symbol and output size
symbol = 'TSLA'
output_size = 'full'

# Initialize the TimeSeries object
ts = TimeSeries(key=api_key, output_format='pandas')

# Get the daily stock data for Tesla
data, meta_data = ts.get_daily(symbol=symbol, outputsize=output_size)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Plot the closing prices
plt.plot(df.index, df['4. close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Tesla Stock Price')
plt.xticks(rotation=45)
plt.show()
