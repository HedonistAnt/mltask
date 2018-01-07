import numpy as np
from dsparse import  parse_classes,parse
from sklearn import svm
from sklearn.cluster import k_means, MiniBatchKMeans

class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates = parse_classes()
X, Y, UX, VX, VY,traindates,vdates,udates = parse (class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates)
clf = MiniBatchKMeans(n_clusters=3, max_iter=100, batch_size=100, verbose=0, compute_labels=True, random_state=None,
                      tol=0.0, max_no_improvement=10, init_size=None, n_init=3, reassignment_ratio=0.01)
clf.fit(X, Y)
acc=0
for v in range(len(VX)):
    vr = np.array(VX[v]).reshape(1, -1)
    r=clf.predict(vr)
    print(r)
    print(VY[v])
acc = acc/len(VY)
print(acc)