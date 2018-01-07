import keras
from keras import Sequential
from keras.layers import Dense
from keras import losses
from dsparse import parse,parse_classes
import numpy as np
class_0, class_1, class_2, undefined, validation,vdates,c0dates,c1dates,c2dates,udates = parse_classes()
X, Y, UX, VX, VY = parse(class_0, class_1, class_2, undefined, validation)
NY = Y
Y=[]
for y in NY:
    if y==b'0':
        Y.append([1,0,0])
    if y==b'1':
        Y.append([0,1,0])
    if y==b'2':
        Y.append([0,0,1])

act = 'sigmoid'
num_classes = 3
model = Sequential()
model.add(Dense(2200, input_dim=3, activation=act))
model.add(Dense(1900, activation=act))
model.add(Dense(2000, activation=act))
model.add(Dense(1000, activation=act))
model.add(Dense(1600, activation=act))
model.add(Dense(1400, activation=act))
model.add(Dense(3, activation=act))
model.compile(loss='binary_crossentropy', optimizer="Adam", metrics=['binary_accuracy'])
model.fit(X, Y, epochs=20, batch_size=10)
scores = model.evaluate(VX, VY)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))