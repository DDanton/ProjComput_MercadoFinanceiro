# módulo: price_simulation.py
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from scipy.stats import t 
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # ou outro backend suportado


def PriceSimulationFunc(data, steps=10, num_simulations=1, distribution='MixGaussians', ticker_title=None):
    data = pd.DataFrame(data)
    p0 = data.iloc[-1]['Close']
    last_date = data.iloc[-1]['Date']
    data_r = data['Return'].dropna().to_numpy().reshape(-1, 1)

    plt.figure(figsize=(10, 6))  # Tamanho do gráfico

    for _ in range(num_simulations):
        count = 0
        prices = [p0]

        if distribution == 'MixGaussians':
            # Ajuste o modelo de Mixture of Gaussians aos dados
            num_components = 2
            model = GaussianMixture(n_components=num_components)
            model.fit(data_r)
            # Gere números aleatórios com base no modelo ajustado
            num_samples = steps
            samples = model.sample(num_samples)[0]
            samples_list = [i[0] for i in samples]
            samples = np.array(samples_list)

            while count < steps:
                R = samples[count]
                price = prices[-1] * (1 + R)  # pela própria definição de retorno
                prices.append(price)
                count += 1

        elif distribution == 't-distribution':
            df, loc, scale = t.fit(data['Return'].dropna())

            while count < steps:
                R = t.rvs(df, loc, scale)
                price = prices[-1] * (1 + R)
                prices.append(price)
                count += 1

        # Plot dos preços simulados
        plt.plot(prices)

    # Configurações do plot
    plt.title(f'Simulação de Preços - {ticker_title}' if ticker_title else 'Simulação de Preços', fontsize=16)
    plt.xlabel('Days', fontsize=14)
    plt.ylabel('Preço USD', fontsize=14)
    plt.grid(True)

    # Adiciona a legenda
    plt.legend()

    # Exibe o gráfico
    plt.show()