import matplotlib.pyplot as plt
import numpy as np
from random import sample

# linspace creates numeric sequences - evenly spaced numbers structured as array
a = np.linspace(0,5,11)
b = a**2

# creating simple line plot
plt.plot(a,b,'g*', label='Example 2')
plt.xlabel('X axis title')
plt.ylabel('Y axis title')
plt.title('Top title here')

# generate multisubplots on same canvas
plt.subplot(1,2,1) #subplot(nrows, ncols, plot_number)
plt.plot(a,b,'b--') #color options
plt.subplot(1,2,2)
plt.plot(b,a,'r*-')
plt.show()

# generating pie charts
labels = 'frogs', ' hogs', 'Dogs', 'Logs'
sizes = [15,30,45,10]
explode = (0,0.1,0,0) # exploding means separate a certain chunk of the pie
figl, ax1 = plt.subplots()
# if you create the inputs for a pie chart prior you can easily manage the data
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') # equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# generate histogram
data = sample(range(1, 1000), 100)
plt.hist(data)
plt.show()