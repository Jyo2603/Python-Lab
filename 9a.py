#9a. Develop a python program read a dataset and perform the following using Pandas
#• Visualize the dataset using plot ().
#• Draw the Scatter plot for the dataset on any column.
#• Display the scatter plot with different colors.
#• Draw the Histogram for the dataset on any column.

import matplotlib.pyplot as plt
iris.plot()
plt.show()

iris.plot(kind = 'scatter', x = 'petal.length', y = 'sepal.length')
plt.show()

x = iris['petal.length']
y = iris['sepal.length']
a = iris['petal.width']
b = iris['sepal.width']
plt.scatter(x, y, c='green')
plt.scatter(a, b, c='red')
plt.show()

iris['petal.length'].plot(kind = 'hist')
plt.show()
