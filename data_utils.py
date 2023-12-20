# módulo: data_utils.py
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def stock_data(ticker, start_date='2019-01-02'):
    data = yf.Ticker(ticker)
    data = data.history(start=start_date, end=None)
    data.index = data.index.strftime('%Y-%m-%d')
    data.reset_index(inplace=True)

    data['Prev-Close'] = data['Close'].shift(1)
    data['Return'] = data['Close'] / data['Prev-Close'] - 1
    data['Log-Return'] = np.log(data['Return'] + 1)

    return data

def skew_kurt(data,mode = 'standard'):
  skewness_values = []
  kurtosis_values = []
  result = []
  data = data.dropna()

  if mode ==  'standard':
    n_samples = len(data['Return'])
    mean = data['Return'].mean()
    std  = data['Return'].std()

    for value in data['Return']:
      skewness = ((value - mean) / std)**3
      kurtosis = ((value - mean) / std)**4 - 3
      skewness_values.append(skewness)
      kurtosis_values.append(kurtosis)

  elif mode == 'log':
    n_samples = len(data['Log-Return'])
    mean = data['Log-Return'].mean()
    std  = data['Log-Return'].std()

    for value in data['Log-Return']:
      skewness = ((value - mean) / std)**3
      kurtosis = ((value - mean) / std)**4 - 3
      skewness_values.append(skewness)
      kurtosis_values.append(kurtosis)
  # Dividir pelos números de amostras

  skewness_result = sum(skewness_values) / n_samples
  kurtosis_result = sum(kurtosis_values) / n_samples
  result.append(skewness_result)
  result.append(kurtosis_result)

  return result


def return_histogram(data, scale=None, bins=100, color='blue', edgecolor='black', alpha=0.7):
    data = pd.DataFrame(data)

    if scale == 'log':
        mean = data['Return'].mean()
        std = data['Return'].std()
        y = data['Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha)
    else:
        mean = data['Log-Return'].mean()
        std = data['Log-Return'].std()
        y = data['Log-Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha)

    y.set_xlabel('returns')
    y.set_ylabel('freq')
    y.set_title('return histogram')

    y.text(0.95, 0.95, f'Mean: {mean:.4f}\nStd: {std:.4f}', color='red', ha='right', va='top', transform=y.transAxes, fontsize=10)

    return y


# módulo: distributions.py