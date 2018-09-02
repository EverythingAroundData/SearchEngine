import urllib.request as r
from Class1 import web as w
from Class1 import weburls as u

#MyFInstance = w()

#print (MyFInstance.add_to_index([], 'linkedin', 'http://linkedin.com/'))

MyInst = u()
url = 'http://twitter.com'

pcontent = str(r.urlopen(url).read())

print (MyInst.get_all_links(pcontent))