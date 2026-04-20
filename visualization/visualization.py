# -*- coding: utf-8 -*-
"""visualization.ipynb

"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
# %matplotlib inline
import warnings

tips=sns.load_dataset("tips")
df=pd.DataFrame(tips)
df.head()

"""**Preprocessing and Exploratory Data Analysis**

checking for missing data
"""

df .isnull().sum()

"""Viewing the descriptive statistics of the dataset"""

df.describe()

"""Get a numerical summary for 'tip'"""

df.tip.describe ()

"""Five Number Summary For bill and tip"""

bill = df.total_bill
print("Maximum Bill", np.max(bill))
print("Minimum Bill", np.min (bill))
print("Standard Deviation",np.std(bill))
print("Median", np.median (bill))
print("Mean ",np.mean (bill))

tip = df.tip
print("Maximum Tip",np.max(tip))
print("Minimum Tip",np.min(tip))
print("Standard Deviation", np.std(tip))
print("Median", np.median (tip))
print("Mean", np.mean(tip))

"""**Exploratory data analysis**

Explore if there is any dependency between the variable "Tip" and rest of the variables.
"""

sns.countplot(x='sex', data=tips)
sns.despine()
print(tips.sex.value_counts())

sns.countplot(x='sex', data=tips,hue='smoker',palette='viridis')

plt.figure(figsize=(8,6))
plt.title("Tips Per Day of Week")
sns.countplot(x=tips['day'], color='purple')

sns.catplot(x='day', data=tips, hue='sex', palette='ch:.25', kind='count')

sns.distplot(df['tip'])

g=sns.distplot(tips.tip, kde=False)
g.set_title('Tip Amount Histogram')

plt.figure(figsize=(20,5))
sns.boxplot(x=bill, color='b')

"""outliers in tip column"""

plt.figure(figsize=(20,5))
sns.boxplot(x=tip, color='g')

"""IQR value"""

bill_tip = pd.DataFrame(df,columns=['total_bill', 'tip', 'size'])
print(bill_tip)
print("IQR For Total Bill: ",stats.iqr(bill))
print("IQR For Tip: ",stats.iqr(tip))

sns.relplot(x='total_bill',y='tip',data=df,col='time', hue='smoker',size='size')

plt.figure(figsize=(12,10))
sns.scatterplot (data=df,x="total_bill",y="tip", hue="sex");

"""Can see a linaer pattern ie as total bill increases tip also increases."""

sns.lmplot(x='total_bill',y='tip',data=df,col='time', hue='smoker')

sns.catplot(x='day',y='tip',data=df,kind='swarm')

sns.catplot(x="time", y="tip", data=df, height=6, kind="bar", palette="muted")

sns.catplot(x='day',y='tip', data=df,kind="violin")

sns.pairplot(df, hue='sex')

# Inference: The pairplot reveals several key insights into the relationships between numerical variables, differentiated by gender:
# Male customers (blue points) are more numerous and exhibit a wider spread, particularly at higher `total_bill` and `tip` values.
# Their distributions for these variables tend to extend further than those of female customers.
# Female customers (orange points) are present across the spectrum but are less frequently associated with the very highest `total_bill` and `tip` amounts.
# For instance, `total_bill` and `tip` both appear right-skewed for both genders, indicating more frequent smaller values and fewer large values.

"""Correlation Matrix"""

corr_matrix=df.corr(numeric_only=True)
ax=sns.heatmap(data=corr_matrix,annot=True,vmax=1,vmin=-1,center=0)
bottom, top=ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)

"""Converting categorical variables into numerical values so that the machine learning model can understand."""

from sklearn.preprocessing import LabelEncoder
labelencoder_df=LabelEncoder()
df['sex']=labelencoder_df.fit_transform(df['sex'])
df['smoker']=labelencoder_df.fit_transform(df['smoker'])
df['day']=labelencoder_df.fit_transform(df['day'])
df['time']=labelencoder_df.fit_transform(df['time'])
df.head()

# Inference:
# This transformation is essential for preparing the data for machine learning models, as they typically require numerical input rather than
# text-based categories.

"""Creating heatmap including these numerical values"""

corr_matrix=df.corr(numeric_only=True)
ax=sns.heatmap(data=corr_matrix,annot=True,vmax=1,vmin=-1,center=0)
bottom, top=ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)

# The ideal scenario would be serving a larger group of non-smoking male customers during dinner on a Saturday or Sunday,
# as they are most likely to incur a high total bill and leave a substantial tip.
