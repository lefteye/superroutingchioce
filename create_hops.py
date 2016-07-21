# -*- coding:UTF-8 -*-
# 用于产生跳数
import random
import csv

f = open('tiaoshu133.csv','ab')
c = csv.writer(f)
x=[]
for i in range(69991):
    r = random.choice([3])
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
