"""
Multi linear regression generalizes linear regression - allows the dependent
varibale to be a linear function of multiple independent variables
"""

import pandas as pd
import pandas_datareader.data as wb
import numpy as np
import datetime as dt
from datetime import timedelta
import statsmodels.api as sm
from statsmodels import regression
import matplotlib.pyplot as plt

end = dt.datetime.now()
start = end - timedelta(days=2000)

asset1 = str(raw_input('Enter ticker 1: ')).upper()
asset2 = str(raw_input('Enter ticker 2: ')).upper()

Tickers = ([[asset1,asset2]])
df = pd.DataFrame()
for t in Tickers:
    df[t] = wb.DataReader(t, 'yahoo',start,end)['Adj Close']

# creating the benchmark index
bent = str(raw_input('Enter the ticker of the benchmark: ')).upper()
benchmark = wb.DataReader(bent,'yahoo',start,end)['Adj Close']

# linear regression of the two assets
slr = regression.linear_model.OLS(df[asset1],sm.add_constant(df[asset2])).fit()
print('SLR Beta of asset 2: ', slr.params[1])

# multiple linear regression using asset2 and benchmark as the independent variables
# column stack takes a sequence of 1-D arrays and stacks them as columns to make 2-D
mlr = regression.linear_model.OLS(df[asset1],sm.add_constant(np.column_stack((df[asset2],benchmark)))).fit()
prediction = mlr.params[0] + mlr.params[1] + mlr.params[2]*benchmark
prediction.name = 'Prediction'
print('MLR beta of asset 2', mlr.params[1], '\nMLR beta of benchmark: ', mlr.params[2])

# plotting the results of the linear regression
df[asset1].plot()
df[asset2].plot()
benchmark.plot()
prediction.plot(color='y')
plt.xlabel('Price')
plt.legend(bbox_to_anchor=(1,1), loc=2)
plt.show()

# outputs Anova table
mlr.summary()