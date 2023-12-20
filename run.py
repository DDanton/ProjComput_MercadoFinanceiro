from data_utils import stock_data, return_histogram, skew_kurt
from distributions import  return_distributions
from analitycs import StockAnalyzer
from gaussian_mix import MixtureModel
from stats_time_series import PriceSimulationFunc_trend
from plotter import StockPlotter
from price_simulation import PriceSimulationFunc
from stats_time_series import diff_times_return, diff_times_prices
from arima_forecast import ARIMAPredictor
import matplotlib.pyplot as plt
import pandas as pd
    
if __name__ == "__main__":
    googl = stock_data('GOOGL')
# Exemplo de uso com parâmetros ajustados
    
    #return_histogram(googl, scale='log', bins=50, color='orange', edgecolor='black', alpha=0.5)
    # Exibindo o gráfico
    #plt.show()

    # Exemplo de chamada da função
    #return_distributions(data=googl, distribution='t-distribution', mode='log')

    #print(skew_kurt(data=googl,mode = 'log'))

    # Exemplo de uso da classe
    '''stocks_list = ['AMZN', 'GLD', 'LMT', 'XLF', 'XLI']
    start_date = '2020-01-01'  # Especifique a data de início desejada
    analyzer = StockAnalyzer(stocks_list, start_date=start_date)
    analyzer.plot_correlation_matrix()
    analyzer.plot_pairplot()'''
    
    #analyzer.plot_returns_over_time(separate_plots=False)  # Altere para False para todos os valores no mesmo plot
    #MixtureModel(googl, mode='log')
    #PriceSimulationFunc(data=googl, steps=100, distribution='MixGaussians')]
    
    # Exemplo de uso
    '''ticker = ['AAPL','AMZN']
    plotter = StockPlotter(ticker)
    plotter.plot_stock()
    #plotter.plot_multiple_stocks(['AAPL','SBUX'],columns=['Close'], title='Stock Prices')
    plotter.plot_moving_average(window=50)
    plotter.plot_bollinger_bands()
    plotter.plot_exponential_moving_average(span=30)
    PriceSimulationFunc_trend(googl, steps=100, num_simulations=100, distribution='MixGaussians', trend='up', trend_strength=1.)'''
    
    # Exemplo de uso para 'Close'
    '''aapl = stock_data('AAPL')
    aapl['Date'] = pd.to_datetime(aapl['Date'])
    aapl.set_index('Date', inplace=True)
    aapl = aapl.dropna()
    aapl_predictor = ARIMAPredictor(aapl, column='Close')
    close_model = aapl_predictor.fit_model()
    aapl_predictor.plot_result(close_model)
    aapl_predictor.plot_test(close_model)
    aapl_predictor.extrapolate_test(close_model,future_steps =100)'''


