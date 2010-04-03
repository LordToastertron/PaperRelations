#!/usr/bin/env python
#
# NaturePaper.py
#
#


# class for dealing with papers from nature publishing group.

# nature citations come in two files. one citation file, and one references
# file, both with the same format.

from Paper import Paper

class NaturePaper(Paper):

    def __init__(self, citFile = "", refFile = ""):
        Paper.__init__(self)
        self.citFile = citFile
        self.refFile = refFile


if __name__ == "__main__":
    print "Testing NaturePaper:\n"
    print "Instantiating NaturePaper"
    n = NaturePaper()
    print "Successfully instantiated n as NaturePaper"
