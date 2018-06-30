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

# Below is the same procedure as above add_to_index (shorter code :) ) 
# handle the condition if url already exists
def add_to_index_new(index, keyword, url):
    for kword in index:
        if kword[0]==keyword:
            kword[1].append(url)
            return index
    index.append([keyword, [url]])
    return index
index = []
print (add_to_index_new(index, 'udacity', 'www.udacity.com')) 
print (add_to_index_new(index, 'udacity', 'www.facebook.com')) 
print (add_to_index_new(index, 'udacity', 'www.linkedin.com')) 
print (add_to_index_new(index, 'data bricks', 'www.twitter.com'))
print (add_to_index_new(index, 'wierd tiger', 'www.linkedin.com'))  
print (add_to_index_new(index, 'wierd tiger', 'www.facebook.com')) 

# Lookup function returns list of urls associated with a keyword

def lookup(index, keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return []

print (lookup(index, 'udacity')) 

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

def add_page_to_index(index, url, content):
    pcontent = content.split()
    for word in pcontent:
        if lookup(index, word) == []:
            add_to_index_new(index, word, url)
    return index

print (add_page_to_index(index,'fake.text',"This is a test"))

print (add_page_to_index(index,'www.udacity.com',"Portal for learning new stuff"))


# Web crawler function to be added