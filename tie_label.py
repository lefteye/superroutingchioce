# -*- coding:UTF-8 -*-
# 用于给数据进行打标签
import csv
import random

def compare(r1,r2):
    if abs(r1[0]-r2[0]) <= 3:    #cmp_avg_packetloss
        if abs(r1[1] - r2[1]) <=4.5: #mp_avg_delay
            if abs(r1[2]-r2[2]) <=2: # cmp_hop_counts
                if abs(r1[3]-r2[3]) <=0.25: #cmp_avg_thoughput
                    if abs(r1[4]-r2[4]) <= 2.2: #cmp_avg_bandwidth
                        if abs(r1[5] - r2[5]) <= 2.2 :  #cmp_avg_jetter
                            if cmp(r1[0],r2[0]) == 0 :
                                if cmp(r1[1],r2[1])== 0:
                                    if cmp(r1[2],r2[2])==0:
                                        if cmp(r1[3],r2[3])==0:
                                            if cmp(r1[4],r2[4])==0:
                                                if cmp(r1[5],r2[5])<=0:
                                                    return r1
                                                else:
                                                    return r2
                                            elif cmp(r1[4],r2[4])<0:
                                                return r2
                                            else:
                                                return r1
                                        elif cmp(r1[3],r2[3])<0:
                                            return r2
                                        else:
                                            return r1
                                    elif cmp(r1[2],r2[2])<0:
                                        return r1
                                    else:
                                        return r2
                                elif cmp(r1[1],r2[1]) <0:
                                    return r1
                                else:
                                    return r2
                            elif cmp(r1[0],r2[0]) <0:
                                return r1
                            else:
                                return r2
                        elif cmp(r1[5], r2[5]) < 0:
                            return r1
                        elif cmp(r1[5], r2[5]) > 0:
                            return r2

                    elif cmp(r1[4], r2[4]) <0:
                        return r2
                    else:
                        return r1

                elif cmp(r1[3], r2[3]) < 0:
                    return r2
                else:
                    return r1

            elif cmp(r1[2], r2[2])<0:
                return r1
            else:
                return r2

        elif cmp(r1[1], r2[1]) <0:
            return r1
        else:
            return r2

    elif cmp(r1[0], r2[0]) < 0:
#        print 'hello'
        return r1
    else:
        return r2

'''
def reduce1(function, iterable1):

    it = iterable1[0]
    accum_value = it
 #   print accum_value
    for x in iterable1[1:]:
#        print x
        accum_value = function(accum_value, x)
#    return accum_value
'''
def f_int(l):
    u=[]
    for i in l:
#        print type(z)
        t=float(i)
        u.append(t)
    return u




#    return 'hello'

f = open('iperf_83999s.csv')
c = f.readlines()

csvfile1 = open('iperf_83999.csv', 'ab')
writer1 = csv.writer(csvfile1)

ttt = []
n = 0
for i in c:
    t = i.strip('\n').split(',')
#    print t
#    n=n+1
    p = f_int(t)
#    print n
#    print p
    ttt.append(p)
    n = n+1
    if n%50 == 0:
#        print ttt
        ee = []
        rr = []
        ll =[]
        ppp = sorted(ttt)
#        print ppp
        for i in range(50):
            if ppp[i][0] <= (ppp[0][0]+3):
                ee.append(ppp[i])
            else:
                rr.append(ppp[i])
#        print ee
#        print rr
        mm = reduce(compare, ee)
#        print type(mm)
        mm[-1] = 1
#        print ttt
#        print mm
        for i in ee:
            ll.append(i)
        for i in rr:
            ll.append(i)

        random.shuffle(ll)
        for x in ll:
            rowValue1 = x
            writer1.writerow(rowValue1)
        ttt = []
        continue

    else:
        continue


print 'allcomplted'

csvfile1.close()
