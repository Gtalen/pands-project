"""
Analysis of the iris Dataset Using Python
By Ebelechukwu Chidimma Igwagu
"""

#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
sns.set_theme()            #setting seaborn as default style for plots when using matplotlib

#importing the iris dataset from the web to the variable iris
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# opening the output text file
f = open('irisoutput.txt', 'a')

print (iris, file = f)

#viewing the first 5 rows of the dataset
print(iris.head(), file = f)

#viwing the last 5 rows of the dataset
print(iris.tail(), file = f)

#scrolling through the entire dataset
print(iris.to_string(), file=f)

#Viewing the data structure and types

print(iris.info(), file = f)

print(iris.describe())

# Descriptives
# Categorical variables

# Counting the species in the dataset
print(iris['species'].value_counts(), file=f)

# Categorical Variables - Countplot

sns.countplot(iris, x='species').set_title('Iris dataset species countplot')
plt.show()

#creating a histogram for the numerical variables
fig, ax = plt.subplots(2, 2, figsize = (13, 8))
fig.suptitle ('Iris dataset numerical variable Histogram')

# Setting up the subplots
sns.histplot(data=iris, x='sepal_length', hue='species',  multiple='stack', kde=True, ax = ax [0, 0])
sns.histplot(data=iris, x='sepal_width', hue='species',   multiple='stack', kde=True, ax = ax [0, 1])
sns.histplot(data=iris, x='petal_length', hue='species',multiple='stack', kde=True, ax = ax [1, 0])
sns.histplot(data=iris, x='petal_width', hue='species', multiple='stack',kde=True, ax = ax [1, 1])

plt.show()













