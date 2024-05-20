## HIgher National Diploma in Science in Computing (Data Analytics)
## Programming and Scripting Module (8632: 2023-2024)
## Project Title: Exploratory  Data Analysis on the Iris Dataset Using Python
## Author: Ebelechukwu Chidimma Igwagu




### Project Description

This repository contains my analysis of the [Fisher’s Iris dataset](https://archive.ics.uci.edu/dataset/53/iris).  This project demonstrated the use of python programs and scripts in analysing data to provide meaningful insights. All analysis was performed with the Anaconda (Python 3.11.5) interpreter. The project comprises an [iris.py](https://github.com/Gtalen/pands-project/blob/main/iris.py) script, [iris.ipynb](https://github.com/Gtalen/pands-project/blob/main/iris.ipynb) notebook and [Analysis Output](https://github.com/Gtalen/pands-project/tree/main/Analysis%20Output).

### Overview
The [Fisher’s Iris dataset](https://archive.ics.uci.edu/dataset/53/iris) contains measured attributes on 3 different species of iris flower. Every row represents an instance of an iris plant. The dataset is made of 150 rows of 50 species each of setosa, versicolor, and virginica iris flower. The measured attributes in centimeters were petal length, petal width, sepal length and sepal width. The credit for the original data source was attributed to [Edgar Anderson](https://en.wikipedia.org/wiki/Edgar_Anderson).


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
import scipy.stats as stats
```
### Loading the dataset

The iris dataset was accessed [here]((https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv). 

```
# Importing the raw iris dataset

iris_data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

```
### The [Iris](https://github.com/Gtalen/pands-project/blob/main/iris.py) python Script
This script was used to perform an exploratory data analysis (EDA) on the iris dataset. A summary of the script's function is given below;
- Imports the necessary libraries
- Defines a function for performing EDA "iris_EDA"
- Assigns an output directory for the function
- Loads the dataset
- Performs a basic data exploration; Data shape, structure, types and descriptive statictics
- Data Integrity check
- Data Manipulation
- Data Visualization
- Statistical testing
- Saves all the analysis output and plots to the [Analysis Output](https://github.com/Gtalen/pands-project/tree/main/Analysis%20Output).


- 
### Statistical Models
Follow along with the project and you will be able to test all of the models;

1 **Descriptivee statistics**
- Barcharts
- Histograms 
- Boxplot:

2 **Correlation Analysis**  
-  Scatterplots
- Heatmap correlation matrix
- Pairplots

3 **Regression Analysis

### Analysis Steps 
Basic analysis applied

- Data Exploration
- Data Manipulation
- Data Visualization
- Statistical testing
- Data findings 


 ### Conclusion


### Contributors
- Ebelechukwu Chidimma Igwagu

- Eager to contribute? This project is open to external contribution.

### License



### References
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html
- https://codeblockhub.com/python-tutorial-iris-dataset/
- https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda
- https://www.geeksforgeeks.org/detect-and-remove-the-outliers-using-python/
- https://realpython.com/pandas-groupby/
- https://www.youtube.com/watch?v=Oe7PwgPolDQ
- https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.select_dtypes.html
- https://en.wikipedia.org/wiki/Iris_flower_data_set
- https://www.analyticsvidhya.com/blog/2020/07/univariate-analysis-visualization-with-illustrations-in-python/
- https://seaborn.pydata.org/generated/seaborn.kdeplot.html
- https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda
- https://careerfoundry.com/en/blog/data-analytics/what-is-an-outlier/
-https://neuraldatascience.io/5-eda/data_cleaning.html
