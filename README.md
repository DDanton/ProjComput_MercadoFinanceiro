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
Funções desse módulo:

### Função `stock_data`

#### Descrição
A função `stock_data` recebe o símbolo de ticker de uma ação e uma data de início (opcional) e retorna dados históricos dessa ação a partir da data especificada. Os dados incluem informações como preço de fechamento, retorno simples e retorno logarítmico.

#### Parâmetros
- `ticker` (str): Símbolo da ação para recuperar dados.
- `start_date` (str, padrão='2019-01-02'): Data de início para recuperar dados. Se não fornecida, a data padrão é '2019-01-02'.

#### Exemplo de Uso
```python

# Exemplo de uso
from data_utils import stock_data

ticker_symbol = 'AAPL'
start_date = '2022-01-01'
stock_data_aapl = stock_data(ticker_symbol, start_date)
print(stock_data_aapl.head())
```

### Função `skew_kurt`

#### Descrição:
A função skew_kurt calcula a assimetria (skewness) e a curtose (kurtosis) de um conjunto de dados. Pode operar em dois modos: 'standard', que utiliza os retornos brutos, e 'log', que utiliza os log-retornos.

#### Parâmetros

- `data` (DataFrame): O conjunto de dados contendo informações financeiras.
- `mode` (str, padrão='standard'): Modo de cálculo, podendo ser 'standard' para retornos brutos ou 'log' para log-retornos.

#### Retorno:
Uma lista contendo dois elementos: o primeiro é a skewness e o segundo é a kurtosis.

### Função `return_histogram`

#### Descrição:
A função `return_histogram gera um histograma dos retornos ou log-retornos de um conjunto de dados financeiros. Pode operar em dois modos: 'standard', que utiliza os retornos brutos, e 'log', que utiliza os log-retornos.

#### Parâmetros

- `data` (DataFrame): O conjunto de dados contendo informações financeiras.
- `scale` (str, padrão=None): Modo de escala para os dados, podendo ser 'log' para log-retornos.
- `bins` (int, padrão=100): Número de bins no histograma.
- `color` (str, padrão='blue'): Cor das barras do histograma.
- `edgecolor` (str, padrão='black'): Cor das bordas das barras do histograma.
- `alpha` (float, padrão=0.7): Transparência das barras do histograma.

#### Retorno : 
Um objeto de eixo (axis) do matplotlib contendo o histograma gerado.

####################################################################################################

##  Módulo `distributions`
Funções desse módulo:

### Função `return_distributions`

#### Descrição:
A função return_distributions gera dois gráficos para visualização da distribuição dos retornos ou log-retornos de um conjunto de dados financeiros. O primeiro gráfico mostra o histograma dos dados, com uma sobreposição da curva de ajuste (normal ou t-distribution). O segundo gráfico é o QQ-plot (Quantile-Quantile plot), que compara os quantis teóricos com os quantis observados, proporcionando uma visualização da adequação da distribuição escolhida.

#### Parâmetros
Alguns dos parâmetros tem origem da biblioteca matplotlib

- `data` (DataFrame): O conjunto de dados contendo informações financeiras.
- `distribution` (str, padrão='normal'): Tipo de distribuição a ser ajustada ('normal' ou 't-distribution').
- `mode` (str, padrão='standard'): Modo de cálculo, podendo ser 'standard' para retornos brutos ou 'log' para log-retornos.
- `bins` (int, padrão=100): Número de bins no histograma.
- `color` (str, padrão='blue'): Cor das barras do histograma.
- `edgecolor` (str, padrão='black'): Cor das bordas das barras do histograma.
- `alpha` (float, padrão=0.7): Transparência das barras do histograma.

#### Exemplo de uso
```python
from distributions import return_distributions
from data_utils import stock_data

# Carregar dados
googl = stock_data('GOOGL')

