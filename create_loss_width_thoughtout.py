# -*- coding:UTF-8 -*-
#用于产生吞吐量、可用带宽、抖动、丢包率

import csv

f = open('iperf_13.csv')
c = f.readlines()
csvfile1 = open('iperf_133.csv', 'ab')
writer1 = csv.writer(csvfile1)


for i in c:
#    try:
        t = i.split()
#        print t
#      print len(t)
        ll = []
        if len(t)==14:

            a= t[5]
#            print type(a)
            e=float(a)
      #      print type(a)
    #        print a
            if e > 10:
#                print "helloworld"
                h = e * 0.001
                k = str(h)
                ll.append(k)
            else:
                a = t[5]
                ll.append(a)
            b = t[7]
            c = t[-5]
            d = t[-1]


            ll.append(b)
            ll.append(c)

            if len(d) == 6:
                t = d[1:4]
                ll.append(t)
#        writer1.writerow(d)
        #            print d
            else:
                t = d[1]
                ll.append(t)
#        writer1.writerow(d)

#ll.append(d)
        elif len(t) == 13:
            a = t[4]
            b = t[6]
            c = t[-5]
            d = t[-1]
            e = float(a)
            #      print type(a)
            #        print a
            if e > 10:
#                print "helloworld"
                h = e * 0.001
                k = str(h)
                ll.append(k)
            else:
                a = t[4]
                ll.append(a)

            ll.append(b)
            ll.append(c)

            if len(d) == 6:
                t = d[1:4]
                ll.append(t)
                writer1.writerow(ll)
        #            print d
            else:
                t = d[1]
                ll.append(t)
                writer1.writerow(ll)
        else:
            continue
#print ll

print "all complted"
csvfile1.close()
