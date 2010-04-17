#!/usr/bin/python
#
# NatureSpider.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details

from NatureIndexParser import NatureIndexParser
import urllib

class NatureSpider:

    def __init__(self):
        self.idxparser = NatureIndexParser()

    def readIndex(self, resourceName):
        "Reads a resource to parse by index parser. This should be a "
        "filename or url. urls are assumed to start with 'http'"
        if(resourceName[:4] == 'http'):
            f = urllib.urlopen(resourceName)
        else:
            f = open(resourceName)
        self.idxparser.parse(f.read())

if __name__ == '__main__':
    n = NatureSpider()
    n.readIndex('http://www.nature.com/nbt/archive/index.html')
    print n.idxparser.links
