# -*- coding: utf-8 -*-
"""smote_exercise.ipynb


Exercise 1
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from imblearn.over_sampling import SMOTE

df = pd.read_csv("creditcard.csv")

df.isnull().sum()

df.describe()

df["Class"].value_counts()

X = df.drop("Class", axis=1)
y = df["Class"]

scaler = StandardScaler()
X[["Amount","Time"]] = scaler.fit_transform(X[["Amount","Time"]])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Before SMOTE")
print("Confusion Matrix\n", confusion_matrix(y_test, pred))
print("Accuracy:", accuracy_score(y_test, pred))
print("Precision:", precision_score(y_test, pred))
print("Recall:", recall_score(y_test, pred))
print("F1 Score:", f1_score(y_test, pred))

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)

model2 = LogisticRegression(max_iter=1000)
model2.fit(X_res, y_res)
pred2 = model2.predict(X_test)

print("\nAfter SMOTE")
print("Confusion Matrix\n", confusion_matrix(y_test, pred2))
print("Accuracy:", accuracy_score(y_test, pred2))
print("Precision:", precision_score(y_test, pred2))
print("Recall:", recall_score(y_test, pred2))
print("F1 Score:", f1_score(y_test, pred2))

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# probabilities for ROC
y_prob = model.predict_proba(X_test)[:,1]
y_prob_smote = model2.predict_proba(X_test)[:,1]

# ROC values
fpr1, tpr1, _ = roc_curve(y_test, y_prob)
fpr2, tpr2, _ = roc_curve(y_test, y_prob_smote)

auc1 = roc_auc_score(y_test, y_prob)
auc2 = roc_auc_score(y_test, y_prob_smote)

plt.figure(figsize=(7,5))
plt.plot(fpr1, tpr1, label=f'Before SMOTE (AUC = {auc1:.3f})')
plt.plot(fpr2, tpr2, label=f'After SMOTE (AUC = {auc2:.3f})')

plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()

"""Exercise 2"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from imblearn.over_sampling import SMOTE

cols = ['ID','Diagnosis','radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean',
        'compactness_mean','concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean',
        'radius_se','texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se',
        'concave points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst',
        'perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst',
        'concave points_worst','symmetry_worst','fractal_dimension_worst']
df = pd.read_csv("wdbc.data",names=cols)

df.shape

df.isnull().sum()

df.describe()

df["Diagnosis"].value_counts()

df["Diagnosis"] = df["Diagnosis"].map({"M":1,"B":0})
df = df.drop("ID", axis=1)

X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,stratify=y,random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
pred = model.predict(X_test)

print("\nBefore SMOTE")
print("Confusion Matrix\n", confusion_matrix(y_test,pred))
print("Accuracy:", accuracy_score(y_test,pred))
print("Precision:", precision_score(y_test,pred))
print("Recall:", recall_score(y_test,pred))
print("F1 Score:", f1_score(y_test,pred))

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train,y_train)

model2 = LogisticRegression(max_iter=1000)
model2.fit(X_res,y_res)
pred2 = model2.predict(X_test)

print("\nAfter SMOTE")
print("Confusion Matrix\n", confusion_matrix(y_test,pred2))
print("Accuracy:", accuracy_score(y_test,pred2))
print("Precision:", precision_score(y_test,pred2))
print("Recall:", recall_score(y_test,pred2))
print("F1 Score:", f1_score(y_test,pred2))

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# probabilities for ROC
y_prob = model.predict_proba(X_test)[:,1]
y_prob_smote = model2.predict_proba(X_test)[:,1]

# ROC values
fpr1, tpr1, _ = roc_curve(y_test, y_prob)
fpr2, tpr2, _ = roc_curve(y_test, y_prob_smote)

auc1 = roc_auc_score(y_test, y_prob)
auc2 = roc_auc_score(y_test, y_prob_smote)

plt.figure(figsize=(7,5))
plt.plot(fpr1, tpr1, label=f'Before SMOTE (AUC = {auc1:.3f})')
plt.plot(fpr2, tpr2, label=f'After SMOTE (AUC = {auc2:.3f})')

plt.plot([0,1],[0,1],'k--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve Comparison")
plt.legend()
plt.show()
