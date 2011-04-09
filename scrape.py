import urllib
urltoscrape = 'http://bwog.com/feed/'
x = urllib.urlopen(urltoscrape)
str1 = x.read()
x.close()
print str1
