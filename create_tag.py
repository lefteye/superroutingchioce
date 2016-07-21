# -*- coding:UTF-8 -*-
# 用于产生tag-0
import random
import csv

f = open('tag83999.csv','ab')
c = csv.writer(f)
x=[]
for i in range(609929):
    r = random.choice([0])
    x.append(r)
#    print r
#    c.writerow(r)
#print x
y =[]
for i in x:
    t = str(i)
    y.append(t)
#print y
d =[]
for i in y:
    t = i.split()
#    print t
    c.writerow(t)
f.close()

print "all complted"
