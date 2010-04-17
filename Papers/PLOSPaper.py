#!/usr/bin/env/python
# PLOSPaper.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
#
# class for dealing with PLOS papers. currently a stub.
from Paper import Paper

class PLOSPaper(Paper):

    def __init__(self, citFile = '', refFile = ''):
        Paper.__init__(self)
        self.citFile = citFile
        self.refFile = refFile
