
# módulo: analytics.py
        
import seaborn as sns
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StockAnalyzer:
    def __init__(self, stocks, start_date='2019-01-02'):
        self.stocks = stocks
        self.start_date = start_date
        self.returns_data = self.generate_returns_data()

    def stock_data(self, stock):
        data = yf.Ticker(stock)
        data = data.history(start=self.start_date, end=None)
        data.index = data.index.strftime('%Y-%m-%d')  # formato ano mes dia
        data = pd.DataFrame(data)  # passa para um DataFrame em pandas
        # Resetando o índice para mover a data como uma coluna
        data.reset_index(inplace=True)
        ## vou agora começar a calcular os retornos
        '''para isso eu tenho que criar novos dados chamando o preco do dia anterior para o dia seguinte
        e com isso eu consigo vetorizar os calculos e calcular o retorno de uma forma mais direta, sem utilizar loops'''
        # return = [Pt - P(t-1)]/Pt
        data['Prev-Close'] = data['Close'].shift(1)
        data['Return'] = data['Close'] / data['Prev-Close'] - 1
        ## adicionando o retorno log
        data['Log-Return'] = np.log(data['Return'] + 1)
        return data

    def generate_returns_data(self, return_scale='normal'):
        data_frame_stocks = []

        for stock in self.stocks:
            data_frame_stocks.append(self.stock_data(stock))

        if return_scale == 'normal':
            returns_stocks = pd.concat([df['Return'] for df in data_frame_stocks], axis=1)
        elif return_scale == 'log':
            returns_stocks = pd.concat([df['Log-Return'] for df in data_frame_stocks], axis=1)

        returns_stocks.columns = self.stocks
        return pd.DataFrame(returns_stocks)

    def plot_correlation_matrix(self):
        correlation_matrix = self.returns_data.corr()

        # Plotar matriz de correlação usando Seaborn
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title("Matriz de Correlação")
        plt.show()

    def plot_pairplot(self):
        # Plotar pairplot usando Seaborn
        sns.set(style="ticks")
        sns.pairplot(self.returns_data, kind='scatter', diag_kind='kde', palette='husl')
        plt.suptitle("Pairplot - Retornos", y=1.02)
        plt.show()

    def plot_returns_over_time(self, separate_plots=False):
        # Plotar retornos ao longo do tempo para cada ação usando Seaborn
        sns.set(style="whitegrid", palette="husl", rc={"lines.linewidth": 1.5})

        if separate_plots:
            fig, axes = plt.subplots(len(self.stocks), 1, figsize=(12, 6), sharex=True, sharey=True)
            for i, symbol in enumerate(self.returns_data.columns):
                sns.lineplot(data=self.returns_data, x=self.returns_data.index, y=symbol, label=symbol, linewidth=2, ax=axes[i])
                axes[i].set_title(symbol)
            plt.xlabel("Data")
            plt.tight_layout()
        else:
            plt.figure(figsize=(12, 6))
            colors = sns.color_palette("husl", n_colors=len(self.stocks))
            for i, symbol in enumerate(self.returns_data.columns):
                sns.lineplot(data=self.returns_data, x=self.returns_data.index, y=symbol, label=symbol, linewidth=1, color=colors[i])
            plt.title("Retornos ao longo do Tempo")
            plt.xlabel("Data")
            plt.legend(loc="upper left")
            plt.ylabel('Returns')

        plt.show()
