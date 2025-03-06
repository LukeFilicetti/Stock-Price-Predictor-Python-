import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Fetch historical stock data
def get_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    df = stock.history(period="1y")
    df = df[['Close']].reset_index()
    df['Days'] = np.arange(len(df))
    return df

# Predict future prices
def predict_stock_prices(df):
    X = df[['Days']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.array(range(len(df), len(df) + 10)).reshape(-1, 1)
    future_prices = model.predict(future_days)

    return future_days.flatten(), future_prices

# Main script
symbol = "AAPL"
df = get_stock_data(symbol)
future_x, future_y = predict_stock_prices(df)

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], label="Historical Prices", color='blue')
plt.plot([df['Date'].max() + pd.Timedelta(days=i) for i in range(1, 11)], future_y, label="Predicted Prices", color='red')
plt.legend()
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title(f"{symbol} Stock Price Prediction")
plt.show()