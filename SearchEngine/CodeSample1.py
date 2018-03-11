page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

start_link = page.find('<a href=')

print (start_link)

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=')
req_link = page[start_link:]
start_pos = req_link.find('"')
start_pos+=1
stop_pos = req_link.find('"', start_pos+1)
url = req_link[start_pos:stop_pos]

print (url)
