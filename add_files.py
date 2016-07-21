# -*- coding:UTF-8 -*-
# 文件叠加


import csv
#import re
f =open('iperf_10000_00.csv','ab')
writer1 = csv.writer(f)

f2 = open('iperf_133.csv', 'a+')
c =f2.readlines()
for i in c:

    t = i.strip('\n').split(',')
#    print t
    writer1.writerow(t)
#    print t

    '''
    try:
        t=i.split()
        d=t[0:2]
        print d
        t=t[2]
        if len(t)==6:
            t=t[1:4]
            d.append(t)
            print d
            writer1.writerow(d)
#            print d
        else:
            t=t[1]
            d.append(t)
            writer1.writerow(d)
#            print d
    except Exception:
        continue


#        x =t[2]
#        print x[1:5]
#        writer1.writerow(t)


'''
print "all complted"

f.close()
f2.close()
