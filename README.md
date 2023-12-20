# ProjPythonStockPrices

## Descrição
Este projeto tem como objetivo desenvolver funcionalidades que utilizem dados de ações retirados e tratados da biblioteca
yfinance. Com isso, tem-se a ideia de através das series temporais a aplicação automatizada de modelos de simulação 
de preços utilizando uma abordagem de monte Carlo/ processos estocásticos por caminhos aleatórios e a utilização do modelo ARIMA de Machine Learning.

## Modelo estocástico empregado
Explicar o modelo estocástico que foi utilizado para simulação dos preços dos ativos
Modelo com adição de tendência 

## Modelo Arima 
Descrever como ele funciona. Por quais razões utiliza-se esse modelo para séries temporais
Método de achar os hiperparâmetros AIC

[Python-Forecast Book]: 

## Bibliotecas Necessárias

Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o código:

- [seaborn](https://seaborn.pydata.org/)
- [prophet](https://facebook.github.io/prophet/)
- [yfinance](https://pypi.org/project/yfinance/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [pmdarima](https://pmdarima.readthedocs.io/)
- [statsmodels](https://www.statsmodels.org/)
- [scikit-learn](https://scikit-learn.org/)
- [scipy](https://www.scipy.org/)


# Uso - Exemplos

##  Módulo `data_utils`

### Função `stock_data`

#### Descrição
A função `stock_data` recebe o símbolo de ticker de uma ação e uma data de início (opcional) e retorna dados históricos dessa ação a partir da data especificada. Os dados incluem informações como preço de fechamento, retorno simples e retorno logarítmico.

#### Parâmetros
- `ticker` (str): Símbolo da ação para recuperar dados.
- `start_date` (str, padrão='2019-01-02'): Data de início para recuperar dados. Se não fornecida, a data padrão é '2019-01-02'.

### Exemplo de Uso
```python

# Exemplo de uso
from data_utils import stock_data

ticker_symbol = 'AAPL'
start_date = '2022-01-01'
stock_data_aapl = stock_data(ticker_symbol, start_date)
print(stock_data_aapl.head())
```

## Função `PriceSimulationFunc_trend`

### Descrição
Esta função realiza uma simulação de preço com tendência ascendente ou descendente, usando uma distribuição de mistura de gaussianas ou uma distribuição t. A função aceita dados históricos de preços, como um DataFrame do pandas.

### Parâmetros

- `data` (DataFrame): O DataFrame contendo os dados históricos de preços.
- `steps` (int): O número de etapas para simulação.
- `num_simulations` (int): O número de simulações a serem executadas.
- `distribution` (str): A distribuição a ser usada ('MixGaussians' ou 't-distribution').
- `trend` (str): A tendência dos preços ('up', 'down' ou 'none').
- `trend_strength` (float): A força da tendência.

### Exemplo de Uso

```python
from stats_time_series import PriceSimulationFunc_trend
from sua_biblioteca import stock_data

# Carregar dados
googl = stock_data('GOOGL')

# Executar a simulação de preço com tendência ascendente
PriceSimulationFunc_trend(googl, steps=100, num_simulations=8, distribution='MixGaussians', trend='up', trend_strength=0.1)
```



## Esse video é muito interessante para que vocês consigam mexer também (a partir dos 10minutos fica mais relevante): https://www.youtube.com/watch?v=7cNP3AE49Bg 
# 
#
#
#
#
