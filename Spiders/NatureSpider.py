#!/usr/bin/python
#
# NatureSpider.py
# created: nathan dotz - nathan (dot) dotz (at) gmail (dot) com
# license: GNU GPL3 - see LICENSE file for details

# The hierarchy of Nature's site involves a main index, which links to 
# pages representing each volume(issue). Each of these issues contain 
# links to some number of articles. Each article may contain one or 
# more reference files.
# thus:
# index                       <- readIndex fetches hrefs to issues
#   |                         <- readIssues loops through issue links to
#   |                               call readIssue on eatch
#   `-issue                   <- readIssue fetches hrefs to articles 
#   |   |
#   |   `-article #1111       <- readArticle fetches hrefs to ref files
#   |   |   |                 <- fetchReferences gets actual ref files
#   |   |   `- 1111refs.ris
#   |   |   |
#   |   |   `- 1111.ris
#   |   |
#   |   `-article #1234
#   |       |
#   |       `- 1234refs.ris
#   |       |
#   |       `- 1234.ris
#   `-issue
#
# usw...
#
# 

from NatureIndexParser import NatureIndexParser
from NatureIssueParser import NatureIssueParser
import urllib, random

class NatureSpider:
    "Class for handling hierarchy of and fetching reference files "
    "from Nature websites "

    def __init__(self):
        self.idxparser = NatureIndexParser()
        self.issues = []
        self.articles = []

    def __getResource(self,resourceName):
        "Dynamically return a resource handle based on its name"
        if(resourceName[:4] == 'http'):
            f = urllib.urlopen(resourceName)
        else:
            f = open(resourceName)
        return f

    def readIndex(self, resourceName):
        "Reads a resource to parse for links to issues. This should be a "
        "filename or url. urls are assumed to start with 'http'"
        f = self.__getResource(resourceName)
        self.idxparser.parse(f.read())

    def readIssue(self, resourceName):
        "Read a resource to fetch all links to article texts, and push it "
        "on to the list of issues."
        i = NatureIssueParser()
        f = self.__getResource(resourceName)
        i.parse(f.read())
        self.issues.append(i)

    def readArticle(self, resourceName):
        "Read a resource to fetch all links to article reference files, "
        "and push it on to a list of articles"
        a = NatureArticleParser()
        f = self.__getResource(resourceName)
        a.parse(f.read())
        self.articles.append(a)

    def indexLinks(self):
        "Return a list of links from the idxparser, randomized, so that "
        "site access is non-sequential"
        random.shuffle(self.idxparser.links)
        return self.idxparser.links

    def articleLinks(self):
        "Compile and return a randomized list of links to article pages "
        "from the tree of links in issues"
        a = []
        for i in self.issues:
            for l in i.links:
                a.append(l)
        random.shuffle(a)
        return a

    def readIssues(self):
        "Loop over links provided in the idxparser, pushing NatureIssue "
        "instances onto self.issues via readIssue"
        i = 0
        for l in self.indexLinks():
            if i > 10:              # stopgap for testing, so as not 
                break               # to pull whole site ever time
            self.readIssue('http://www.nature.com'+l)
            i += 1

    def readArticles(self):
        "Parse all articles queued in self.articleLinks() by "
        "mapping self.readArticle"
        for l in this.articleLinks():
            self.readArticle('http://nature.com'+l)

    def fetchReferences(self):
        pass
    

if __name__ == '__main__':
    prefix = 'nbt';
    n = NatureSpider()
    urlstr = 'http://www.nature.com/'+prefix+'/archive/index.html'
    n.readIndex(urlstr)
    n.readIssues()
    print sorted(n.articleLinks())
