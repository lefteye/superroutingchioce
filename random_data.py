# -*- coding:UTF-8 -*-
#进行打标签之前将数据进行随机排序在此之前需要将前面产生的数据整理到一个文档中

import random
import csv

f =open('iperf_7777tag.csv')
csvfile1 = open('iperf_7777.csv', 'ab')
c= f.readlines()
f.close()
writer1 = csv.writer(csvfile1)
ll = []
for i in c:
    try:

        m = i.strip('\n').split(',')
#        print m
#        print type(m)
        ll.append(m)


    except:
        continue


#print ll
random.shuffle(ll)
random.shuffle(ll)
random.shuffle(ll)
random.shuffle(ll)

for x in ll:
    writer1.writerow(x)

csvfile1.close()
