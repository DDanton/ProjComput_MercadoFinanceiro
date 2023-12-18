
##gaussian miture module


import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from scipy.stats import norm

def MixtureModel(data, mode='normal', bins=100, color='blue', edgecolor='black', alpha=0.7):
    if mode == 'normal':
        data_r = data['Return'].dropna().to_numpy().reshape(-1, 1)
        column_name = 'Return'
    elif mode == 'log':
        data_r = data['Log-Return'].dropna().to_numpy().reshape(-1, 1)
        column_name = 'Log-Return'
    else:
        raise ValueError("Mode should be 'normal' or 'log'.")

    model = GaussianMixture(n_components=2)
    model.fit(data_r)

    weights = model.weights_
    means = model.means_.flatten()
    cov = model.covariances_.flatten()

    x_list = np.linspace(data_r.min(), data_r.max(), 100)
    fx0 = norm.pdf(x_list, means[0], np.sqrt(cov[0]))
    fx1 = norm.pdf(x_list, means[1], np.sqrt(cov[1]))
    fx = weights[0] * fx0 + weights[1] * fx1

    print("weights:", weights)
    print("means:", means)
    print("variances:", cov)

    plt.figure(figsize=(10, 6))
    plt.hist(data_r, bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True, label=f'{column_name} histogram')
    plt.plot(x_list, fx, label='Mixture model')
    plt.ylabel(f'Freq-{mode}')
    plt.xlabel('Returns')
    plt.legend()
    plt.title(f'Mixture Model for {column_name}')
    plt.show()

# Exemplo de uso:
# MixtureModel(data, mode='normal')
