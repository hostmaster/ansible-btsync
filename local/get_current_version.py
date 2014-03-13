#! /usr/bin/env python

from BeautifulSoup import BeautifulSoup as BS
import urllib2

URL = "http://www.bittorrent.com/sync/downloads"

html = urllib2.urlopen(URL)
soup = BS(html)
elem = soup.findAll('li', {'title': 'title here'})




