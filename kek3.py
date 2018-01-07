import numpy as np
from dsparse import  parse_classes
from sklearn import neighbors, datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import cross_val_score,cross_val_predict
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import GridSearchCV

X,Y,UX= parse_classes()
trees = ExtraTreesClassifier()
cross_val_score(trees,X)