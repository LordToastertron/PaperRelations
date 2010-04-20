#!/usr/bin/python
#
# NatureSpider.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details

from NatureIndexParser import NatureIndexParser
from NatureIssueParser import NatureIssueParser
import urllib, random

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
        random.shuffle(self.idxparser.links)
        return self.idxparser.links

    def readIssues(self):
        i = 0
        for l in self.idxlinks():
            if i > 10:
                break
            self.readIssue('http://www.nature.com'+l)
            i += 1

    def articlelinks(self):
        a = []
        for i in self.issues:
            for l in i.links:
                a.append(l)
        return a

    

if __name__ == '__main__':
    n = NatureSpider()
    n.readIndex('http://www.nature.com/nbt/archive/index.html')
    n.readIssues()
    print sorted(n.articlelinks())
