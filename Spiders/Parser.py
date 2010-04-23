#!/usr/bin/env python
#
# Parser.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
# base class for link-grabbing parser

import sgmllib

class Parser(sgmllib.SGMLParser):

    def __init__(self, verbose=0):
        sgmllib.SGMLParser.__init__(self,verbose)
        self.links = []

    def parse(self, input):
        self.feed(input)
        self.close()
