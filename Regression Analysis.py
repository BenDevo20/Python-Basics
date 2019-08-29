import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

# This follows the same format as excel -- you can index by rows and columns
data = pd.read_excel('Housing.xlsx')
# calling the columns that you want
# need to use double bracket since they are two different one dimensional arrays
print(data[['House Price', 'House Size (sq.ft.)']])

# running univariate regression
# defining variables by their columns names in excel
x = data['House Size (sq.ft.)']
y = data['House Price']

#outputting graphs using matplotlib
plt.scatter(x,y)
plt.axis([0,2500,0,1500000]) # setting the axis should be based off of the x and y variables that are in the data set
plt.ylabel('House Price')
plt.xlabel('House Size (Sq ft)')
plt.show()