part = ['b','a','c','f','d']
print(part)
print(part[3])
print(part[-1]) # prints the last element of a list
part[4] = '8' # this replaces the 5th element in the list
del part[1] # this deletes the element in the list
part.append("ben") # appends the string to the list
print(part[1:3]) # this print everything after position 1 and everything before position 3
part.index("c") # outputs the position of the element that you put in the parenthesis

numbers = [1,2,3,4,5,6]
numbers.sort() # this sorts the numbers in numerical order
numbers.sort(reverse=True) # this outputs the numbers in reverse order

#creating lists with range
range(10)
print(range(3,7)) # this will print 3,4,5,6 -- the ending number does not print
print(range(1,20,2)) # this prints starting at 1 and then adds 2 until the ending number

