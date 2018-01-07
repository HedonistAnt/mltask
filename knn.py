import numpy as np
from dsparse import  parse_classes,parse
from sklearn import neighbors, datasets

class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates = parse_classes()
X, Y, UX, VX, VY,traindates,vdates,udates = parse (class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates)



X1=[]
Y1=[]

X2=[]
Y2=[]

X3=[]
Y3=[]

X4=[]
Y4=[]

X5=[]
Y5=[]

for d in range(len(X)):
    if traindates[d]==29:
        X1.append(X[d])
        Y1.append(Y[d])
    if traindates[d]==30:
        X2.append(X[d])
        Y2.append(Y[d])
    if traindates[d]==1:
        X3.append(X[d])
        Y3.append(Y[d])
    if traindates[d]==2:
        X4.append(X[d])
        Y4.append(Y[d])
    if traindates[d]==3:
        X5.append(X[d])
        Y5.append(Y[d])


weight = 'distance'
metric = "pyfunc"
p=1
n_neighbors = 1
radius = 0.9
knn=neighbors.RadiusNeighborsClassifier(radius=radius, weights="distance", algorithm="auto", leaf_size=60, p=p, metric="minkowski")
#knn=neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights="distance", algorithm="auto", leaf_size=60, p=p, metric="minkowski", metric_params=None)
knn.fit(X, Y)
"""
acc=0
for v in range(len(VX)):
    vr = np.array(VX[v]).reshape(1, -1)
    r=knn.predict(vr)
    if r == VY[v]:
        acc += 1
acc = acc / len(VY)
print(acc)"""

text_file = open("Output.txt", "w")
for u in range( len(UX)):
    ur = np.array(UX[u]).reshape(1, -1)
    r=knn.predict(ur)
    if r == b'0':
        text_file.write("0\n")
    if r == b'1':
        text_file.write("1\n")
    if r == b'2':
        text_file.write("2\n")

text_file.close()


"""knn1=neighbors.RadiusNeighborsClassifier(radius=10, weights="distance", algorithm="brute", leaf_size=30, p=p, metric="minkowski", metric_params=None)
knn1.fit(X1, Y1)

knn2=neighbors.RadiusNeighborsClassifier(radius=10, weights="distance", algorithm="brute", leaf_size=30, p=p, metric="minkowski", metric_params=None)
knn2.fit(X2, Y2)

knn3=neighbors.RadiusNeighborsClassifier(radius=10, weights="distance", algorithm="brute", leaf_size=30, p=p, metric="minkowski", metric_params=None)
knn3.fit(X3, Y3)

knn4=neighbors.RadiusNeighborsClassifier(radius=10, weights="distance", algorithm="brute", leaf_size=30, p=p, metric="minkowski", metric_params=None)
knn4.fit(X4, Y4)

knn5=neighbors.RadiusNeighborsClassifier(radius=10, weights="distance", algorithm="brute", leaf_size=30, p=p, metric="minkowski", metric_params=None)
knn5.fit(X5, Y5)

acc=0
text_file = open("Output.txt", "w")
for v in range(len(VX)):
    vr = np.array(VX[v]).reshape(1, -1)
    if vdates[v]==29:
        r=knn1.predict(vr)

    if vdates[v]==30:
        r=knn2.predict(vr)

    if vdates[v]==1:
        r=knn3.predict(vr)

    if vdates[v]==2:
        r=knn4.predict(vr)

    if vdates[v]==3:
        r=knn5.predict(vr)

    if r==VY[v]:
        acc+=1
acc = acc/len(VY)
print(acc)
"""
"""for u in range( len(UX)):
    ur = np.array(UX[u]).reshape(1, -1)


    if udates[u]==29:
        r=knn1.predict(ur)

    if udates[u]==30:
        r=knn2.predict(ur)

    if udates[u]==1:
        r=knn3.predict(ur)

    if udates[u]==2:
        r=knn4.predict(ur)

    if udates[u]==3:
        r=knn5.predict(ur)

    if r==b'0':
        text_file.write("0\n")
    if r==b'1':
        text_file.write("1\n")
    if r==b'2':
        text_file.write("2\n")"""