#module arima_forecast.py
from pmdarima import auto_arima
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import pandas as pd

class ARIMAPredictor:
    def __init__(self, data, column='Close', n_test=30):
        self.data = data
        self.column = column
        self.n_test = n_test
        self.train, self.test = self.split_data()

    def split_data(self):
        data = self.data[self.column].dropna()
        train = data.iloc[:-self.n_test]
        test = data.iloc[-self.n_test:]
        return train, test

    def fit_model(self):
        model = auto_arima(self.train, error_action='ignore', trace=True, suppress_warnings=True, maxiter=100, seasonal=False)
        return model

    def plot_result(self, model):
        params = model.get_params()
        d = params['order'][1]

        train_pred = model.predict_in_sample(start=d, end=-1)
        test_pred, confint = model.predict(n_periods=self.n_test, return_conf_int=True)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.data.index, self.data[self.column], label='data')
        ax.plot(self.train.index[d:], train_pred, label='fitted')
        ax.plot(self.test.index, test_pred, label='forecast')
        ax.fill_between(self.test.index, confint[:, 0], confint[:, 1], color='red', alpha=0.3)
        ax.legend()
        plt.title(f'ARIMA Forecast for {self.column}')


    def plot_test(self, model):
        test_pred, confint = model.predict(n_periods=self.n_test, return_conf_int=True)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.test.index, self.test, label='true')
        ax.plot(self.test.index, test_pred, label='forecast')
        ax.fill_between(self.test.index, confint[:, 0], confint[:, 1], color='red', alpha=0.3)
        ax.legend()
        plt.title(f'ARIMA Forecast Test for {self.column}')
        plt.show()

    def extrapolate_test(self, model, future_steps=10):
        extrapolate_values, confint = model.predict(n_periods=future_steps, return_conf_int=True)
        last_date = self.test.index[-1]

        future_index = pd.date_range(start=last_date, periods=future_steps + 1, freq='B')[1:]
        future_pred = model.predict(n_periods=future_steps)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(self.test.index, self.test, label='true')
        ax.plot(future_index, future_pred, label='extrapolation')
        ax.fill_between(future_index, confint[:, 0], confint[:, 1], color='red', alpha=0.3)
        ax.legend()
        plt.title(f'ARIMA Extrapolation for {self.column}')
        plt.show()