#!/usr/bin/env python
#
# NatureCollector.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
#
# class that grabs all of the .ris files in a directory and
# creates NaturePaper objects, populated with data in a list
# to insert into a relational database.

from NaturePaper import NaturePaper
import os
import sys

class NatureCollector:

    def __init__(self, path):
        self.path = path
        self.paperList = []

    def ls(self):
        return os.listdir(self.path)

    def loadPapers(self):
        for f in self.ls():
            if f.find('ref') > -1:
                continue
            p = NaturePaper()
            print f
            p.loadCitFile(self.path + f)
            p.loadRefFile(self.path + f.replace('.','refs.'))
            self.paperList.append(p)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print sys.argv[1]
        nc = NatureCollector(sys.argv[1])
    else:
        nc = NatureCollector('.')
    nc.loadPapers()
    for i in nc.paperList:
        print i.Title
