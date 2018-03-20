################################## Unit 3 ###########################################
#Lesson 6
#1. Median
import math as m
from CodeSample2 import MyFirst as mf

def median(a):
    a.sort()
    listlen = len(a)
    idx = int(listlen/2)
    if listlen % 2 == 1:
        return (a[m.floor(idx)])
    else:        
        c = (a[idx]+a[idx-1])/2
        return (c)

a = [7, 8, 6, 5, 16]
print (median(a))

b = [5, 7, 12, 8]
print (median(b))

#2. find last

instance = mf()

def find_last(s, t):
    l = len(t)
    lst = []
    for i in range(len(s))[::1]:
        if t == s[i:i+l]:
            lst.append(i)
    p = instance.maxno(lst)
    return (p)        
                  
print (find_last('acdg dd ac', 'ac'))