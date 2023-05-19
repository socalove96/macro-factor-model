# Macro Factor Model Repository

This repository, located at [https://github.com/socalove96/macro-factor-model.git](https://github.com/socalove96/macro-factor-model.git), contains the code and files for my Macro Factor Model project.

## Description

The Macro Factor Model project focuses on building a statistical model that captures the relationships between macroeconomic factors and asset returns. By analyzing various macroeconomic indicators, the model aims to provide insights into the factors that drive asset price movements and help inform investment decisions.

## Features

- **Macro Factor Model Implementation:** The repository includes the implementation of the macro factor model, which utilizes statistical techniques to estimate the impact of macroeconomic factors on asset returns.
- **Data Processing:** It provides functions for processing and cleaning macroeconomic data, preparing it for analysis and model estimation.
- **Factor Analysis:** The project includes tools for conducting factor analysis to identify and select the most relevant macroeconomic factors.
- **Model Estimation and Evaluation:** It offers functions for estimating the model parameters and evaluating the performance and predictive power of the macro factor model.
- **Visualization:** The repository includes visualizations of the macroeconomic data, factor loadings, and model output to facilitate interpretation and analysis.

## Installation

To set up and run this Macro Factor Model project locally, please follow these steps:

1. Clone the repository using the following command:
   ```
   git clone https://github.com/socalove96/macro-factor-model.git
   ```

2. Navigate to the project directory:
   ```
   cd macro-factor-model
   ```

3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

4. Run the main script or explore the Jupyter notebooks provided to understand and utilize the Macro Factor Model functionality.

# Macroeconomic Factor Model

The provided code includes a factor model implemented in Python using the pandas, numpy, statsmodels, matplotlib, os, yfinance, and pandas_datareader libraries. The factor model aims to analyze stock returns and their relationship with macroeconomic factors. Here's a description of the factor model implemented in the code:

The **get_stock_returns_and_macro_factors** function retrieves stock returns and macroeconomic factors from the FRED (Federal Reserve Economic Data) API and processes the data. It retrieves data for the S&P 500 index and various macroeconomic indicators. The data is resampled on an annual basis and filtered to exclude specific date ranges (e.g., financial crisis and pandemic periods). The function returns the stock returns, macroeconomic factors, and the latest values of the macroeconomic factors.

The **calculate_params** function estimates the parameters of the factor model using Ordinary Least Squares (OLS) regression. It adds a constant column to the macroeconomic factors, fits the regression model, and extracts the intercept, beta coefficients (factor loadings), and residuals. The function prints a summary of the regression results and returns the calculated parameters.

The **macro_factor_model_return** function calculates the return of an asset based on the macroeconomic factor model equation. It takes the intercept, beta coefficients, macroeconomic factor values, and an error term as inputs. The function multiplies the beta coefficients by the macroeconomic factor values, calculates the dot product, and adds the intercept and error term to obtain the return of the asset.

The **plot_observed_vs_fitted** function plots the observed returns versus the fitted values obtained from the factor model regression. It provides a visual representation of how well the model fits the observed data.

The main part of the code initializes the start and end dates, defines the Fred tickers and column names for macroeconomic factors, calls the get_stock_returns_and_macro_factors function to retrieve the data, calls the calculate_params function to estimate the factor model parameters, calculates the return of an asset using the macro_factor_model_return function, and finally, plots the observed versus fitted values using the plot_observed_vs_fitted function.

This factor model analyzes the relationship between stock returns and macroeconomic factors, estimates the model parameters using regression, and provides a visual assessment of the model's performance.


# Limitations to the code
**Simplified model representation:** The code assumes a simple linear relationship between stock returns and macroeconomic factors. In reality, the relationship may be more complex and nonlinear. The factor model implemented here may not capture all the intricacies and dynamics of the actual relationship.

**Limited macroeconomic factors:** The code uses a predefined set of macroeconomic factors from the FRED API. While these factors are commonly used, they may not capture all relevant economic variables that can influence stock returns. The model's accuracy and predictive power depend on the choice and availability of macroeconomic factors.

**Assumptions of linearity and independence:** The factor model assumes a linear relationship between stock returns and macroeconomic factors. It also assumes that the factors are independent of each other and do not exhibit multicollinearity. Violations of these assumptions can affect the model's reliability and accuracy.

**Data limitations:** The code retrieves stock returns and macroeconomic factors from the FRED API within the specified date range. The accuracy and representativeness of the results heavily depend on the quality, availability, and timeliness of the data. If the data is incomplete, contains errors, or exhibits data gaps, it can impact the model's performance.

**Model overfitting:** The code does not include a validation or testing phase for the factor model. It's important to evaluate the model's performance on out-of-sample data to assess its generalization ability. Overfitting, where the model performs well on the training data but poorly on new data, could be a concern.

**Limited scope:** The code focuses on a specific factor model implementation and its application to a particular dataset. It does not cover other advanced techniques, alternative factor models, or considerations specific to different industries or investment strategies. The factors and code presented should be adapted and extended based on the specific requirements and context of the analysis.

## Contributing

Thank you for your interest in contributing to the Macro Factor Model project! If you have any suggestions, bug reports, or improvements, please feel free to open an issue or submit a pull request. Your contributions are greatly appreciated.

## License

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the `LICENSE` file for more details.

## Contact

If you have any questions or would like to reach out, please feel free to contact me via email at [alex.malek96@gmail.com](mailto:alex.malek96@gmail.com).

Thank you for visiting the Macro Factor Model repository!
