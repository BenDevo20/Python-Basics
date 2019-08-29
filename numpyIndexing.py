import numpy as np

# creating a sample array
arr_example = np.arange(0,11) # with no interval it prints every number
# getting value at an index position
print(arr_example[8])
# getting values in a range
print(arr_example[1:5]) # position 1 is not the first position

# broadcasting. setting value with index range
arr_example[0:5]=100

# indexing a 2D array (matrices)
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d[1]) # this indexes a row
print(arr_2d[1][0]) # gets row and then position in the row