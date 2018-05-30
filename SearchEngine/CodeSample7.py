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
    vcomp = nlist[0]
    cntr = 0
    i = 0
    alist = []
    slist = []
    listlen =len(nlist)
    while i<listlen:
        if i == 0:
            alist.append(nlist[i])
        else:
            if nlist[i] > vcomp:
                if len(slist)>0:
                    alist.append(slist)
                    slist = []
                if len(slist)==0:
                    alist.append(nlist[i])
                vcomp = nlist[i]
            else:
                slist.append(nlist[i])
                cntr = 1
        i=i+1
    if cntr ==1:
        if len(slist)>0:
            alist.append(slist)
    return alist


blist = [5, 4, 3, 9, 8, 7]
print (sublists(blist))
#result = [5,[4,3],9,[8,7]]

blist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print (sublists(blist))
#result = [9, [8, 7, 6, 5, 4, 3, 2, 1]]

blist = [4,5,5,5,3,2,1,2,3,2,6,6]
print (sublists(blist))
#result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]

blist = [1,2,3,4,5,6,7,8,9]
print (sublists(blist))
#result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

blist = [6,5,4,5,3,6,7,8,9,5,7,10]
print (sublists(blist))
#result = [6, [5, 4, 5, 3, 6], 7, 8, 9, [5, 7], 10]


# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.


def freq_analysis(string):
    adict = {}
    alist = []
    j = 0
    for i in range(97,123):
        adict[chr(i)] = 0.0
    while j < len(string):
        adict[string[j]] = adict[string[j]] + 0.25
        j = j+1
    for c in sorted(adict):
        alist.append(adict[c])
    print (alist) 

freq_analysis('zabcdxd')
freq_analysis('spark')
freq_analysis('hadoop')
freq_analysis('bewarethebunnies')
freq_analysis('bigdatabrews')
freq_analysis('abcd')


# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

def add_to_index(index, keyword, url):
    newindex = []
    newurl = []
    collectkeywords = []
    i = 0
    j = 0
    if len(index)==0:
        newindex.append(keyword)
        newurl.append(url)
        newindex.append(newurl)
        index.append(newindex)
    else:
        while i < len(index):
            collectkeywords.append(index[i][0])
            i = i + 1
        if keyword not in collectkeywords:
            newindex.append(keyword)
            newurl.append(url)
            newindex.append(newurl)
            index.append(newindex)
        else:
            j = collectkeywords.index(keyword)
            if url not in index[j][1]:
                index[j][1].append(url)
    return index

index = []

print (add_to_index(index, 'udaity', 'www.udacity.com')) 
print (add_to_index(index, 'udaity', 'www.facebook.com')) 
print (add_to_index(index, 'udaity', 'www.linkedin.com')) 
print (add_to_index(index, 'data bricks', 'www.twitter.com'))
print (add_to_index(index, 'wierd tiger', 'www.linkedin.com'))  
print (add_to_index(index, 'wierd tiger', 'www.facebook.com')) 
