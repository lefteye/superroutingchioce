# -*- coding:UTF-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import model_from_json
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np
import loadpkl

(X_train, y_train),(X_test, y_test) = loadpkl.load_data()
X_test = np.array(X_test)
y_test = np.array(y_test)
t1=X_test.shape[0]/36
#print t1
X_test = X_test.reshape(t1,6,6)#测试集行数 、
y_test = y_test.reshape(t1,6)

model = model_from_json(open('my_model_architecture.json').read())
model.load_weights('my_model_weights.h5')
model.compile(optimizer = 'rmsprop', loss = 'mse', metrics=['accuracy'])

#model.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics=['accuracy'])
#prob = model.evaluate(X_test,y_test,batch_size=32)
#print prob
#prob2 = model.predict(X_test)
#print prob2

#y_proba = model.predict_proba(X_test,batch_size=32)
y_predict = model.predict_classes(X_test,batch_size=64)
#print 'y_proba:' ,y_proba
print 'y_predict:',y_predict
#n=0
##  print i
#print n

