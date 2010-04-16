#!/usr/bin/env python

# for i in range (1,500):
# 	url = 'http://dx.doi.org/10.1038/nbt.' + str(i)	
# 	c.append( (url, urllib2.urlopen(url).read()) )	#store tuples of url / contents
# 	time.sleep(3)

import sgmllib, re

class NatureIndexParser(sgmllib.SGMLParser):

    def __init__(self, verbose=0):
        sgmllib.SGMLParser.__init__(self,verbose)
        self.links = []

    def start_a(self,attrs):
        for prop, value in attrs:
            if prop == "href" and re.search("^/nbt/journal/v[0-9]", value) != None:
                self.links.append(value)

    def parse(self, input):
        self.feed(input)
        self.close()

if __name__ == '__main__':
    f = open ('../index.html','r')
    n = NatureIndexParser(1)
    n.parse(f.read())
    print n.links
    print len(n.links)
    f.close()
