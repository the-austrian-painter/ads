# -*- coding: utf-8 -*-
"""dbscan_exercise.ipynb



# Exercise 1:
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
X = iris.data  # features

X_scaled = StandardScaler().fit_transform(X)

dbscan = DBSCAN(eps=0.8, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

unique_labels = set(labels)
print("Cluster labels:", unique_labels)

n_clusters = len(unique_labels) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print("Estimated number of clusters:", n_clusters)
print("Number of noise points:", n_noise)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))

for label in unique_labels:
    if label == -1:
        color = 'black'
        label_name = 'Noise (Outliers)'
    else:
        color = plt.cm.jet(label / max(unique_labels))
        label_name = f'Cluster {label}'

    plt.scatter(X_pca[labels == label, 0],
                X_pca[labels == label, 1],
                c=[color],
                label=label_name)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("DBSCAN Clustering on Iris Dataset")
plt.legend()
plt.show()

"""# Exercise 2:"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = load_breast_cancer()
X = data.data
y = data.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dbscan = DBSCAN(eps=2.5, min_samples=5)
labels = dbscan.fit_predict(X_scaled)

unique_labels = set(labels)

n_clusters = len(unique_labels) - (1 if -1 in labels else 0)
n_noise = list(labels).count(-1)

print("Cluster labels:", unique_labels)
print("Estimated number of clusters:", n_clusters)
print("Number of noise points:", n_noise)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(8,6))

for label in unique_labels:
    if label == -1:
        color = 'black'
        label_name = 'Noise (Outliers)'
    else:
        color = plt.cm.jet(label / max(unique_labels))
        label_name = f'Cluster {label}'

    plt.scatter(X_pca[labels == label, 0],
                X_pca[labels == label, 1],
                c=[color],
                label=label_name)

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("DBSCAN Clustering on Breast Cancer Dataset")
plt.legend()
plt.show()
