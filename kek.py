import numpy as np
from dsparse import  parse_classes
from sklearn import neighbors, datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import cross_val_score,cross_val_predict
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import GridSearchCV
X,Y,UX= parse_classes()


"""n_estimators = np.array([1000])
#min_samples = np.array(range(2,10,1))
criterion = np.array(["gini","entropy"])
max_features = np.array(range(1,10,1))
max_features = np.concatenate((max_features,np.array([None,"auto","sqrt","log2"])))
max_depth=np.array([None])
min_samples_split = np.array(range(2,10,1))
min_samples_leaf = np.array(range(1,10))
min_weight_fraction_leaf  = np.array([0.1,0.2,0.3,0.4,0.5])
param_grid = [{"max_features":max_features, "criterion":criterion,"n_estimators":n_estimators,
               "max_depth":max_depth,"min_samples_split":min_samples_split,"min_samples_leaf":min_samples_leaf,"min_weight_fraction_leaf":min_weight_fraction_leaf}]
"""

VX = []
VY = []
c=0
"""n_estimators= 34 max_depth= 35 acc= 0.90596645587
n_estimators= 53 max_depth= 56 acc= 0.907616167171"""
while c<len(X):


    if c%10 ==0:
        VX.append(X[c])
        del X[c]
        VY.append(Y[c])
        del Y[c]
    c += 1
best_accuracy=0
best_clf = None
for n in range(10,100):
    for d in range(3,100):
        clf = ExtraTreesClassifier(n_estimators=n, max_depth=d, min_samples_split=2,
                                   class_weight="balanced_subsample")
        clf.fit(X,Y)
        cv_accuracy = clf.score(VX,VY)
        if cv_accuracy>best_accuracy:
            best_accuracy = cv_accuracy
            print("n_estimators=", n, "max_depth=",d,"acc=", cv_accuracy)

"""clf = ExtraTreesClassifier(n_estimators=17, max_depth=27, min_samples_split=2,
                                   class_weight="balanced_subsample")
clf.fit(X,Y)
text_file = open("Output.txt", "w")
for u in range( len(UX)):
    ur = np.array(UX[u]).reshape(1, -1)
    r=clf.predict(ur)
    if r == 0:
        text_file.write("0\n")
    if r == 1:
        text_file.write("1\n")
    if r == 2:
        text_file.write("2\n")

text_file.close()
#clf = ExtraTreesClassifier(n_estimators=10, max_depth=200, min_samples_split=2,class_weight="balanced_subsample")

"""
#knn=neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights="distance", algorithm="auto", leaf_size=60, p=p, metric="minkowski", metric_params=None)
