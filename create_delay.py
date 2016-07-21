# -*- coding:UTF-8 -*-
# 用于产生往返时延

import csv

f =open('ping_13.csv')
f1 = open('ping_133.csv','ab')
c = f.readlines()
writer1 = csv.writer(f1)

f.close()
x = []
for i in c:
    print len(i)
    try:
        if 56<= len(i)<= 68:
            t = i.split('=')
            t = t[-1]
            t = t[:-4]
#        print type(t)
            #print t
            x.append(t)
#        print x
#        writer1.writerow(x)
    except Exception :
        continue
#print x
for i in x:
    t=i.split()
#    print t
    writer1.writerow(t)

f1.close()
print "all complted"