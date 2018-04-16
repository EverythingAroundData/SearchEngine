# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(univ_info):
    sofstudents = []
    tfees = []
    flist = []
    for olist in univ_info:
        sofstudents.append(olist[1])
        tfees.append(olist[1]*olist[2])
    flist.append(sum(sofstudents))
    flist.append(sum(tfees))
    return flist

print (total_enrollment(usa_univs))
print (total_enrollment(udacious_univs))

## Lesson 11, 2nd last program, and Lesson 12, 6th and 7th program are on hold

#sudoku
# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

s1 = [[1,2,3],
      [2,3,1],
      [3,1,2]]

def check_sudoku(s):
    a = 0
    b = 0
    c = 0
    x = 0
    y = 0
    k = 0
    listlen = []
    newlist = []
    for i in s:
        a = a + 1
        listlen.append(len(i))
    for p in listlen:
        if a!=p:
            return
    while b < a:
        if b+1 not in list(range(a+1)[1::1]):
            return 
        b = b + 1
    for e in s:
        for f in e:
            if f in list(map(chr, range(97,123))) or f in list(map(chr, range(65,91))) or f != int(f):
                return False
    c = sum(s[1])
    while x < a:
        while y < a:
            k = k + s[y][x]
            if y == a - 1:
                newlist.append(k)
            y = y + 1
        k = 0
        y = 0
        x = x + 1
    for m in newlist:
        if m != c:
            return False
    return True

s2 = [[1,2,3,4],
      [2,3,1,3],
      [3,1,2,3],
      [4,4,4,4]]

s3 = [[1,2,3,4],
      [2,3,1,4],
      [4,1,2,3],
      [3,4,1,2]]

s4 = [[1,2,3,4,5],
      [2,3,1,5,6],
      [4,5,2,1,3],
      [3,4,5,2,1],
      [5,6,4,3,2]]

s5 = [['a','b','c'],
      ['b','c','a'],
      ['c','a','b']]

s6 = [[1, 1.5],
      [1.5, 1]]


print (check_sudoku(s1)) 
print (check_sudoku(s2)) 
print (check_sudoku(s3)) 
print (check_sudoku(s4)) 
print (check_sudoku(s5)) 
print (check_sudoku(s6)) 


# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def isListSymmetric(alist):
    i = 0
    j = 0
    for e in alist:
        if len(e) != len(alist):
            return 'Uneven no. of nested list members'
    while i<len(alist):
        while j<len(alist):
            if alist[i][j] != alist[j][i]:
                return False
            j=j+1
        j=0
        i=i+1
    return True
      
list1 = [['Cat', 'Dog', 'Cow'], 
         ['Dog', 'Lion', 'Tiger'], 
         ['Cow', 'Tiger', 'Parrot']]

      
list2 = [['Cat', 'Dog', 'Cow'], 
         ['Crow', 'Lion', 'Tiger'], 
         ['Cow', 'Tiger', 'Parrot']]

      
list3 = [['Cat', 'Dog', 'Cow'], 
         ['Dog', 'Lion', 'Tiger'], 
         ['Cow', 'Tiger', 'Parrot', 'Pegion']]


print (isListSymmetric(list1))
print (isListSymmetric(list2))
print (isListSymmetric(list3))



# Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def isSquareAntiSymmetric(alist):
    i = 0
    j = 0
    for e in alist:
        if len(e) != len(alist):
            return 'Not a square'
    while i<len(alist):
        while j<len(alist):
            if alist[i][j] != -alist[j][i]:
                return False
            if i==j and alist[i][j] != 0:
                return False
            j=j+1
        j=0
        i=i+1
    return True

print (isSquareAntiSymmetric([[0, 1, -2], 
                              [-1, 0, 3], 
                              [2, -3, 0]]))   


print (isSquareAntiSymmetric([[0, 0, 0],
                              [0, 0, 0],
                              [0, 0, 0]]))


print (isSquareAntiSymmetric([[0, 1, 2], 
                              [-1, 0, -2], 
                              [2, 2,  3]]))


print (isSquareAntiSymmetric([[1, 2, 5],
                              [0, 1, -9],
                              [0, 0, 1]]))

#Identity Matrix

