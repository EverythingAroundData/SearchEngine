## Better Split ##
def bettersplit(source,splitlist):
    j=0
    i=0
    k=0
    str = []
    splist = []
    for p in splitlist:
         splist.append(p)
    if source[len(source)-1] not in splist:
        source = source+splitlist[0] 
    while j<len(source):
        while i<len(splitlist):
            if source[j] == splitlist[i]:               
                str.append(source[:j])
                source = source[j+1:]
                j=-1 
                break                               
            i=i+1
        i=0
        j=j+1
    if '' in str:
        while k < len(str):
            str.remove('')
            k=k+1  
    return (str)

source = "This is a test-of the,string separation-code!"
splitlist = " ,!-"

print (bettersplit(source,splitlist))

source = "After  the flood   ...  all the colors came out."
splitlist = " ."

print (bettersplit(source,splitlist))

source = "First Name,Last Name,Street Address,City,State,Zip Code"
splitlist =","

print (bettersplit(source,splitlist))