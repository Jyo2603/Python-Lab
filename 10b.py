#10b. Write a python program to read the Iris dataset and perform the following operations using Pandas
#• Display first 5 rows of the dataset.
#• Display last 5 rows of the dataset.
#• Display the information about the dataset.
#• Display the overview of the values of each column.
#• Visualize the dataset using plot ().

import pandas as pd
iris = pd.read_csv("iris.csv")
iris.head(5)
iris.tail(5)
iris.describe()
iris.info()

import matplotlib.pyplot as plt
iris.plot()
plt.show()
