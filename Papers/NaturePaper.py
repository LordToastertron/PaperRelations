#!/usr/bin/env python
#
# NaturePaper.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
#
# class for dealing with papers from nature publishing group.
# nature citations come in two files. one citation file, and one references
# file, both with the same format.

from Paper import Paper
import re

class NaturePaper(Paper):

    def __init__(self, citFile = '', refFile = ''):
        Paper.__init__(self)
        self.citFile = citFile
        self.refFile = refFile

    def parseCitation(self, splitLinesFromCitation):
        "Takes a list of split lines from a citation file, and iterates "
        "over them load the appropriate data"
        for line in splitLinesFromCitation:
            if line.strip() == '':
                continue
            try:
                head, info = line.split('-',1)
            except ValueError:
                continue
            #print "split",head,"and",info
            if head.strip() == "TI": self.Title = info.strip()
            if head.strip() == "TY": self.Type = info.strip()
            if head.strip() == "JA": self.JournalFrom = info.strip()
            if head.strip() == "PB": self.PublishingGroup = info.strip()
            if head.strip() == "UR": self.DxUrl = info.strip()
            if head.strip() == "AU":
                last,first = info.strip().split(',',1)
                self.Authors.append((last,first))

    def loadCitFile(self, filename):
        "Takes a filename, opens file, then sends the split "
        "lines to parseCitation to load the current Paper's citation"
        handle = open(filename, 'r')
        lines = handle.read()
        lines = lines.split("\n")
        self.parseCitation(lines)

    def loadRefFile(self,filename):
        "Takes a filename, opens file, splits on blank lines,"
        " then splits again to create new objects via parseCitation"
        handle = open(filename, 'r')
        lines = handle.read()
        lines = lines.split("\n\n")
        for line in lines:
            tempPaper = NaturePaper()
            tempPaper.parseCitation(line.split("\n"))
            self.References.append(tempPaper)


if __name__ == '__main__':
    print "Testing NaturePaper:\n"
    print 'Instantiating NaturePaper'
    n = NaturePaper()
    print 'Successfully instantiated n as NaturePaper'
    print 'Loading citation file'
    n.loadCitFile("/home/nate/workspace/PaperRelations/nbt.1618.ris")
    print 'Citation file loaded'
    print 'Loading References file'
    n.loadRefFile("/home/nate/workspace/PaperRelations/nbt.1618refs.ris")
