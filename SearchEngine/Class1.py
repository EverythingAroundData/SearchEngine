class web:
    def add_to_index(index, keyword, url):
        for kword in index:
            if kword[0]==keyword:
                kword[1].append(url)
                return index
        index.append([keyword, [url]])
        return index
        
    def lookup(index, keyword):
        for entry in index:
            if entry[0]==keyword:
                return entry[1]
        return []
        
    def add_page_to_index(index, url, content):
        pcontent = content.split()
        for word in pcontent:
            if lookup(index, word) == []:
                add_to_index(index, word, url)
        return index