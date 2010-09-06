#!/usr/bin/env python
#
# NatureIndexParser.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details
# Grabs the set of links from an index page of Nature-type articles
# to be used to spider for other citations

from Parser import Parser
import re

class NatureIndexParser(Parser):

    def start_a(self,attrs):
        for prop, value in attrs:
            if prop == "href" and re.search("/journal/v[0-9]", value) != None:
                self.links.append(value)

