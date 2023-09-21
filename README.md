# Insurance Data Analysis Using Python
This Python script showcases an analysis of insurance-related data and demonstrates linear regression modeling. It employs various libraries, including numpy, pandas, matplotlib, seaborn, and scikit-learn, to perform data exploration and modeling. The primary steps are as follows:

Table of Contents
1. Introduction
2. Installation
3. Usage
4. Data Source
5. Data Visualization
6. Linear Regression Model
7. Visualization of Regression Results
8. Screenshots

# Introduction
The main objective of this data is exploring and analyzing a dataset related to insurance information and conducting a simple linear regression analysis to predict BMI based on age. It covers the following tasks:

● Loading data from a CSV file. 
● Data cleaning and preprocessing. 
● Creating various plots using Matplotlib and Seaborn for data visualization. 
● Implementing a linear regression model to predict bmi according age group.

# Installation
1. Clone this repository: git clone https://github.com/

2. Navigate to the project directory: cd Insurance

3. Install the required Python packages using pip: pip install pandas numpy matplotlib seaborn scikit-learn

Or
Download Zip and Install requirements.txt write command : pip install -r requirements.txt

# Usage
1. Run the Python script: python insurance.py

2. The script will load the Insurance data, perform analysis, generate plots, and display them.

# Data Source
The script starts by loading an insurance dataset from a CSV file named 'insurance.csv'. The dataset contains essential information such as 'age,' 'sex,' 'bmi,' 'region,' and 'charges' for individuals.

Data Exploration
Basic information about the dataset is displayed, including the first few rows, shape, and statistical summary.
Data is divided into two age groups: 'oldAge' (age >= 55) and 'youngAge' (age < 55).
Within these groups, data is further segmented based on gender into 'oldAgeMale,' 'oldAgeFemale,' 'youngAgeMale,' and 'youngAgeFemale.' The size and sample of each subgroup are also presented.

# Data Visualization
Several data visualization techniques are employed to gain insights:

● Barplot: A barplot is created using Seaborn to compare 'bmi' among 'oldAge' individuals, distinguished by gender and region.
● Bar Chart: A bar chart is generated to visualize the frequency of smokers within different age groups.
● Lineplot: Seaborn is used to produce a lineplot that illustrates the relationship between 'age' and 'charges,' with hue differentiation by gender.
● Violinplot: A violinplot is created to display the distribution of 'charges' across different regions.
● Countplot: Seaborn's countplot is utilized to visualize the count of individuals within specific 'age' groups, segregated by gender.
● Histplot: A histogram plot is generated to visualize the distribution of 'bmi' values with specified edge color and fill color.

# Linear Regression Model
The script proceeds to perform a linear regression analysis to predict 'bmi' based on 'age':
● Data is split into training and testing sets using the train_test_split function.
● A Linear Regression model is trained using the training data.
● Predictions are made on the test data using the trained model.
● The Mean Squared Error (MSE) is computed to evaluate the model's performance.

# Visualization of Regression Results
● A DataFrame named 'record' is created to hold both the actual 'BMI' values and the predicted 'BMI' values from the regression model.
● A line plot is generated using Seaborn to visually compare the actual and predicted 'BMI' values against 'age.' The plot provides insights into how well the regression model approximates 'BMI' based on 'age.'
● This script serves as a comprehensive example of data analysis and linear regression modeling, offering valuable insights into the provided insurance dataset. It can be adapted for similar regression tasks and serves as an educational resource for data analysis enthusiasts and aspiring data scientists.


# Screenshots

![1](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/722f8792-ee1e-4185-8955-097025c7c5dd)

![2](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/43b4fc7f-10f6-4535-9b8c-41c89d2ff06c)

![3](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/949a47b7-9be6-45e5-8013-e192f5ae0818)

![4](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/e4abbeb6-3bf0-4ee8-af67-b94d010d4f9a)

![5](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/1015288d-13e6-4b67-86ce-7f7d5c47b752)

![6](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/15b8aafb-7a72-4aa6-9d74-01351eabbc6b)

![7](https://github.com/Keshajani12/Insurance-Data-Analysis-Using-Python/assets/143489586/19f69e58-d34f-499f-81df-ab01ce32fb58)
