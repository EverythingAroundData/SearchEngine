# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

def sublists(nlist):
    cntr = 0
    i = 0
    alist = []
    slist = []
    listlen =len(nlist)
    while i<listlen:
        if i == 0:
            alist.append(nlist[i])
        else:
            if nlist[i]>nlist[i-1]:
                if len(slist)>0:
                    alist.append(slist)
                    slist = []
                if len(slist)==0:
                    alist.append(nlist[i])
            else:
                slist.append(nlist[i])
                cntr = 1
        i=i+1
    if cntr ==1:
        alist.append(slist)
    return alist


blist = [5, 4, 3, 9, 8, 7]
print (sublists(blist))
#result = [5,[4,3],9,[8,7]]

blist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print (sublists(blist))

blist = [4,5,5,5,3,2,1,2,3,2,6,6]
print (sublists(blist))


blist = [1,2,3,4,5,6,7,8,9]
print (sublists(blist))