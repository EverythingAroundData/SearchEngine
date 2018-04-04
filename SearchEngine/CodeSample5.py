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

#extract all the urls from a page

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">'
'<div class="udacity float-left"><a href="http://twitter.com">'
'<This is random text><a href="http://google.com"><div class="udacity float-left">'
'<div class="udacity float-left"><a href="http://linkedin.com"><This is random text>'
'<div class="udacity float-left"><a href="http://www.youtube.com"><Extract urls from this page content>'
'<This is random text><a href="http://facebook.com"><This is random text>'
)

def get_next_target(page):
    linkf = page.find('<a href=')
    if linkf ==-1:
        return '', ''
    upagecontent = page[linkf+1:]
    links = upagecontent.find('"')
    mpagecontent = upagecontent[links+1:]
    linke = mpagecontent.find('"')
    url = mpagecontent[:linke]
    fpagecontent = mpagecontent[linke:]
    return url, fpagecontent


def get_all_links(page):
    urllist = []
    while True:
        url, pcontent = get_next_target(page)
        if url:
            urllist.append(url)            
            page = pcontent
        else:
            return urllist

print (get_all_links(page))

samplecontent = ('SSIS 2012 Projects: Setup, Project Creation and Deployment'
                'It used to be that SQL Server Integration Services (SSIS) packages' 
                'had to be deployed individually. Now, they can be all deployed '
                'together from a single file by means of the Project Deployment '
                'Model introduced in SSIS 2012. Where there are tens or even hundreds '
                'of SSIS packages to deploy, this system is essential. Url for content above is'
                '<a href="https://www.red-gate.com/simple-talk/sql/ssis/ssis-2012-projects-setup-project-creation-and-deployment/">'
                'All the python code is on <a href="https://github.com/EverythingAroundData/SearchEngine/tree/master/SearchEngine">')

print (get_all_links(samplecontent))