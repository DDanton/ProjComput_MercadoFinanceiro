# módulo: price_simulation.py
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from scipy.stats import t 
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # ou outro backend suportado


def PriceSimulationFunc(data, steps=10, distribution='MixGaussians'):
    data = pd.DataFrame(data)
    p0 = data.iloc[-1]['Close']
    last_date = data.iloc[-1]['Date']
    data_r = data['Return'].dropna().to_numpy().reshape(-1, 1)
    count = 0
    prices = [p0]

    if distribution == 'MixGaussians':
        # Ajuste o modelo de Mixture of Gaussians aos dados
        num_components = 2
        model = GaussianMixture(n_components=num_components)
        model.fit(data_r)
        # Gere números aleatórios com base no modelo ajustado
        num_samples = steps
        ''' Uma lista de numeros aleatorios que seguem a distribuição das MixGaussians'''
        samples = model.sample(num_samples)[0]
        samples_list= []
        for i in samples:
            actual_value  = i[0]
            samples_list.append(actual_value)
        samples = np.array(samples_list)

        while count < steps:
            R = samples[count]
            price = prices[-1] * (1 + R)  # pela própria def de retorno
            prices.append(price)
            count += 1

    elif distribution == 't-distribution':
        df, loc, scale = t.fit(data['Return'].dropna())

        while count < steps:
            R = t.rvs(df, loc, scale)
            price = prices[-1] * (1 + R)
            prices.append(price)
            count += 1

    # Configurações do plot
    #sns.set(style="whitegrid")  # Estilo de fundo do seaborn
    plt.figure(figsize=(10, 6))  # Tamanho do gráfico

    # Plot dos preços
    plt.plot(prices, color='blue', label='Simulated Prices')

    # Títulos e rótulos
    plt.title('Simulação de Preços', fontsize=16)
    plt.xlabel('Days', fontsize=14)
    plt.ylabel('Preço', fontsize=14)

    # Adiciona a legenda
    plt.legend()

    # Exibe o gráfico
    plt.show()