# Gerar gráficos de distribuição para retornos padrão
return_distributions(googl, distribution='normal', mode='standard')
```

################

##  Módulo `gaussian_mix`
Funções desse módulo:

### Função `MixtureModel`

#### Descrição:
A função MixtureModel gera um histograma dos retornos ou log-retornos de um conjunto de dados financeiros, junto com um modelo de mistura gaussiana que se ajusta aos dados. O modelo de mistura gaussiana é composto por dois componentes gaussianos. A função imprime os pesos, médias e variâncias dos componentes.

#### Parâmetros:

- `data` (DataFrame): O conjunto de dados contendo informações financeiras.
- `mode` (str, padrão='normal'): Modo de cálculo, podendo ser 'normal' para retornos brutos ou 'log' para log-retornos.
- `bins` (int, padrão=100): Número de bins no histograma.
- `color` (str, padrão='blue'): Cor das barras do histograma.
- `edgecolor` (str, padrão='black'): Cor das bordas das barras do histograma.
- `alpha` (float, padrão=0.7): Transparência das barras do histograma.

#### Retorno:
Um histograma com curva de ajuste do modelo de mistura gaussiana.

```python

from distributions import MixtureModel
from sua_biblioteca import stock_data

# Carregar dados
googl = stock_data('GOOGL')

# Gerar gráfico de modelo de mistura para retornos padrão
MixtureModel(googl, mode='normal')
```

# Classe `StockAnalyzer`

A classe `StockAnalyzer` é responsável por analisar e visualizar dados históricos de retornos de ações. Ela oferece funcionalidades para carregar dados, calcular retornos e gerar visualizações informativas.

## Métodos

### `__init__(self, stocks, start_date='2019-01-02')`

#### Descrição
Inicializa uma instância da classe `StockAnalyzer`.

#### Parâmetros
- `stocks` (lista): Lista de símbolos de ações a serem analisados.
- `start_date` (string, opcional): Data de início para análise. O padrão é '2019-01-02'.

### `stock_data(self, stock)`

#### Descrição
Carrega dados históricos de uma ação específica.

#### Parâmetros
- `stock` (string): Símbolo da ação a ser carregada.

#### Retorno
Um DataFrame contendo dados históricos da ação.

### `generate_returns_data(self, return_scale='normal')`

#### Descrição
Gera dados de retornos a partir dos dados históricos das ações.

#### Parâmetros
- `return_scale` (string, opcional): Escala dos retornos ('normal' ou 'log'). O padrão é 'normal'.

#### Retorno
Um DataFrame contendo os retornos das ações.

### `plot_correlation_matrix(self)`

#### Descrição
Plota a matriz de correlação entre os retornos das ações.

### `plot_pairplot(self)`

#### Descrição
Plota um pairplot dos retornos das ações.

### `plot_returns_over_time(self, separate_plots=False)`

#### Descrição
Plota os retornos das ações ao longo do tempo.

#### Parâmetros
- `separate_plots` (bool, opcional): Se verdadeiro, plota gráficos separados para cada ação. O padrão é falso.

## Exemplo de Uso

```python
from analytics import StockAnalyzer

# Criar uma instância de StockAnalyzer
analyzer = StockAnalyzer(['AAPL', 'GOOGL'], start_date='2020-01-01')

# Plotar matriz de correlação
analyzer.plot_correlation_matrix()

# Plotar pairplot
analyzer.plot_pairplot()

# Plotar retornos ao longo do tempo
analyzer.plot_returns_over_time(separate_plots=True)
```

# Função `PriceSimulationFunc`

A função `PriceSimulationFunc` realiza uma simulação estocástica de preços com base na distribuição dos retornos das ações. A simulação pode ser realizada usando uma distribuição de Mixture of Gaussians ou uma distribuição t.

## Parâmetros
- `data` (DataFrame): DataFrame contendo os dados históricos de preços.
- `steps` (int, opcional): O número de etapas para a simulação. O padrão é 10.
- `distribution` (str, opcional): A distribuição a ser utilizada ('MixGaussians' ou 't-distribution'). O padrão é 'MixGaussians'.

## Exemplo de Uso

```python
from price_simulation import PriceSimulationFunc
from data_utils import stock_data

# Carregar dados
googl = stock_data('GOOGL')

# Executar simulação de preços com distribuição de Mixture of Gaussians
PriceSimulationFunc(googl, steps=20, distribution='MixGaussians')
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
