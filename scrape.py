import urllib
import feedparser
urltoscrape = 'http://bwog.com/feed/'
x = urllib.urlopen(urltoscrape)
str1 = x.read()
d = feedparser.parse(urltoscrape)
x.close()
#print str1
#print d.feed.title
for entry in d.entries:
    for cat in entry.categories:
        if cat[1]=="free food":
            print entry.title
        
