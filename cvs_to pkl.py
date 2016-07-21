# -*- coding:UTF-8 -*-
import pickle
import numpy as np

f =open('iperf_7777tag.csv')
lines =f.readlines()
ll = []
labels =[]
#n =0
for i in lines:
    try:
        tt=i.strip('\n\r').split(',')
        m = tt[0:-1]
#        print m
        tag = i[-2:-1]
#        print  tag
        labels.append(tag)
#        print type(m)
#        print labels
#        m = m.split(",")
#        print m
#        print type(m)
        list_a = map(eval, m)
        labelss = map(eval,labels)
#        n = n+1
#        print list_a
#        print '\n'
#        print labelss
        for x in list_a:
            ll.append(x)

#       print m
#        print ll
#        print len(ll)
    except :
        continue

f.close()
#print ll
X = np.array(ll)
#X = X.reshape(rows,30)
#print '\n'
#print labelss
label = np.array(labelss)
#label =label.reshape(rows,6)

#print "yizhixing"
output = open('iperf_xxxxxxxx.pkl', 'wb')

# Pickle dictionary using protocol 0.

pickle.dump(X, output)

# Pickle the list using the highest protocol available.

pickle.dump(label, output)

output.close()

#print "all lines=" ,n

#进行reshape
