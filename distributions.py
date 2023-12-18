# módulo: distributions.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import probplot, norm, t

class MyT:
    def __init__(self, data):
        self.data = data

    def fit(self, x):
        params = t.fit(x)
        df, loc, scl = params
        return df

    def ppf(self, x, loc=0, scale=1):
        df = self.fit(self.data)
        return t.ppf(x, df, loc, scale)



def return_distributions(data, distribution='normal', mode='standard', bins=100, color='blue', edgecolor='black', alpha=0.7):
    std = data['Return'].std()
    std_log = data['Log-Return'].std()
    mean = data['Return'].mean()
    mean_log = data['Log-Return'].mean()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    if distribution == 'normal' and mode == 'standard':
        x_space = np.linspace(data['Return'].min(), data['Return'].max(), 100)
        y_space = norm.pdf(x_space, loc=mean, scale=std)
        axes[0].plot(x_space, y_space, label='normal fit', color='orange')
        data['Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True, ax=axes[0])
        x_pos_mean = 0.3
        y_pos_mean = 0.95
        axes[0].text(x_pos_mean, y_pos_mean, f'Mean: {mean:.4f}\nStd: {std:.4f}', color='red',
                     ha='right', va='top', transform=axes[0].transAxes, fontsize=10)
        axes[0].legend()
        axes[0].set_title('Histograma e Ajuste Normal - Retornos Padrão')
        axes[0].set_xlabel('Retornos Padrão')
        axes[0].set_ylabel('Frequência')

        # QQ-plot para normal
        probplot(data['Return'].dropna(), dist='norm', fit=True, plot=axes[1])

    elif distribution == 'normal' and mode == 'log':
        x_space = np.linspace(data['Log-Return'].min(), data['Log-Return'].max(), 100)
        y_space = norm.pdf(x_space, loc=mean_log, scale=std_log)
        axes[0].plot(x_space, y_space, label='normal fit', color='orange')
        data['Log-Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True, ax=axes[0])
        x_pos_mean = 0.3
        y_pos_mean = 0.95
        axes[0].text(x_pos_mean, y_pos_mean, f'Mean: {mean_log:.4f}\nStd: {std_log:.4f}', color='red',
                     ha='right', va='top', transform=axes[0].transAxes, fontsize=10)
        axes[0].legend()
        axes[0].set_title('Histograma e Ajuste Normal - Log-Retornos')
        axes[0].set_xlabel('Log-Retornos')
        axes[0].set_ylabel('Frequência')

        # QQ-plot para normal
        probplot(data['Log-Return'].dropna(), dist='norm', fit=True, plot=axes[1])

    elif distribution == 't-distribution' and mode == 'standard':
        x_space = np.linspace(data['Return'].min(), data['Return'].max(), 100)
        myt = MyT(data['Return'].dropna())
        params = t.fit(data['Return'].dropna())
        df, loc, scl = params
        y_space = t.pdf(x_space, df, loc, scl)
        axes[0].plot(x_space, y_space, label='t - fit', color='orange')
        data['Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True, ax=axes[0])
        x_pos_mean = 0.3
        y_pos_mean = 0.95
        axes[0].text(x_pos_mean, y_pos_mean, f'Mean: {mean:.4f}\nStd: {std:.4f}\nDF: {df:.4f}', color='red',
                     ha='right', va='top', transform=axes[0].transAxes, fontsize=10)
        axes[0].legend()
        axes[0].set_title('Histograma e Ajuste t - Retornos Padrão')
        axes[0].set_xlabel('Retornos Padrão')
        axes[0].set_ylabel('Frequência')

        # QQ-plot para t-distribution
        probplot(data['Return'].dropna(), dist=myt, fit=True, plot=axes[1])

    elif distribution == 't-distribution' and mode == 'log':
        x_space = np.linspace(data['Log-Return'].min(), data['Log-Return'].max(), 100)
        myt = MyT(data['Log-Return'].dropna())
        params = t.fit(data['Log-Return'].dropna())
        df, loc, scl = params
        y_space = t.pdf(x_space, df, loc, scl)
        axes[0].plot(x_space, y_space, label='t - fit', color='orange')
        data['Log-Return'].hist(bins=bins, color=color, edgecolor=edgecolor, alpha=alpha, density=True, ax=axes[0])
        x_pos_mean = 0.3
        y_pos_mean = 0.95
        axes[0].text(x_pos_mean, y_pos_mean, f'Mean: {mean_log:.4f}\nStd: {std_log:.4f}\nDF: {df:.4f}', color='red',
                     ha='right', va='top', transform=axes[0].transAxes, fontsize=10)
        axes[0].legend()
        axes[0].set_title('Histograma e Ajuste t - Log-Retornos')
        axes[0].set_xlabel('Log-Retornos')
        axes[0].set_ylabel('Frequência')

        # QQ-plot para t-distribution
        probplot(data['Log-Return'].dropna(), dist=myt, fit=True, plot=axes[1])

    plt.subplots_adjust(wspace=0.4)
    plt.show()
