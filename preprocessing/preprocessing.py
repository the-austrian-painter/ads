# -*- coding: utf-8 -*-
"""preprocessing.ipynb

"""

import pandas as pd
import numpy as np
students = [[86, 'M', 'verygood'], [95, 'F', 'excellent'], [75, None, 'good'], [np.nan, 'M', 'average'], [71, 'M', 'good'], [np.nan, None, 'verygood'], [92, 'F', 'verygood'], [99, 'M', 'excellent']]

dfstud = pd.DataFrame(students)

dfstud.columns = ['marks', 'gender', 'result']

dfstud

dfstud.isnull().values.sum()

X = dfstud.iloc[:,0:2].values
y = dfstud.iloc[:,2].values
type(X)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X[:,0:1] = imputer.fit_transform(X[:,0:1])
print(X)

imputer = SimpleImputer(missing_values=None, strategy='constant', fill_value='M')
X[:,1:2] = imputer.fit_transform(X[:,1:2])
print(X)

"""*Conclusion*

We can use Sklearn.impute class SimpleImputer to impute missing values for both numerical and categorical features.
For numerical missing values a strategy such as mean, median, most freq. and constant can be used.
For categorical features a strategy such as most frequent and constant can be used.
"""

import pandas as pd
import numpy as np

ds = pd.read_csv('/content/CountryAgeSalary.csv')

ds

X = ds.iloc[:, :-1].values
Y = ds.iloc[:,3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X[:,1:2] = imputer.fit_transform(X[:,1:2])
print(X)

imputer = SimpleImputer(missing_values=np.nan, strategy='median')
X[:,2:3] = imputer.fit_transform(X[:,2:3])
print(X)

"""Conclusion

We can use Sklearn.impute class SimpleImputer to impute missing values for both numerical features on imported datasets. For numerical missing values a strategy such as mean, median, most freq. and constant can be used.
"""

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])
print(X)

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

columntransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')

X = np.array(columntransformer.fit_transform(X), dtype=str)
print(X)

"""Conclusion

LabelEncoder is used when the categorical data is ordinal i.e. it has a specific order and we have large number of categorical values available.
OneHotEncoder is used when the categorical datais not ordinal and the categories are less.
"""

ds = pd.read_csv('/content/CountryAgeSalary.csv')

X1 = X[:, 3:5]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X1)
scaled_features = scaler.transform(X1)
df_MinMax = pd.DataFrame(scaled_features, columns=['Age', 'Salary'])
df_MinMax

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
sc_X = scaler.fit_transform(X1)
sc_X = pd.DataFrame(sc_X, columns=['Age', 'Salary'])
sc_X

"""Conclusion

Standardization is used when features have different scales and the model assumes data is normally distributed as Gausian Distribution.
Normalization is used when features need to be scaled to a fixed range like 0-1 and not normally distributed.
"""

