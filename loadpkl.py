# -*- coding:UTF-8 -*-

import numpy as np
import cPickle as pickle
def load_data():
#    X_train_1 =[]
#    y_train_1 = []
    f = open('iperf_test.pkl','rb')

    X_test = pickle.load(f)
#    print X_test
#print info   #show file
    y_test = pickle.load(f)
#    print y_test
    f.close()
#print '\n'

#print len(X)
    f = open('iperf_train.pkl','rb')

    X_train = pickle.load(f)
#    print X_train
#print info
# #show file
    y_train = pickle.load(f)
#    print y_train
    f.close()
    return (X_train, y_train), (X_test, y_test)
'''
    for i in X_train:
        for j in i :
            X_train_1.append(j)

    for i in y_train:
        for j in i :
            y_train_1.append(j)

    return (X_train_1,y_train_1) ,(X_test, y_test)
'''
'''
(b,d),(c,e) =load_data()


b = np.array(b)
d = np.array(d)
#c = np.array(c)
#e = np.array(e)
#b = b.reshape(7645,6,5)
#d = d.reshape(7645,6,1)
print b
print b.shape
print d
print d.shape
#print c
#print c.shape
#print e
#print e.shape
'''

