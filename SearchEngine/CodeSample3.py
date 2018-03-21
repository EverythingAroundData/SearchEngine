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
    if s.find(t) == -1:
        return 'string not found'
    else:
        for i in range(len(s))[::1]:
            if t == s[i:i+l]:
                lst.append(i)
        p = instance.maxno(lst)
        return (p)        
                  
print (find_last('acdg dd ac', 'z'))

#3. divide the amount in multiple of 5, 2 and 1

def stamp(amt):
    f = m.floor(amt/5)
    five = amt%5
    if five>=2:
        t = m.floor(five/2)
        if five%2 == 0:
            one = 0
        if five%2 == 1:
            one = 1
    else:
        if five==0:
            one = 0
        if five == 1:
            one = 1
        t = 0
    return '('+str(f)+'p, '+str(t)+'p, '+str(one)+'p)'

print (stamp(74))

#4. range of values in list

def lrange(alist):
    alist.sort()
    l = len(alist)
    return (alist[l-1] - alist[0])

print (lrange([44,6,1,91]))