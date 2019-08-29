"""
numpy is a linear algebra library for python - PyData ecosystem rely on NumPy
as one of their main building blocks

numpy is fast, has bindings to C libraries
"""
import numpy as np

# example of a list
list_1 = [1,2,3]
# assign a list to a variable
list_array = np.array(list_1)
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

# arange - return evenly spaced values within a general interval
np.arange(0,11,2) # start, end, interval - will not include last number

# generate array of zeros and ones
np.zeros(3) # row vector
np.zeros((5,5)) # matrix size
np.ones(3,3)

# linspace - return evenly spaced numbers over a specified interval
x = np.linspace(0,10,3)# start, end, number of positions
y = np.linspace(0,10,50) # it will find 50 numbers between 0 and 10 that are evenly spaced

# generating an identity matrix
i = np.eye(4) # number in the parenthesis is the size of the matrix

# random variables
np.random.rand(2) # the number is size of the matrix
np.random.rand(5,5) # 5x5 matrix of random numbers 0 - 1

np.random.randn(2) # this is different then the above because it is not uniform 
