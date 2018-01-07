from dsparse import  parse_classes,parse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier ,RadiusNeighborsClassifier, RadiusNeighborsRegressor,NearestCentroid
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates = parse_classes()
X, Y, UX, VX, VY,traindates,vdates,udates = parse (class_0, class_1, class_2, undefined , validation,vdates,c0dates,c1dates,c2dates,udates)



# Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process", "RBF SVM" "Decision Tree", "Random Forest", "Neural Net", "AdaBoost","Naive Bayes", "QDA"
names = [ "RadiusNeighborsClassifier", "NearestCentroid", "Nearest Neighbors"]

classifiers = [

    RadiusNeighborsClassifier(radius=5.0, weights="distance", algorithm="brute", leaf_size=30, p=1, metric="minkowski", metric_params=None),
    NearestCentroid(metric="minkowski"),
    #RadiusNeighborsRegressor(radius=1.0, weights="distance", algorithm="brute", leaf_size=30, p=2, metric="minkowski", metric_params=None),
    KNeighborsClassifier(n_neighbors=1,algorithm="brute",p=5, metric="minkowski",weights='distance')]


for name, clf in zip(names, classifiers):
        clf.fit(X,Y)
        acc=0
        for v in range(len(VX)):
            vr = np.array(VX[v]).reshape(1, -1)
            r = clf.predict(vr)
            if r == VY[v]:
                acc += 1
        print(name,acc/len(VY))



