#Lesson 1

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

#Lesson 2

#1 - rounding off
x = 3.14159
print (str(x+0.5)[:str(x+0.5).find('.')])

#2
s = 'udacity'
t = 'bodacious'

print (s[:3]+t[4:])

#3
text = 'Hello Helloo Helllooo Halo'

print (text.find('hoo'))

#4
text = 'zip files are zipped'
print (text.find('zip', text.find('zip')+1))

text = 'zip files are compressed'
print (text.find('zip', text.find('zip')+1))


#Lesson 3

#1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

replaced = line[:line.find(marker)]+replacement+line[line.find(marker)+len(marker):]
print (replaced)