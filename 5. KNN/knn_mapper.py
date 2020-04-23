import sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import operator
from hdfs import InsecureClient

# count = 1

train_data = []

# test_data = []
client_hdfs = InsecureClient('http://localhost:9870')
with client_hdfs.read('/home/mydemo/knn_test/Test.csv', encoding = 'utf-8') as reader:
	test_data = pd.read_csv(reader, index_col = 0)


count = 0

for line in sys.stdin:

	line = line.strip()

	if count == 0:
		pass

	else:

		val = list(map(float, line.split(",")))

		train_data.append(val)

	count +=1


new_train = pd.DataFrame(train_data)

y_train = new_train.iloc[:,-1]
X_train = new_train.iloc[:, 1:48]
X_test = test_data

scaler = MinMaxScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.fit_transform(X_test)

def get_distance(X_train, X):
	#Reference: https://medium.com/@souravdey/l2-distance-matrix-vectorization-trick-26aa3247ac6c
	dists = -2 * np.dot(X, X_train.T) + np.sum(X_train**2, axis=1) + np.sum(X**2, axis=1)[:, np.newaxis]
	return dists

def knn(X_train,X_test,Y_train, k=0):
	final = []
	dist = get_distance(X_train,X_test)
	sortDist = np.argsort(dist, axis=1)
	filtered = sortDist[:,:k]
	#print(sortDist)
	#print(filtered)
	for i in filtered:
		#votes={}
		labels = []
		for j in i:
			z = Y_train.iloc[j]
			# print(int(z), "\t" ,end = " ")
			labels.append(int(z))
		print(labels)
		# print()


result = knn(X_train_norm,X_test_norm,y_train,k=5)

