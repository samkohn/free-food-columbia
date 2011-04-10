import feedparser
urltoscrape = 'http://bwog.com/feed/'
d = feedparser.parse(urltoscrape)
for entry in d.entries:
    for cat in entry.categories:
        if cat[1]=="free food":
            print entry.title
            print entry.link
            print "\n"
