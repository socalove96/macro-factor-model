import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os
import yfinance as yf
from pandas_datareader import data, fred
import pandas_datareader as pdr
from fredapi import Fred

yf.pdr_override()


def get_stock_returns_and_macro_factors(start_date, end_date, fred_tickers, index='SP500'):
    """
    Retrieve stock returns and macroeconomic factors from FRED API and process the data.

    Arguments:
        The stock ticker.
    index : str
        Default index
    start_date : str
        The start date in the format 'YYYY-MM-DD'.
    end_date : str
        The end date in the format 'YYYY-MM-DD'.
    fred_tickers : Fred database tickers in the form of a Dict.

    Returns:
    stock_returns : pandas Series
        Stock returns data.
    macro_factors : pandas DataFrame
        Macro factors data.
    latest_macro_factors : List
        Latest factor values to insert calculate returns with.
    """
    # Initialize the Fred API client
    fred = Fred(api_key=os.getenv('FRED_API_KEY'))

    # Create an empty dataframe
    df = pd.DataFrame()

    # Retrieve and resample S&P500 df
    index_data = fred.get_series(index, start_date, end_date).resample('AS').first()
    df[index] = index_data

    # Retrieve and resample macroeconomic data
    for ticker, column_name in fred_tickers.items():
        df[column_name] = fred.get_series(ticker, start_date, end_date).resample('AS').first()

    # Extract the factor values for the latest year
    latest_factor_values = df.iloc[-1].values.tolist()[1:]
    latest_factor_values = [5.25, latest_factor_values[1] * 1.009, 4.0, 5.1, 63.5]

    # Define the date ranges corresponding to the financial crisis and pandemic intervals
    crisis_start_date = pd.to_datetime('2007-12-01')
    crisis_end_date = pd.to_datetime('2009-12-01')

    pandemic_start_date = pd.to_datetime('2020-01-01')
    pandemic_end_date = pd.to_datetime('2020-12-31')

    # Filter the data based on the date ranges
    df = df.loc[~((df.index >= crisis_start_date) & (df.index <= crisis_end_date)) &
                ~((df.index >= pandemic_start_date) & (df.index <= pandemic_end_date))]

    # Split the data into stock returns and macro factors
    stock_returns = df[index]
    macro_factors = df[df.columns.tolist()[1:]]

    print(stock_returns)
    print(macro_factors)
    print(latest_factor_values)

    return stock_returns, macro_factors, latest_factor_values


def calculate_params(stock_returns, macro_factors):
    """
    Calculate the intercept, beta, and residuals of the factor model.
    
    Arguments:
    stock_returns : pandas Series
        The stock returns data.
    macro_factors : pandas DataFrame
        The macroeconomic factors data.
        
    Returns:
    intercept : float
        The intercept term of the factor model.
    beta : numpy array
        The beta coefficients or factor loadings.
    residuals : float
        The residual value of the factor model.
    """
    # Add a constant column to the macro factors
    macro_factors = sm.add_constant(macro_factors)
    
    # Fit the OLS regression model
    model = sm.OLS(stock_returns, macro_factors)
    results = model.fit()
    print(results.summary())

    # Extract the beta, intercept, and residuals from the results
    beta = results.params[1:]
    intercept = results.params[0]
    residual = results.resid[-1]

    # Print the intercept, beta, and residuals
    print("\nIntercept:\n", intercept)
    print("\nBeta:\n", beta)
    print("\nResidual:\n", residual)

    return intercept, beta, residual


def macro_factor_model_return(a_i, b_ik, F_K, epsilon_i):
    """
    Calculate the return of asset i based on the macroeconomic factor model equation.
    
    Arguments:
    a_i : float
        The intercept term or constant for asset i.
    b_ik : numpy array or list
        The factor loadings or coefficients for asset i.
    F_K : numpy array or list
        The macro factors values.
    epsilon_i : float
        The error term or residual for asset i.
        
    Returns:
    float
        The calculated return of asset i.

    """
    b_i = np.array(b_ik)
    F = np.array(F_K)

    factor_component = np.dot(b_i, F.T)

    return a_i + factor_component + epsilon_i



def plot_observed_vs_fitted(stock_returns, residual, intercept, beta, macro_factors):
    """
    Plot the observed returns vs fitted values.

    Arguments:
    stock_returns : pandas Series
        Observed stock returns.
    residuals : pandas Series
        Residuals from the regression model.
    intercept : float
        Intercept term from the regression model.
    beta : numpy array
        Beta coefficients from the regression model.
    macro_factors : pandas DataFrame
        Macro factors used in the regression model.
    """
    fig, ax = plt.subplots()
    ax.scatter(stock_returns, stock_returns - residual, label='Observed Returns')
    ax.plot(stock_returns, intercept + np.dot(macro_factors, beta), color='red', label='Fitted Values')
    ax.set_xlabel('Observed Returns')
    ax.set_ylabel('Fitted Values')
    ax.legend()
    plt.show()

#____________________________________________________________________________________________________________________________________#

if __name__ == "__main__":
    # Define the start and end dates
    start_date = "2013-01-01"
    end_date = "2023-01-01"

    # Define the Fred tickers and corresponding column names to obtain macro factors
    fred_tickers = {
        'RIFSPFFNA': 'RATES',
        'GDPC1': 'GDP',
        'FPCPITOTLZGUSA': 'CPI',
        'UNRATE': 'UNRATE',
        'UMCSENT': 'CONS_SENT',
    }

    # Createa dataframes of stock returns and macro factors, and a list of current factor values
    stock_returns, macro_factors, factor_values = get_stock_returns_and_macro_factors(start_date, end_date, fred_tickers, 'SP500')

    # Calculate the parameters of the factor model
    intercept, beta, residual = calculate_params(stock_returns, macro_factors)

    # Calculate the return of asset i based on the macroeconomic factor model
    factor_model_return = macro_factor_model_return(intercept, beta, factor_values, residual)
    print(factor_model_return)

    # Plot the observed vs fitted values
    plot_observed_vs_fitted(stock_returns, residual, intercept, beta, macro_factors)