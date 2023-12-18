from data_utils import stock_data
from distributions import  return_distributions
from analitycs import StockAnalyzer
from gaussian_mix import MixtureModel
from stats_time_series import PriceSimulationFunc_trend
from plotter import StockPlotter
from price_simulation import PriceSimulationFunc
from stats_time_series import diff_times_return, diff_times_prices
from arima_forecast import ARIMAPredictor

def main():
    # Exemplo de uso
    googl = stock_data('GOOGL')
    #return_distributions(googl, mode='log', bins=50, color='orange', edgecolor='black', alpha=0.5)

    #analyzer = StockAnalyzer(['AAPL', 'AMZN', 'GOOGL'])
    #analyzer.plot_returns_over_time(separate_plots=False)

    #MixtureModel(googl, mode='log')

    

if __name__ == "__main__":
    googl = stock_data('GOOGL')
    PriceSimulationFunc_trend(googl, steps=10, num_simulations=1, distribution='MixGaussians', trend='none', trend_strength=0.01)

