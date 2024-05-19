"""
Analysis of the iris Dataset Using Python
By Ebelechukwu Chidimma Igwagu
"""

#importing the libraries
import sys
import seaborn as sns
sns.set_theme()            #setting seaborn as default style for plots when using matplotlib
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def iris_EDA(iris_output_dir):
    #importing the iris dataset from the web to the variable iris
    iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
    print (iris_data, file = f)
    
    # Data Exploration
    # Viewing the first 5 rows of the dataset
    print(iris_data.head(), file = f)
    
    # Viewing the last 5 rows of the dataset
    print(iris_data.tail(), file = f)
    
    # Viewing the total number of columns and rows
    print(iris_data.shape, file=f)

    # Scrolling through the entire dataset
    print(iris_data.to_string(), file=f)
    
    # Printing off the unique species in the dataset.
    print(iris_data['species'].unique(), file=f)
    
    # Viewing the data structure and types
    
    print(iris_data.info(), file = f)
    
    # Checking and summng up the non.null variables
    print(iris_data.isnull().sum(), file=f)
    
    # Counting the species in the dataset
    iris_data['species'].value_counts()
    
    # Descriptives: Summary statistics of the numerical variables
    print(iris_data.describe())
    
    # Descriptives: Categorical variables
    # Counting the species in the dataset
    print(iris_data['species'].value_counts(), file=f)
    
    # PLotting the Countplot for the categorical variable
    sns.countplot(iris_data, x='species').set_title('Iris dataset species countplot')
    plt.savefig('Countplot of the Iris species.png')  #saves the plot
    plt.close()   # Closing the plot

    # Plotting a histogram for the numerical variables
    fig, ax = plt.subplots(2, 2, figsize = (13, 8))
    fig.suptitle ('Iris dataset numerical variable Histogram')
    
    # Setting up the subplots
    sns.histplot(data=iris_data, x='sepal_length', hue='species',  multiple='stack', kde=True, ax = ax [0, 0])
    sns.histplot(data=iris_data, x='sepal_width', hue='species',   multiple='stack', kde=True, ax = ax [0, 1])
    sns.histplot(data=iris_data, x='petal_length', hue='species',multiple='stack', kde=True, ax = ax [1, 0])
    sns.histplot(data=iris_data, x='petal_width', hue='species', multiple='stack',kde=True, ax = ax [1, 1])
    
    # Saving the plot
    plt.savefig('Histograms of num var.png')
    plt.close()   # Closing the plot
    
    # Plotting a swarm[plot by species]
    fig, ax = plt.subplots(2, 2, figsize = (15, 15))
    fig.suptitle ('Iris Dataset swarm plots by species')
    
    #creating chart for each subplot
    sns.swarmplot(data=iris_data, y='sepal_length', x ='species', hue ='species', ax = ax [0, 0])
    sns.swarmplot(data=iris_data, y='sepal_width',  x ='species', hue ='species', ax = ax [0, 1])
    sns.swarmplot(data=iris_data, y='petal_length', x ='species', hue ='species', ax = ax [1, 0])
    sns.swarmplot(data=iris_data, y='petal_width',  x ='species', hue ='species', ax = ax [1, 1])
    
    # Saving the plot
    plt.savefig('Swarmplot by Iris species.png')
    plt.close()   # Closing the plot
    
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
    
    plt.savefig('Boxplot Iris outliers.png') # Saving the plot
    plt.close()   # Closing the plot
    
    
    # Removing the outliers from the boxplot
    fig, ax = plt.subplots(2, 2, figsize = (13, 8))
    fig.suptitle ('Iris Dataset numerical variable Boxplots')
    
    #creating chart for each subplot
    #plot 1: row 1, column 1
    sns.boxplot(data=iris, x='species', y='sepal_length', showfliers=False, ax = ax [0, 0])
    
    #plot 2: row 1, column 2
    sns.boxplot(data=iris, x='species', y='sepal_width', showfliers=False, ax = ax [0, 1])
    
    #plot 3: row 2, column 1
    sns.boxplot(data=iris, x='species', y='petal_length', showfliers=False, ax = ax [1, 0])
    
    #plot 4: row 2, column 2
    sns.boxplot(data=iris, x='species', y='petal_width', showfliers=False, ax = ax [1, 1])
    
    plt.savefig('Boxplot Iris - no outliers.png') # Saving the plot
    plt.close()   # Closing the plot

    # Outlier detection - Interquartile method 
    # Finding the Interquartile range by Iris Species
    # Using pandas groupby to group the dataset by species
    iris_species = iris.groupby('species')
    
    # Counting each specie
    print(iris_species.count(), file=f) 
    
    # Isolating the species in the dataset
    setosa = iris_species.get_group('setosa')
    versicolor = iris_species.get_group('versicolor')
    virginica = iris_species.get_group('virginica')
    
    # Selecting the numerical columns for each specie
    setosa =iris_species.get_group('setosa').select_dtypes(include=['float64'])
    versicolor =iris_species.get_group('versicolor').select_dtypes(include=['float64'])
    virginica =iris_species.get_group('virginica').select_dtypes(include=['float64'])
    
    # Defining a function to detect outliers by interquartile method
    def IQR_outlier(df):
        Q1 = df.quantile(0.25)     # Finding the 25th percentile
        Q3 = df.quantile(0.75)     # Finding the 75th percentile
        IQR = Q3 - Q1              # Interquartile range
        lower_limit = Q1 - 1.5 * IQR   # defining the lower limit of the range
        upper_limit = Q3 + 1.5 * IQR   # defining the upper limit of the range
        outliers = df[((df<(lower_limit)) | (df>(upper_limit)))]
        return outliers
       
    # finding outliers in the dataset by species 
    outliers = iris_species.apply(IQR_outlier)
    
    # Dropping rows where all the elements are not a number(NAN)
    species_outliers = outliers.dropna(how='all')  
    print (species_outliers, file=f)
    
    
    # f.close()
    iris_output_dir = r'C:\Users\great\Desktop\pands> cd .\pands-project\\'

# Opening a text file to append the analysis output
with open ('irisoutput.txt', 'a') as f:
    original_stdout = sys.stdout  # Save the original standard output
    sys.stdout = f
    try:
        iris_EDA(r'C:\Users\great\Desktop\pands\pands-project\\') # performs the exploratory data analysis on the iris dataset and prints the output functions
    finally:
        # Reset standard output to the original value
        sys.stdout = original_stdout

#f = open('irisoutput.txt', 'a')
print ('EDA, all done!')  # To confirm that the program ran
    