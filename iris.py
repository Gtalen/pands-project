"""
Analysis of the iris Dataset Using Python
By Ebelechukwu Chidimma Igwagu
"""

#importing the libraries
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings    #to handle default plot warning
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings    # importing python warning module
sns.set_theme()    #setting seaborn as default style for plots when using matplotlib

def iris_EDA(iris_output_dir):
    iris_output_dir = r'C:\Users\great\Desktop\pands\pands-project\Analysis Output\\'
    #importing the iris dataset to a pandas dataframe
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
    
    # Checking and summing up the non.null values
    print(iris_data.isnull().sum(), file=f)
    
    # Counting the species in the dataset
    iris_data['species'].value_counts()
    
    ## Descriptive Statistics
    # Summary statistics of the numeric variables for all 3 iris species
    print(iris_data.describe())
    
    ##  Summary statistics of the numeric variables by the iris species 
    print(iris_data.groupby('species').describe(), file =f)

    # Descriptives: Categorical variables
    # Counting the species in the dataset
    print(iris_data['species'].value_counts(), file=f)
    
    # PLotting the Countplot for the categorical variable
    sns.countplot(iris_data, x='species').set_title('Iris dataset species countplot')
    plt.savefig('Countplot of the Iris species.png')  #saves the plot
    plt.close()   # Closing the plot

    #creating a histogram for the numeric variables
    fig, ax = plt.subplots(2, 2, figsize = (13, 8))
    fig.suptitle ('Iris dataset numeric variable Histogram')
    
    # Setting up the subplots
    sns.histplot(data=iris_data, x='sepal_length', bins=20, ax = ax [0, 0])
    sns.histplot(data=iris_data, x='sepal_width', bins=20, ax = ax [0, 1])
    sns.histplot(data=iris_data, x='petal_length', bins=20, ax = ax [1, 0])
    sns.histplot(data=iris_data, x='petal_width', bins=20, ax = ax [1, 1])
    
    # Saving the plot
    plt.savefig('Histograms of num var.png')
    plt.close()   # Closing the plot

    # Plotting a histogram for the numeric variables by species
    fig, ax = plt.subplots(2, 2, figsize = (13, 8))
    fig.suptitle ('Iris dataset numeric variable Histogram by species')
  
  # Setting up the subplots
    sns.histplot(data=iris_data, x='sepal_length', hue='species', bins=20, multiple='stack', kde=True, ax = ax [0, 0])
    sns.histplot(data=iris_data, x='sepal_width', hue='species', bins=20, multiple='stack', kde=True, ax = ax [0, 1])
    sns.histplot(data=iris_data, x='petal_length', hue='species', bins=20, multiple='stack', kde=True, ax = ax [1, 0])
    sns.histplot(data=iris_data, x='petal_width', hue='species', bins=20, multiple='stack',kde=True, ax = ax [1, 1])
  
    # Saving the plot
    plt.savefig('Histograms of num var by specie.png')
    plt.close()   # Closing the plot
    
    # Plotting a swarm[plot by species]
    fig, ax = plt.subplots(2, 2, figsize = (15, 15))
    fig.suptitle ('Iris Dataset swarm plots by species')
    
    #creating chart for each subplot
    sns.stripplot(data=iris_data, y='sepal_length', x ='species', hue ='species', ax = ax [0, 0])
    sns.stripplot(data=iris_data, y='sepal_width',  x ='species', hue ='species', ax = ax [0, 1])
    sns.stripplot(data=iris_data, y='petal_length', x ='species', hue ='species', ax = ax [1, 0])
    sns.stripplot(data=iris_data, y='petal_width',  x ='species', hue ='species', ax = ax [1, 1])
    
    # Saving the plot
    plt.savefig('Stripplot by Iris species.png')
    plt.close()   # Closing the plot
    
    # Data Quality Checks
    ## Data Cleaning and  Manipulation
    
    # Creating a copy of the dataset before cleaning up the data
    iris = iris_data.copy()
    print(iris, file = f)
    
    # checking for missing values
    print(iris.isnull().sum(), file =f)
    
    # Checking for the total number of duplicates
    print(iris.duplicated().sum(), file=f)
    
    # Extracting the duplicate rows
    print(iris[iris.duplicated()], file=f)
    
    # Outlier Mining   
    # Outliers - Interquartile method 

    # Finding the Interquartile range by Iris Species
    # Using pandas groupby to group the dataset by species
    iris_species = iris.groupby('species')
    
    # Interquartile method for outliers
    # Counting each specie
    print(iris_species.count(), file=f) 
           
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
    
    # Summing up the total outliers in iris dataset
    outliers_sum = species_outliers.count().sum()
    print ((f'The total number of outlliers in the iris dataset using the IQR method is {outliers_sum}.'), file=f)

    ## Summing up the total outliers in iris dataset by attribute
    outliers_by_attribute = species_outliers.count()
    print ((f'The total number of outlliers in the iris dataset by attribute using the IQR method is: \n{outliers_by_attribute}'), file=f)
    
    # Counting the outliers by Specie
    ## Isolating the species in the dataset
    setosa = iris_species.get_group('setosa')
    versicolor = iris_species.get_group('versicolor')
    virginica = iris_species.get_group('virginica')

    # Selecting the numeric columns for each specie and applying IQR
    setosa_outliers = iris_species.get_group('setosa').select_dtypes(include=['float64']).apply(IQR_outlier)
    versicolor_outliers = iris_species.get_group('versicolor').select_dtypes(include=['float64']).apply(IQR_outlier)
    virginica_outliers = iris_species.get_group('virginica').select_dtypes(include=['float64']).apply(IQR_outlier)
    
    # Iris Setosa
    setosa_attribute_count = setosa_outliers.count()
    setosa_outliers_count = setosa_outliers.count().sum()
    print (setosa_outliers, file=f)
    print ((f'The iris setosa attribute count is \n{setosa_attribute_count}'), file=f)
    print ((f'The iris setosa total outlier count is {setosa_outliers_count}.'), file=f)

    # Iris Versicolor
    versicolor_attribute_count = versicolor_outliers.count()
    versicolor_outliers_count = versicolor_outliers.count().sum()
    print (versicolor_outliers, file=f)
    print ((f'The iris versicolor attribute count is \n{versicolor_attribute_count}'), file=f)
    print ((f'The iris versicolor total outlier count is {versicolor_outliers_count}.'), file=f)

    # Iris Virginica
    virginica_attribute_count = virginica_outliers.count()
    virginica_outliers_count = virginica_outliers.count().sum()
    print (virginica_outliers, file=f)
    print ((f'The iris virginica attribute count is \n{virginica_attribute_count}'), file=f)
    print ((f'The iris virginica total outlier count is {virginica_outliers_count}.'), file=f)

    ## Visualizing Outliers - Boxplot
    # Boxplots
    fig, ax = plt.subplots(2, 2, figsize = (13, 8))
    fig.suptitle ('Iris Dataset numeric variable Boxplots')
        
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
    fig.suptitle ('Iris Dataset numeric variable Boxplots excluding outliers')
        
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
    
    # Bivariate Analysis
    # creating a pairplot of the  iris dataset
    sns.pairplot(iris, hue = 'species', markers= ['o', 's','^'], height=3.5, aspect=1.02)
    
    # Creating the main title for the pairplot
    plt.suptitle('Pairplot of the Iris datset')
    
    # Suppressing the figure layout warning to make it tidy
    warnings.filterwarnings('ignore', message='The figure layout has changed to tight')
    plt.savefig('Pairplot of the Iris dataset.png') # Saving the plot
    plt.close()   # Closing the plot

    # Correlation Analysis
    
    # Selecting the numeric columns from the DataFrame
    iris_numeric = iris.select_dtypes(include=['float64'])
    
    # Calculating the correlation matrix of the numeric variables
    iris_numeric_corr = iris_numeric.corr()
    print (f'The iris dataset correlation coefficient: \n{iris_numeric_corr}.', file=f)


    # Heatmap - Correlation Matrix
    # Creating the heatmap with the correlation matrix 
    sns.heatmap(iris_numeric_corr, annot=True, cmap='coolwarm')
    
    # labelling the title
    plt.title('Iris Dataset numeric variables Correlation Matrix')
    plt.savefig('Heatmap of the Iris dataset.png') # Saving the plot
    plt.close()   # Closing the plot

    #printing off variables with strong correlation
    iris_numeric_corr = iris_numeric_corr.unstack()
    #abs to convert neg corr to pos corr
    strong_corr =iris_numeric_corr[abs(iris_numeric_corr) >= 0.7]   
    print ((f'The iris dataets variables with strong correlations are : \n {strong_corr}'), file=f)

    # Regression Analysis
    # Creating a short name for the variables
    plen = iris['petal_length']
    pwidth = iris['petal_width']
    plen = iris['sepal_length']
    swidth = iris['sepal_width']
    

    # creating the scatterplot of petal length and petal width
    sns.scatterplot(data=iris, x='petal_length', y='petal_width', hue='species')
    
    plt.title ('Scatterplot of iris petal length and petal width')
   
    #calculating the correlation coefficient
    plen_pwidth_corr  = iris['petal_length'].corr(iris['petal_width'])
    print ((f'The iris correlation coefficient of the petal length and width is {plen_pwidth_corr}.'), file=f)
    
    # calculating the slope(m) and intercept (c)
    m, c = np.polyfit(plen, pwidth, deg=1) # deg = 1 for lin reg
    
    #show
    print ((f'The slope is {m} and the intercept is {c}'), file=f)
    
    #creating the best fit line for petal length using its min and max values to gen 100 equally spaced values
    plen_values = np.linspace(min(plen), max(plen), 100)
    
    # generating the corresponding values for the petal width
    pwidth_values = m * plen_values + c
    
    # plotting the best fit line for bodymass vs flipper length
    plt.plot(plen_values, pwidth_values, color='black')


    # Additional plots
    # Regression pairplot
    sns.pairplot(data=iris, x_vars='petal_length', y_vars='petal_width', hue='species', height=6, aspect=1.02, kind='reg')
    plt.title('Relationship between iris petal length and petal width')
    plt.savefig('Corr and Reg analysis on the iris petal length and petal width.png') # Saving the plot
    plt.close()   # Closing the plot

    fig, ax = plt.subplots(2, 2, figsize = (15, 8))
    fig.suptitle ('Iris datset Dataset violin plots by species')
    
    #creating chart for each subplot
    sns.violinplot(data=iris, x='species', y='petal_length', hue = 'species',  ax = ax [0, 0])
    sns.violinplot(data=iris, x='species', y='petal_width', hue =  'species', ax = ax [0, 1])
    sns.violinplot(data=iris, x='species', y='sepal_length', hue = 'species', ax = ax [1, 0])
    sns.violinplot(data=iris, x='species', y='sepal_width', hue =  'species', ax = ax [1, 1])
    plt.savefig('Iris datset Dataset violin plots by species.png') # Saving the plot
    plt.close()   # Closing the plot

# Opening a text file to append the analysis output
with open ('irisoutput.txt', 'a') as f:
    original_stdout = sys.stdout  # Save the original standard output
    sys.stdout = f
    try:
        iris_EDA(r'C:\Users\great\Desktop\pands\pands-project\Analysis Output\\') # performs the exploratory data analysis on the iris dataset and prints the output functions
    finally:
        # Reset standard output to the original value
        sys.stdout = original_stdout

#f = open('irisoutput.txt', 'a')
print ('EDA, all done!')  # To confirm that the program ran
    