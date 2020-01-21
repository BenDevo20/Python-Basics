"""
This program uses a multiple linear regression to study the effects of individual stocks on the overall market
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels import regression
import pandas_datareader.data as wb
import datetime as dt
from datetime import timedelta as td
import matplotlib.pyplot as plt

end = dt.datetime.now()
start = end - td(days=999)
# stores the users tickers in a list - independent variable
tick_list = np.array(str(input('Enter tickers: ')).upper().split())
#print(tick_list)
# creating benchmark index - dependent variable
benTik = [str(input('Enter ticker of benchmark index: ')).upper()]
#print(benTik)
bench = wb.DataReader(benTik, 'yahoo', start, end)['Adj Close']
#print(bench)
# returns of benchmark index
bench_ret = bench.pct_change().dropna()
#print(bench_ret)
# data frame where ticker data will be stored
df = pd.DataFrame()
for t in tick_list:
    df[t] = wb.DataReader(t, 'yahoo', start, end)['Adj Close']
pct_ret = df.pct_change().dropna()
#print(pct_ret)
#print(pct_ret)
#df2 = pd.DataFrame(pct_ret)
#print(df2)
#for t in tick_list:

index = 0
asset_pos = index
print(tick_list[0:2])
print(pct_ret[tick_list])

x = pct_ret[tick_list]

print(type(x))
slr = regression.linear_model.OLS(bench_ret,sm.add_constant(np.column_stack(((map(lambda x: pct_ret[x,tick_list])))))).fit()
#slr = regression.linear_model.OLS(bench_ret,sm.add_constant(np.column_stack((pct_ret[tick_list[asset_pos]],pct_ret[tick_list[1]])))).fit()

#print(slr.summary())
