from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris = load_iris()

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(iris.data)

print("Cluster Labels:")
print(kmeans.labels_)