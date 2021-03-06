"""
This program uses a multiple linear regression to study the effects of individual stocks on the overall market
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels import regression
import statsmodels.stats.diagnostic as smd
import scipy.stats as stats
import pandas_datareader.data as wb
import math as m
import datetime as dt
from datetime import timedelta as td
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# datetime.now() - always updates when run for the past 1000 days
end = dt.datetime.now()
start = end - td(days=999)

# stores the users tickers in a list - which are used as independent variables in regression
tick_list = np.array(str(input('Enter tickers: ')).upper().split())

# creating benchmark index - returns used for dependent variable for regression
benTik = [str(input('Enter ticker of benchmark index: ')).upper()]
bench = wb.DataReader(benTik, 'yahoo', start, end)['Adj Close']

# percent returns of benchmark index -- dependent variable
bench_ret = bench.pct_change().dropna()

# data frame where ticker (independent variable) data will be stored
df = pd.DataFrame()

# stores adjusted close for each ticker entered in tick_list in dataframe
for t in tick_list:
    df[t] = wb.DataReader(t, 'yahoo', start, end)['Adj Close']

# calculates percent return of each ticker that is stored in data frame
pct_ret = df.pct_change().dropna()
x = pct_ret[tick_list]

# runs regression - lambda used to index percent return by each position in tick_list
# maybe I should run a heteroscedasticity model - non-constant variance
mlr = regression.linear_model.OLS(bench_ret,sm.add_constant(np.column_stack(((map(lambda x: pct_ret[x],tick_list)))))).fit()
print(mlr.summary())
#print(mlr.params[1]*pct_ret[tick_list[0]])
# prediction line for regression
prediction = mlr.params[0] + mlr.params[1]*pct_ret[tick_list[0]] + mlr.params[2]*pct_ret[tick_list[1]] + mlr.params[3]*pct_ret[tick_list[2]]
print(prediction)

# Regression Analysis - residuals and errors
#residuals = mlr.resid

# graphing regression -- returns of independent and dependent variables
for t in tick_list:
    plt.plot(pct_ret[tick_list], label=tick_list)

plt.plot(bench_ret)
plt.plot(prediction)
plt.xlabel('Date')
plt.ylabel('Percent Returns')
plt.legend(bbox_to_anchor=(1.05,1), loc= 'upper left', borderaxespad=0)
plt.show()
