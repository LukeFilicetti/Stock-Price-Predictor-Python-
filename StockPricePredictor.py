# 
# Author: Luke Filicetti
# Description: 
# This program predicts the stock price of a given company (e.g., AAPL) using Linear Regression. 
# It fetches historical stock data using the 'yfinance' library and uses this data to fit a Linear Regression model. 
# The model then predicts future stock prices for the next 10 days. 
# The historical and predicted prices are visualized using matplotlib, displaying the trends over time.
#

# Import necessary libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Fetch historical stock data
def get_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    df = stock.history(period="1y")  # Get 1 year of stock data
    df = df[['Close']].reset_index()  # Use only the closing price and reset the index
    df['Days'] = np.arange(len(df))  # Add a 'Days' column to represent each day
    return df

# Predict future prices using Linear Regression
def predict_stock_prices(df):
    X = df[['Days']]  # This is now a DataFrame, not a numpy array
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array(range(len(df), len(df) + 10)).reshape(-1, 1)
    future_days_df = pd.DataFrame(future_days, columns=["Days"])  # Add column name here
    future_prices = model.predict(future_days_df)  # Use DataFrame here

    return future_days.flatten(), future_prices

# Main script
symbol = "AAPL"  # Stock symbol for Apple
df = get_stock_data(symbol)  # Fetch stock data for Apple
future_x, future_y = predict_stock_prices(df)  # Predict future stock prices

# Plot the historical and predicted stock prices
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], label="Historical Prices", color='blue')  # Historical prices
plt.plot([df['Date'].max() + pd.Timedelta(days=i) for i in range(1, 11)], future_y, label="Predicted Prices", color='red')  # Predicted prices
plt.legend()
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title(f"{symbol} Stock Price Prediction")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()