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
iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Opening the output text file
f = open('irisoutput.txt', 'a')

print (iris_data, file = f)

# Viewing the first 5 rows of the dataset
print(iris_data.head(), file = f)

# Viwing the last 5 rows of the dataset
print(iris_data.tail(), file = f)

# Scrolling through the entire dataset
print(iris_data.to_string(), file=f)

# Viewing the data structure and types

print(iris_data.info(), file = f)

# Descriptives: Summary statistics of the numerical variables
print(iris_data.describe())

# Descriptives: Categorical variables
# Counting the species in the dataset
print(iris_data['species'].value_counts(), file=f)

# PLotting the Countplot
sns.countplot(iris_data, x='species').set_title('Iris dataset species countplot')
plt.show()

# Plotting a histogram for the numerical variables
fig, ax = plt.subplots(2, 2, figsize = (13, 8))
fig.suptitle ('Iris dataset numerical variable Histogram')

# Setting up the subplots
sns.histplot(data=iris_data, x='sepal_length', hue='species',  multiple='stack', kde=True, ax = ax [0, 0])
sns.histplot(data=iris_data, x='sepal_width', hue='species',   multiple='stack', kde=True, ax = ax [0, 1])
sns.histplot(data=iris_data, x='petal_length', hue='species',multiple='stack', kde=True, ax = ax [1, 0])
sns.histplot(data=iris_data, x='petal_width', hue='species', multiple='stack',kde=True, ax = ax [1, 1])

# Displaying the plot
plt.show()

# Plotting a swarm[plot by species]
fig, ax = plt.subplots(2, 2, figsize = (15, 15))
fig.suptitle ('Iris Dataset swarm plots by species')

#creating chart for each subplot
sns.swarmplot(data=iris_data, y='sepal_length', x ='species', hue ='species', ax = ax [0, 0])
sns.swarmplot(data=iris_data, y='sepal_width',  x ='species', hue ='species', ax = ax [0, 1])
sns.swarmplot(data=iris_data, y='petal_length', x ='species', hue ='species', ax = ax [1, 0])
sns.swarmplot(data=iris_data, y='petal_width',  x ='species', hue ='species', ax = ax [1, 1])

# Displaying the plot
plt.show()

### Data Cleaning and  Manipulation

# Creating a copy of the dataset before cleaning up the data
iris = iris_data.copy()
print(iris, file = f)

# checking for missing values
print(iris.isna().sum(), file =f)

# Checking for the total number of duplicates
print(iris.duplicated().sum(), file=f)

# Extracting the duplicate rows
print(iris[iris.duplicated()], file=f)

# Rechecking the value count per specie
print(iris['species'].value_counts(), file=f)

### Outlier Mining

#### Visualizing Outliers
##### Boxplot

# Boxplot
fig, ax = plt.subplots(2, 2, figsize = (13, 8))
fig.suptitle ('Iris Dataset numerical variable Boxplots')

#creating chart for each subplot
#plot 1: row 1, column 1
sns.boxplot(data=iris, x='species', y='sepal_length', ax = ax [0, 0])

#plot 2: row 1, column 2
sns.boxplot(data=iris, x='species', y='sepal_width', ax = ax [0, 1])

#plot 3: row 2, column 1
sns.boxplot(data=iris, x='species', y='petal_length', ax = ax [1, 0])

#plot 4: row 2, column 2
sns.boxplot(data=iris, x='species', y='petal_width', ax = ax [1, 1])

plt.show()

# Using pandas groupby to group the dataset by sepcie
iris_species = iris.groupby('species')
print(iris_species.count(), file=f)

# Define outlier function
def IQR_outlier(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR
    outliers = df[((df<(lower_limit)) | (df>(upper_limit)))]
    return outliers



















