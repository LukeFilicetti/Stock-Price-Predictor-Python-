# Stock-Price-Predictor-Python-
Description: Implement a priority queue system where users can add, remove, and process tasks based on priority.

Uses a MaxHeap to manage tasks.
Allows users to add tasks with different priority levels.
Implements Comparable<Task> to sort tasks automatically.
Outputs the highest priority task first when processing.

This Python project uses yfinance and scikit-learn to predict the future prices of stocks based on historical data. It uses Linear Regression to make predictions, and you can visualize the predictions on a graph.

**Features:**

- Fetches historical stock price data using the yfinance library.
- Uses Linear Regression to predict future stock prices based on historical data.
- Visualizes the historical and predicted prices using matplotlib.

# Installation & Setup

1. Create a Virtual Environment:

`python -m venv venv`

2. Activate the virtual environment:

`venv\Scripts\activate`

`source venv/Scripts/activate`

3. Install Dependencies:

`pip install yfinance pandas numpy matplotlib scikit-learn`

4. Running the Script:

`python StockPricePredictor.py`

5. Selecting Different Stock Symbols:

To predict stock prices for a different company, you can change the symbol in the StockPricePredictor.py script.

For example, to predict the prices for Tesla (TSLA), simply change:

`symbol = "AAPL"`

to

`symbol = "TSLA"`

Then run the script again.

6. Deactivating the Virtual Environment:

`deactivate`

7. Troubleshooting

ModuleNotFoundError: If you get a "ModuleNotFoundError", make sure the virtual environment is activated and the dependencies are installed.

