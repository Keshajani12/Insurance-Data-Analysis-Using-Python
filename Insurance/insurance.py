import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Get data from csv file
df=pd.read_csv('Insurance/insurance.csv')
print(df.head())
print(df.shape)
print(df.describe())

# Find data based on age 
oldAge= df[df.age>= 55]
print(oldAge.head())
print(oldAge.shape)

# Find data based on gender
oldAgeMale= oldAge[oldAge.sex== 'male']
print(oldAgeMale.head())
print(oldAgeMale.shape)

oldAgeFemale= oldAge[oldAge.sex== 'female']
print(oldAgeFemale.head())
print(oldAgeFemale.shape)

# Find data based on age
youngAge=df[df.age <55 ]
print(youngAge.head())
print(youngAge.shape)

# Find data based on gender
youngAgeMale= youngAge[youngAge.sex == 'male']
print(youngAgeMale.head())
print(youngAgeMale.shape)

youngAgeFemale= youngAge[youngAge.sex == 'female']
print(youngAgeFemale.head())
print(youngAgeFemale.shape)

# ============================================================================================================================================================================

# Create Barplot using Seaborn
sns.barplot(data=oldAge,x='sex',y='bmi',hue='region')
plt.show()

pd.crosstab(df.age,df.smoker).plot(kind='bar')
plt.show()

# Create Lineplot using Seaborn
sns.lineplot(data=df,x='age',y='charges',errorbar=None,hue='sex')
plt.show()

# Create Violinplot using Seaborn
sns.violinplot(data=df,x='region',y='charges')
plt.show()

# Create Countplot using Seaborn
sns.countplot(data=df,x='age',hue='sex')
plt.show()

# Create Histplot using Seaborn
sns.histplot(data=df,x='bmi',edgecolor='black',color='red')
plt.show()

# =================================================================================================================================================================================================================================================

# Split data into X (age) and y (bmi)
x=df[['age']]
y=df['bmi']

x_test,x_train,y_test,y_train= train_test_split(x,y,train_size=0.3)
print(x_train.head())
print(x_test.head())

lr=LinearRegression()
lr.fit(x_train,y_train)
y_predict=lr.predict(x_test)
print(y_test.head())
print(y_predict[:5])

# Find mean value of test and predicted data
mse= mean_squared_error(y_test,y_predict)
print(mse)

# Create a DataFrame to hold the actual and predicted BMI
record = pd.DataFrame({
    'Actual BMI': y_test,
    'Predicted BMI': y_predict
})

# Create a line plot using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=record)
plt.title("Actual vs. Predicted BMI")
plt.xlabel("BMI")
plt.ylabel("Age")
plt.show()