#!/usr/bin/python
#
# NatureSpider.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details

from NatureIndexParser import NatureIndexParser
from NatureIssueParser import NatureIssueParser
import urllib

class NatureSpider:

    def __init__(self):
        self.idxparser = NatureIndexParser()
        self.issues = []

    def readIndex(self, resourceName):
        "Reads a resource to parse for links to issues. This should be a "
        "filename or url. urls are assumed to start with 'http'"
        if(resourceName[:4] == 'http'):
            f = urllib.urlopen(resourceName)
        else:
            f = open(resourceName)
        self.idxparser.parse(f.read())

    def readIssue(self, resourceName):
        "Read a resource to fetch all links to article texts"
        if(resourceName[:4] == 'http'):
            f = urllib.urlopen(resourceName)
        else:
            f = open(resourceName)
        i = NatureIssueParser()
        i.parse(f.read())
        self.issues.append(i)

    def idxlinks(self):
        return self.idxparser.links

if __name__ == '__main__':
    n = NatureSpider()
    n.readIndex('http://www.nature.com/nbt/archive/index.html')
    i = 0
    for l in n.idxlinks():
        if i > 10:
            break
        n.readIssue('http://www.nature.com'+l)
        i += 1
    for i in n.issues:
        print i.links
