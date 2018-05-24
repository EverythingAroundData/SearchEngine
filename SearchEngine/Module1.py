# list all the methods of a class from module/s

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

#print (oslist)

# 1. os.name

print (os.name)

# 2. os.getcwd

print ('Current working Directory ' + os.getcwd())
print ('Absolute Path ' + os.path.abspath('/'))
dirlist = os.listdir('..')
print ('list files and folders in cwd ' + str(dirlist))

# 3. os.rename and change directory
abspath = os.path.abspath('/') # returns E:\
os.chdir(abspath)

print (os.getcwd())

#os.rename('New.txt', 'Rename.txt')

# 4. os.mkdir
os.mkdir('newdir')

# 5. os.rmdir
os.rmdir('newdir')
os.rename('New.txt', 'Rename.txt')
