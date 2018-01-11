from dsparse import  parse_classes
from sklearn.ensemble import ExtraTreesClassifier

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
best_accuracy=0
best_clf = None
for n in range(10,100):
    for d in range(3,100):
        for r in range(1,100):
            clf = ExtraTreesClassifier(n_estimators=n, max_depth=d, min_samples_split=2,
                                   class_weight="balanced_subsample",random_state=r)
            clf.fit(X,Y)
            cv_accuracy = clf.score(VX,VY)
            if cv_accuracy>best_accuracy:
                best_accuracy = cv_accuracy
                print("n_estimators=", n, "max_depth=",d, "rs=",r,"acc=", cv_accuracy)


