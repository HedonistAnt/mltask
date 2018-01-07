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
clf = ExtraTreesClassifier(n_estimators=10, max_depth=128, min_samples_split=2,class_weight="balanced_subsample")

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
clf.fit(X,Y)
print(clf.score(VX,VY))