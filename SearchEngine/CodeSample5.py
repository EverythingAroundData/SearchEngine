################### Miscellanious #########################

# Name  Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]
print (countries[1][1])

# Find no. of U in list 
def measure_udacity(alist):
    a=0
    for i in alist:
        for p in i:
            if p=='U':
                a=a+1
    return a

samplelist = ['Dave', 'Udacity', 'U2', 'AU', 'James', 'Au']

print (measure_udacity(samplelist))

# find index of search string in list

def find_element(alist, fstring):
    for i in alist:
        if i==fstring:
            return alist.index(fstring)
    return -1

fstr = 'AU2'
    
print (find_element(samplelist, fstr))
