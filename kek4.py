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

best_accuracy = 0
for m in range(2,100):

        clf = ExtraTreesClassifier(n_estimators=31, max_depth=95, min_samples_split=2,
                                   class_weight="balanced_subsample",criterion="gini")
        clf.fit(X,Y)
        cv_accuracy = clf.score(VX,VY)
        if cv_accuracy>best_accuracy:
            best_accuracy = cv_accuracy
            print( "ml=",m,best_accuracy)