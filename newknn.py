import numpy as np
from dsparse import  parse_classes
from sklearn import neighbors, datasets

X,Y,UX= parse_classes()
VX = []
VY = []
c=0

while c<len(X):

    if c%10 ==0:
        VX.append(X[c])
        del X[c]
        VY.append(Y[c])
        del Y[c]
    c += 1


knn=neighbors.KNeighborsClassifier(n_neighbors=10, weights="distance", algorithm="auto", leaf_size=60, metric="minkowski", metric_params=None)
knn.fit(X,Y)
print(knn.score(VX,VY))