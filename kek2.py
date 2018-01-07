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
trees = ExtraTreesClassifier()

param_grid = [{"max_depth":np.array(range(3,40)),"class_weight": np.array(["balanced","balanced_subsample"]),"n_estimators": np.array(range(10,50))}]
n_jobs = 4
refit = False
clf = GridSearchCV(estimator=trees,param_grid=param_grid,n_jobs=n_jobs,refit=refit,verbose=10,scoring=trees.fit(X,Y).score(VX,VY)).fit(X,Y)
print(clf.best_params_)