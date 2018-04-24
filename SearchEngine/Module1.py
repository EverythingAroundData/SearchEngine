# list all the methods of a class from module

from CodeSample2 import MyFirst as c
newlist = dir(c)

newlist.sort()
print (newlist)

elist = []

#remove built in methods

for e in newlist:
    if e[:2] != '__' and e[-1:-2] != '__':
        elist.append(e)

print ('\n')
print (elist)

# list os methods

import os 
oslist = dir(os)
oslist.sort()

print (oslist)