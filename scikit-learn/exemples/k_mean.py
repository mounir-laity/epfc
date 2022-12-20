import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
# Générer des données:
X, y = make_blobs(n_samples=100, centers = 3, cluster_std=0.5,
random_state=0)
#nb_features = 2 par défaut
plt.scatter(X[:,0], X[:, 1])
# Entrainer le modele de K-mean Clustering
model = KMeans(n_clusters=3)
model.fit(X)
#Visualiser les Clusters
predictions = model.predict(X)
plt.scatter(X[:,0], X[:,1], c=predictions)
plt.show()