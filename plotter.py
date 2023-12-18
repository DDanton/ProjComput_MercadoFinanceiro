# módulo: plotting.py
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import pandas as pd
import numpy as np


class StockPlotter:
    def __init__(self, ticker, start_date='2022-01-01', end_date=None):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.get_stock_data()

    def get_stock_data(self):
        stock_data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return stock_data

    def plot_stock(self, column='Close', title='Stock Price', figsize=(10, 6)):
        plt.figure(figsize=figsize)
        plt.plot(self.data.index, self.data[column], label=column)
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.show()

    def plot_multiple_stocks(self, columns=['Close'], title='Stock Prices', figsize=(10, 6)):
        plt.figure(figsize=figsize)
        for column in columns:
            plt.plot(self.data.index, self.data[column], label=column)
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

    def plot_moving_average(self, column='Close', window=20, title='Moving Average', figsize=(10, 6)):
        plt.figure(figsize=figsize)
        plt.plot(self.data.index, self.data[column], label='Original')
        plt.plot(self.data[column].rolling(window=window).mean(), label=f'{window}-day Moving Average', color='orange')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.show()

    def plot_bollinger_bands(self, column='Close', window=20, num_std=2, title='Bollinger Bands', figsize=(10, 6)):
        rolling_mean = self.data[column].rolling(window=window).mean()
        upper_band = rolling_mean + (self.data[column].rolling(window=window).std() * num_std)
        lower_band = rolling_mean - (self.data[column].rolling(window=window).std() * num_std)

        plt.figure(figsize=figsize)
        plt.plot(self.data.index, self.data[column], label='Price')
        plt.plot(upper_band, label='Upper Band')
        plt.plot(lower_band, label='Lower Band')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.show()

    def plot_exponential_moving_average(self, column='Close', span=20, title='Exponential Moving Average', figsize=(10, 6)):
        plt.figure(figsize=figsize)
        plt.plot(self.data.index, self.data[column], label='Original')
        plt.plot(self.data[column].ewm(span=span, adjust=False).mean(), label=f'{span}-day Exponential Moving Average', color='orange')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(column)
        plt.legend()
        plt.show()
