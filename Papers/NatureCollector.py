#!/usr/bin/env python
#
# NatureCollector.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
#
# class that grabs all of the .ris files in a directory and
# creates NaturePaper objects, populated with data in a list
# to insert into a relational database.

import NaturePaper from NaturePaper
import os

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
            self.paperList.append()
