################################## Unit 2 ###########################################
#Lesson 5
#recursion
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">'
'<div class="udacity float-left"><a href="http://twitter.com">'
'<This is random text><a href="http://google.com"><div class="udacity float-left">'
'<div class="udacity float-left"><a href="http://linkedin.com"><This is random text>'
'<div class="udacity float-left"><a href="http://www.youtube.com"><Extract urls from this page content>'
'<This is random text><a href="http://facebook.com"><This is random text>'
)

def get_next_link(page_content):
    start_link = page_content.find('<a href=')
    req_link = page_content[start_link:]
    start_pos = req_link.find('"')
    start_pos=start_pos+1
    stop_pos = req_link.find('"', start_pos+1)
    url = req_link[start_pos:stop_pos]
    print (url)
    startpos = req_link.find('>')
    pagecontent = req_link[startpos+1:]
    if len(pagecontent)<=0:
        return
    get_next_link(pagecontent)

get_next_link(page)
