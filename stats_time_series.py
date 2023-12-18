# módulo: stats_time_series.py
from statsmodels.tsa.stattools import adfuller
import pandas as pd
from sklearn.mixture import GaussianMixture
from scipy.stats import probplot, norm, t
import numpy as np
import matplotlib.pyplot as plt

## vou criar uma funcao que irá verificar a estacionaridade dos valores, e irá empregar a quantidade necessária de diferenciação
## ela retorna o número de diferenciações mais a lista diferenciada e cria um conjunto de dados chamado Log_price
## o Log price serviria para caso o modelo ARIMA fosse ser implementado com os preços diretamente e nao com os retornos

def diff_times_return(data):
  return_list = []
  data = data.dropna()
  diff = 0 
  res = adfuller(data['Log-Return'])
  p_value = res[1]
  
  # Aplicando o critério dos 5%
  data['Diff'] = data['Log-Return']

  while p_value > 0.05:
    data['Diff'] = data['Diff'].diff()
    diff += 1
    res = adfuller(data['Diff'].dropna())  # Remova NaNs antes de calcular o teste
    p_value = res[1]

  return_list.append(diff)
  return_list.append(p_value)
  return_list.append(data['Diff'])
  return return_list

def diff_times_prices(data):
    return_list = []
    
    # Remover valores ausentes (NaN)
    data = data.dropna()

    # Verificar e substituir infinitos por NaN
    data = data.replace([np.inf, -np.inf], np.nan)

    # Calcular o log dos preços
    data['LogPrice'] = np.log(data['Close'])

    # Aplicar o teste de estacionariedade aos log-preços
    res = adfuller(data['LogPrice'])
    p_value = res[1]

    # Aplicar critério dos 5%
    data['Diff'] = data['LogPrice']
    diff = 0

    while p_value > 0.05:
        data['Diff'] = data['Diff'].diff()
        diff += 1

        # Reaplicar o teste de estacionariedade aos dados diferenciados
        res = adfuller(data['Diff'].dropna())
        p_value = res[1]

    return_list.append(diff)
    return_list.append(p_value)
    return_list.append(data['Diff'])
    
    return return_list

def PriceSimulationFunc_trend(data, steps=10, num_simulations=1, distribution='MixGaussians', trend='none', trend_strength=0.01):
    p0 = data.iloc[-1]['Close']
    last_date = data.iloc[-1]['Date']
    data_r = data['Return'].dropna().to_numpy().reshape(-1, 1)
    
    count = 0
    all_prices = []

    for _ in range(num_simulations):
        prices = [p0]
        if trend == 'up':
            trend_factors = np.linspace(1, 1 + trend_strength, steps)
        elif trend == 'down':
            trend_factors = np.linspace(1, 1 - trend_strength, steps)
        else:
            trend_factors = np.ones(steps)

        if distribution == 'MixGaussians':
            num_components = 2
            model = GaussianMixture(n_components=num_components)
            model.fit(data_r)
            num_samples = steps
            samples = model.sample(num_samples)[0]

            for i in range(steps):
                R = samples[i] * trend_factors[i]
                price = prices[-1] * (1 + R)
                prices.append(price)

        elif distribution == 't-distribution':
            df, loc, scale = t.fit(data['Return'].dropna())

            for i in range(steps):
                R = t.rvs(df, loc, scale) * trend_factors[i]
                price = prices[-1] * (1 + R)
                prices.append(price)


        all_prices.append(prices)

    # Plotar todas as simulações
    for prices in all_prices:
        plt.plot(prices)

    plt.xlabel('Steps')
    plt.ylabel('Price')
    plt.title(f'Multiple Price Simulations ({num_simulations} simulations)')
    plt.show()


