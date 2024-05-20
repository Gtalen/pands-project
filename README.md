## HIgher National Diploma in Science in Computing (Data Analytics)
## Programming and Scripting Module (8632: 2023-2024)
## Project Title: Exploratory  Data Analysis on the Iris Dataset Using Python
## Author: Ebelechukwu Chidimma Igwagu




### Project Description

This repository contains my analysis of the [Fisher’s Iris dataset](https://archive.ics.uci.edu/dataset/53/iris).  This project demonstrated the use of python script in analysing data to provide meaningful insights. All analysis was performed with the Anaconda (Python 3.11.5) interpreter. The project comprises an [iris.py](https://github.com/Gtalen/pands-project/blob/main/iris.py) script, [iris.ipynb](https://github.com/Gtalen/pands-project/blob/main/iris.ipynb) notebook and [Analysis Output](https://github.com/Gtalen/pands-project/tree/main/Analysis%20Output).

### Overview
The [Fisher’s Iris dataset](https://archive.ics.uci.edu/dataset/53/iris) contains measured attributes on 3 different species of iris flower. Every row represents an instance of an iris plant. The dataset is made of 150 rows of 50 species each of setosa, versicolor, and virginica iris flower. The petal length, petal width, sepal length and sepal width of the iris flowers  were the measured attributes. All measurements were in centimeters. The credit for the original data source was attributed to [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson).

![Iris](https://github.com/Gtalen/pands-mywork/blob/main/project/iris%20image.png)


<div>
<img src = '<div>
<img src = 'https://uk.images.search.yahoo.com/images/view;_ylt=AwrNah4_HEpmbEUDQ9VNBQx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkA2E4MGEwMDI1ZTdmOTE3ZWI2NjY2OTk5NzdmZjc3OTgwBGdwb3MDMwRpdANiaW5n?back=https%3A%2F%2Fuk.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dthe%2Biris%2Bdataset%26fr%3Dmcafee%26tab%3Dorganic%26ri%3D3&w=1400&h=502&imgurl=www.embedded-robotics.com%2Fwp-content%2Fuploads%2F2022%2F01%2FIris-Dataset-Classification.png&rurl=https%3A%2F%2Fwww.embedded-robotics.com%2Firis-dataset-classification%2F&size=309.3KB&p=the+iris+dataset&oid=a80a0025e7f917eb666699977ff77980&fr2=&fr=mcafee&tt=Iris+Dataset+Classification+Using+3+Machine+Learning+Algos&b=0&ni=200&no=3&ts=&tab=organic&sigr=xNARYprdCeLI&sigb=X.01Pn0Fmz1x&sigi=IUOeD5VBGqEU&sigt=sPgH93UVv7c6&.crumb=K.SUh56FdNo&fr=mcafee', width = height = '400/'>
</div>

Photocredit: [Awais Naeem](https://www.embedded-robotics.com/iris-dataset-classification/)', width = height = '400/'>
</div>

### Installation

```
- Install Anaconda python Interpreter

- Install Visual studio code

```
### USAGE

### Prerequisites


The libraries used for this project were Pandas, Numpy, matplotlib_pyplot, Seaborn and Sciplot.stats. These packages can be accessed via the Anaconda package. Aadditional requirements can be installed using pip install. 

#### Importing the requirements
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings    # importing python warning module
sns.set_theme()            #setting seaborn as default style for plots when using matplotlib
```

### Loading the dataset

The iris dataset was accessed [here]((https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv). 

```
# Importing the raw iris dataset

iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

```
### The [Iris](https://github.com/Gtalen/pands-project/blob/main/iris.py) python Script
This script was used to perform an exploratory data analysis (EDA) on the iris dataset. A summary of the script's function is given below;

1. Imports the necessary libraries needed for EDA
2. Defines a function for performing EDA called "iris_EDA"
     - Assigns an output directory to the function were the analysis output was saved
     - Loads the dataset
     - Performs a basic data exploration; Data shape, structure, types and descriptive statictics
     - Data Integrity check and data maipulation; Missing values, duplicates, outliers
     - Data Visualization: Countplot, Histograms, Boxplot, striplot, violin plot 
     - Data Analysis:  Descriptive statictics, univariate and bivariate analysis
     - Statistical testing: Correlation and regression analysis: Correlation coefficient and Heatmap.
3. Used the python system standout module to direct and save all the analysis output and plots to the [Analysis Output folder](https://github.com/Gtalen/pands-project/tree/main/Analysis%20Output).

### Results
- [Iris dataset Analysis Summary](https://github.com/Gtalen/pands-project/blob/main/iris.py)
- [Countplot of the Iris species](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Countplot%20of%20the%20Iris%20species.png).
-[Histogram of the iris numeric dataset](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Histograms%20of%20num%20var.png).
-[Histogram of the iris numeric dataset by specie](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Histograms%20of%20num%20var%20by%20specie.png).
- [Stripplot of the iris  datasets by specie](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Stripplot%20by%20Iris%20species.png)
- [Boxplot with outliers](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Boxplot%20Iris%20outliers.png)
- [Boxplot without outliers](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Boxplot%20Iris%20-%20no%20outliers.png)
- [Pairplot of the relation between the numeric variables](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Pairplot%20of%20the%20Iris%20dataset.png)
- [Heatmap - Correaltion analysis](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Heatmap%20of%20the%20Iris%20dataset.png)
- [Scatterplot: Correlation and Regression: Petal length vs petal width](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Regression%20-%20Scatterplot%20of%20iris%20petal%20length%20and%20petal%20width.png)
- [Correlation and Regression: Petal length vs petal width](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Corr%20and%20Reg%20analysis%20on%20the%20iris%20petal%20length%20and%20petal%20width.png)
- [Violinplots by iris species](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Iris%20datset%20Dataset%20violin%20plots%20by%20species.png)

## Discussion
This project utilised python funtions and modules alongside  other prerequisite libraries in analysing the iris dataset.

### Data Exploration
 Data eexploration involved using the data head and tail functions to get a quick overview of the first and last five rows in the dataset respectively. Descriptive statistics was used to summarize the data.

#### Table 1: ![Iris Dataset Descriptives](https://github.com/Gtalen/pands-mywork/blob/main/data-analytics-mywork/Iris%20Descriptive%20Summary%20table.png)

#### Figure-1 Countplot of the Categorical Variales
![Countplot of the Iris species](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Countplot%20of%20the%20Iris%20species.png).

### Data Structure
There are four float (numeric) data type variables and one object (categorical) type.  None of all the 150 measured variables in the datset are of the non null type. There are 50 instances each for the setosa, versicolor and virginica.

#### Table 2

### Univariate Analysis

A univariate analysis involves exploring a datset from one dimension by looking at a single variable as described here by [Sruthi Sudheer](https://www.analyticsvidhya.com/blog/2020/07/univariate-analysis-visualization-with-illustrations-in-python/). A striplot and histogram were plotted using Seaborn and Matplotlib.  A histogram was used to visualize the frequency of occurence of each of the measured attributes. The addition of kernel density estimate (KDE) and species was used to add depth to the plot to provide more information about the dataset. [Kdeplot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) is useful for visualizing observation distribution.

Figure 2 - Histogram of the Iris dataset Categorical Variables
![Histogram of the iris numeric dataset by specie](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Histograms%20of%20num%20var%20by%20specie.png).

#### Histograms and Stripplots Insights

- Iris setosa has a longer sepal width, a distinct shorter petal length and petal width compared to the versicolor and virginica which has some overlap in this regard.
- Iris Virginica has the longets sepal length and sepal width
- The petal lengthand petal width of the iris versicolor lies in between the setosa and virginica
 However, there is some overlap in the iris versicolor and virginica's sepal length and sepal width as well as the sepal width of iris setosa.
- The KDE plot showed a normal distribution of the numeric variables

### Data Quality Checks and manipulation

A copy of the dataset was created before any data manipulations was done as to preserve the original data integrity. The iris data set has no missing values and one duplicate row. However, the duplicate row was ignored because the species value count showed equal number for each of the specie ([Figure 1]()). This was to avoid introducing analytical bias due to the small sample size of the iris dataset.

### Outlier Mining
An outlier is a value that differs significantly from the rest of the dataset. The interquartile method was used to detect within-species outliers in the iris dataset and these were visualized with a Boxplot. In the boxplot, observations outside the whiskers are the outliers. Outliers using the interquartile method are data points that are 1.5 times the interquartile range.

#### Outlier Summary

The IQR method identified a total of 13 outliers in the dataset across all 3 species. 8 of these were from the iris setosa, 5 from iris virginica and and 1 from iris versicolor. The sepal length and sepal width has the highest numebr of outliers of 5 each, 2 from the petal width and 1 from the petal length. Non outliers were represented as not a number. The outliere were not dropped due to the small sample size. Another approach would have been utilizing either the imputation or winsorizing method as described [here](https://neuraldatascience.io/5-eda/data_cleaning.html)  though not done in this analysis. The outliers were visualized using a boxplot.

Figure 2: Iris Dataset Boxplot with outliers
![Boxplot with outliers](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Boxplot%20Iris%20outliers.png)

The outliers were removed from the boxplot only and not from the dataset by using the seaborn library in (Figure 3]())
Figure 3: Iris Dataset Boxplot without outliers
![Boxplot without outliers](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Boxplot%20Iris%20-%20no%20outliers.png)

### Bivariate Analysis

The [Seaborn pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html) was used to visualise the pairwise relationship between variables. The kernel density plot was plotted diagonally alongside the scatterplot of the paired variables in the iris dataset. The KDE plot showed the normal distribution of the iris dataset. The scatterplot showed a linear relationship between the numeric variables. The petal length and petal width of the iris setosa were distinctly shorter than the iris versicolor and virginica in the scatterplot.

Figure 4: Pairplot of the Iris datset
![Pairplot of the relation between the numeric variables](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Pairplot%20of%20the%20Iris%20dataset.png)

## Correlation Analysis
This was performed to understand the strength of the relationship between the numeric variables. Pandas' Corr() method based off the pearson's correlation coefficient was used to calculate the correlation coefficient across all the variables in the iris dataset. This was plotted using the Seaborn heatmap.

### Hypothesis
**Null Hypothesis:** There is a relationship between the the iris petal length and the iris petal width. 

**Alternate Hypothesis** There is no relationship between the the iris petal length and the iris petal width.

Figure 5: Heatmap of the Iris dataset
![Heatmap - Correaltion analysis](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Heatmap%20of%20the%20Iris%20dataset.png)

### Correlation Summary
The correlation coefficient of the pairwise relationship between the iris dataset numeric variables ranged from r = -0.12 to 1. The correlation between the sepal length and sepal width was the weakest ( r = -0.12). A strong postive correlation of 1 was observed when the variables were paired within themselves (eg. Petal length vs petal length). 

#### Testing the Null hypothesis
The Pearson's correlation coeffiient for the petal length and the petal width of the iris dataset was r = 0.96 signifying a strong positve correlation. Hence, the null hypothesis was accepted.


#### Regression Analysis
The linear relationship between the iris petal length and petal depth was analysed. The iris petal width was the dependent variable and the petal length the independent variable.The slope was calculated to be 0.42 and the intercept -0.36.  If every other variable should remain constant, this implies that for every millimeter increase in the iris petal length will, an expected increase of 0.42mm is expected in the iris petal width. 
Figure 6 (Petal length vs Petal width Scatterplot with Regression line)
![Scatterplot: Correlation and Regression: Petal length vs petal width](https://github.com/Gtalen/pands-project/blob/main/Analysis%20Output/Regression%20-%20Scatterplot%20of%20iris%20petal%20length%20and%20petal%20width.png)



 
 ### Conclusion


### Contributors
- Ebelechukwu Chidimma Igwagu

- Eager to contribute? This project is open to external contribution.

### License



### Sources

- Atlassian (Accessed 10/04/2024) Essential chart types for data Visualization | Atlassian. https://www.atlassian.com/data/charts/essential-chart-types-for-data-visualization.
- Bevans, R. (2023). Types of variables in Research & Statistics | Examples. https://www.scribbr.com/methodology/types-of-variables/.
- Bobbitt, Z. (2021). How to Make Heatmaps with Seaborn (With Examples). https://www.statology.org/seaborn-heatmap/.
- Codeblockhub.com (2023) &apos;Data analysis of Iris Dataset : A tutorial,&apos; CodeBlockHub - Code. Create. Innovate., 25 October. https://codeblockhub.com/python-tutorial-iris-dataset/.
- Directing print output to a .txt file (Accessed 01/05/2024). https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file#:~:text=You%20can%20redirect%20stdout%20into%20a,file%20%22output.txt%22%3A%20import%20sys%20sys.stdout%20%3D%20open%28%27output.txt%27%2C%27wt%27%29.
- Exploratory Data Analysis on IRIS Dataset in Python | Flexiple (Accesed 12/05/2024). https://flexiple.com/python/exploratory-data-analysis-on-iris-dataset.
- GeeksforGeeks (2024a) Exploratory data analysis on IRIS Dataset. https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/.
- GeeksforGeeks (2024b) Ways to save Python terminal output to a text File. https://www.geeksforgeeks.org/ways-to-save-python-terminal-output-to-a-text-file/.
- Guest_Blog (2023) 12 Univariate data visualizations with illustrations in Python. https://www.analyticsvidhya.com/blog/2020/07/univariate-analysis-visualization-with-illustrations-in-python/.
- Matt Macarty (2021). Linear Regression Model Techniques with Python, NumPy, pandas and Seaborn. https://www.youtube.com/watch?v=EMIyRmrPWJQ.
- Nik (2023a) Calculate and plot a correlation matrix in Python and Pandas. https://datagy.io/python-correlation-matrix/.
- Numpy.polyfit — NumPy v1.26 Manual (Accessed 01/05/2024). https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html.
- Pandas (2024). How to select, filter, and subset data in Pandas dataframes (2021). https://practicaldatascience.co.uk/data-science/how-to-select-filter-and-subset-data-in-pandas-dataframes.
- Pandas.DataFrame.duplicated — pandas 2.2.2 documentation (Accessed 20/04/2024). https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html.
- Pandas.DataFrame.select_dtypes — pandas 2.2.2 documentation (Accessed 20/04/2024). https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html.
- Python Hub (2020) Introduction to IRIS dataset | Statistical Data Analysis | Python | Data Visualization. https://www.youtube.com/watch?v=Oe7PwgPolDQ.
- Python, R. (2023) pandas GroupBy: Your Guide to Grouping Data in Python. https://realpython.com/pandas-groupby/.
- Python, R. (2023) Plot With pandas: Python Data Visualization for Beginners. https://realpython.com/pandas-plot-python/#survey-your-data.
- Seaborn.boxplot — seaborn 0.13.2 documentation (Accessed 25/04/2024). https://seaborn.pydata.org/generated/seaborn.boxplot.html.
- Seaborn.kdeplot — seaborn 0.13.2 documentation (Accessed 25/04/2024). https://seaborn.pydata.org/generated/seaborn.kdeplot.html.
- Seaborn.pairplot — seaborn 0.13.2 documentation (Accessed 25/04/2024). https://seaborn.pydata.org/generated/seaborn.pairplot.html.
- Seaborn.scatterplot — seaborn 0.13.2 documentation (Accessed 25/04/2024). https://seaborn.pydata.org/generated/seaborn.scatterplot.html.
- Selvaraj, N. (2023) A Beginner’s Guide to data analysis in Python. https://365datascience.com/tutorials/python-tutorials/data-analysis-python/.
- Sequitin, K. (2023) &apos;What is an outlier? Data Analytics explained,&apos; CareerFoundry, 28 September. https://careerfoundry.com/en/blog/data-analytics/what-is-an-outlier/.
- Sharma, P. (2022a) &apos;Exploratory Data Analysis : IRIS Dataset - Analytics Vidhya - Medium,&apos; Medium, 7 January. https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda.
- Sharma, P. (2022b) &apos;Exploratory Data Analysis : IRIS Dataset - Analytics Vidhya - Medium,&apos; Medium, 7 January. https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda.
- Team, D. (2022) Data cleaning tutorial. https://www.datacamp.com/tutorial/tutorial-data-cleaning-tutorial.
- UCI Machine Learning Repository (Accessed 01/04/2024). https://archive.ics.uci.edu/dataset/53/iris.
- Vahi, Y. (2022) 'Exploratory Data Analysis (EDA): a complete roadmap to cleaning data,' Medium, 6 January. https://medium.com/codex/exploratory-data-analysis-a-roadmap-for-cleaning-3e01a0d694.
- Valcheva, S. (2024) Statistical Methods for Data Analysis: a Comprehensive Guide. https://www.intellspot.com/statistical-methods/.
- Wikipedia contributors (2024) Iris flower data set. https://en.wikipedia.org/wiki/Iris_flower_data_set.

### Referenced Sources
