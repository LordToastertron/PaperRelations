#!/usr/bin/env python
# Paper.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
#
# base class for all Paper types 
class Paper:
    
    def __init__(self):
        self.JournalFrom = ""
        self.Publisher = ""
        self.Title = ""
        self.DxUrl = ""
        self.Type = ""
        self.Authors = [ ]
        self.References = [ ]

if __name__ == "__main__":
    print "Testing Paper:\n"
    print "Instantiating Paper"
    n = Paper()
    print "Successfully instantiated n as Paper"
