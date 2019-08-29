import pandas as pd
import numpy as np
from numpy.random import randn

np.random.seed(55)
# (4,5) matrix size index = rows and columns are columns
dataframe = pd.DataFrame(randn(4,5),index=['p','q','r','s'], columns=['a','b','c','d','e'])
print(dataframe)
print(dataframe['a']) # outputs the column a
print(dataframe[['a','b']])
# you can add two dataframes together and create a new column
dataframe['f'] = dataframe['a'] + dataframe['b']
# removing columns
dataframe.drop('f',axis=1)

# selecting rows
print(dataframe.loc['q'])
# select row based off of position
print(dataframe.iloc[0]) # this is the first position
# select rows and columns
print(dataframe.iloc[:])
# multiple conditions that outputs part of the original matrix
print(dataframe[(dataframe['a']>0)&(dataframe['b']>0)])

# creating a dataframe with dictionary items within it as key
df = pd.DataFrame({'col1':[10,11,12,13], 'col2':[100,200,300,400], 'col3': ['abc','def','ghi','xyz']})
