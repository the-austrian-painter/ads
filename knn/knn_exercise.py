# -*- coding: utf-8 -*-
"""knn_exercise.ipynb


# Exercise 1
"""

from sklearn.datasets import load_wine
import pandas as pd

wine_data = load_wine()
X = pd.DataFrame(wine_data.data, columns=wine_data.feature_names)
y = wine_data.target

print(X.head())

from sklearn.neighbors import NearestNeighbors
import numpy as np

k = 5
nbrs = NearestNeighbors(n_neighbors=k)
nbrs.fit(X)

distances, indices = nbrs.kneighbors(X)

kth_distances = distances[:, -1]

threshold = np.mean(kth_distances) + 2 * np.std(kth_distances)
anomalies = X[kth_distances > threshold]

print("Detected anomalies:")
print(anomalies)

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], label='Normal', alpha=0.6)
plt.scatter(X_pca[kth_distances > threshold, 0],
            X_pca[kth_distances > threshold, 1],
            color='red', label='Anomaly', edgecolor='black', s=100)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Wine Dataset: k-NN Anomaly Detection')
plt.legend()
plt.show()

"""# Exercise 2"""

from sklearn.datasets import load_breast_cancer
import pandas as pd

cancer_data = load_breast_cancer()
X = pd.DataFrame(cancer_data.data, columns=cancer_data.feature_names)
y = cancer_data.target

print(X.head())

from sklearn.neighbors import NearestNeighbors
import numpy as np

k = 5
nbrs = NearestNeighbors(n_neighbors=k)
nbrs.fit(X)

distances, indices = nbrs.kneighbors(X)

kth_distances = distances[:, -1]

threshold = np.mean(kth_distances) + 2 * np.std(kth_distances)
anomalies = X[kth_distances > threshold]

print(f"Number of anomalies detected: {len(anomalies)}")
print(anomalies)

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

plt.figure(figsize=(8,6))
plt.scatter(X_pca[:,0], X_pca[:,1], label='Normal', alpha=0.6)
plt.scatter(X_pca[kth_distances > threshold, 0],
            X_pca[kth_distances > threshold, 1],
            color='red', label='Anomaly', edgecolor='black', s=80)
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Breast Cancer Dataset: k-NN Anomaly Detection')
plt.legend()
plt.show()
