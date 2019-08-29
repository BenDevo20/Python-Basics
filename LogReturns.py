import pandas as pd
import pandas_datareader.data as wb
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from datetime import timedelta

end = dt.datetime.now()
start = end - timedelta(days=1500)

tickers = ['MSFT', 'AAPL']
df = pd.DataFrame()
for t in tickers:
    df[t] = wb.DataReader(t, 'yahoo', start, end)['Adj Close']

df['MSFT Log return'] = np.log(df['MSFT'] / df['MSFT'].shift(1))
log_return_d = df['MSFT Log return'].mean()
