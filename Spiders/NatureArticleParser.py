#!/usr/bin/env python
#
# Parser.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details

from Parser import Parser
import re

class NatureArticleParser(Parser):

    def start_a(self,attrs):
        for prop, value in attrs:
            if prop == "href" and re.search("/journal/v[0-9].*\.ris$", value) != None:
                self.links.append(value)
