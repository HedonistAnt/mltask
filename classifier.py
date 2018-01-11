import numpy as np
from dsparse import parse_classes
from sklearn.ensemble import ExtraTreesClassifier

X, Y, UX = parse_classes()
clf = ExtraTreesClassifier(n_estimators=16, max_depth=33, random_state=35, min_samples_split=2,
                           class_weight="balanced_subsample")
clf.fit(X, Y)
text_file = open("Output.txt", "w")
for u in range(len(UX)):
    ur = np.array(UX[u]).reshape(1, -1)
    r = clf.predict(ur)
    if r == 0:
        text_file.write("0\n")
    if r == 1:
        text_file.write("1\n")
    if r == 2:
        text_file.write("2\n")

text_file.close()
