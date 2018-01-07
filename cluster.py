import numpy as np
from dsparse import  parse_classes,parse
from sklearn.cluster import KMeans
class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates = parse_classes()
X, Y, UX, VX, VY,traindates,vdates,udates = parse (class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates)

kmeans = KMeans(n_clusters=3, random_state=0).fit(VX)

for i in range(len(VX)):
    print(kmeans.fit_predict(np.array(VX[i]).reshape(-1,1)), VY[i])