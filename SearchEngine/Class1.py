class web:
    def add_to_index(self, index, keyword, url):
        for kword in index:
            if kword[0]==keyword:
                kword[1].append(url)
                return index
        index.append([keyword, [url]])
        return index
        
    def lookup(self, index, keyword):
        for entry in index:
            if entry[0]==keyword:
                return entry[1]
        return []
        
    def add_page_to_index(self, index, url, content):
        pcontent = content.split()
        for word in pcontent:
            if lookup(index, word) == []:
                add_to_index(index, word, url)
        return index


class weburls():
    def get_next_target(self, page):
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
    
    
    def get_all_links(self, page):
        urllist = []
        while True:
            url, pcontent = self.get_next_target(page)
            if url:
                urllist.append(url)            
                page = pcontent
            else:
                return urllist

# Web crawler function and related functions to be added