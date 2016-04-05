#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
Part III: Weather data
"""

from urlfetch import *

URL = 'https://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html'
HTML = fetch_url(URL)
SAMPLE = DataFinder(HTML)

DATA = SAMPLE.get_tag_by_attr('table', {'id': 'obsTable'})
HEADER = list()
ROWS = list()
for tags in DATA:
    for head in tags.find_all('th'):
        HEADER.append(unicode(head.get_text(strip=True)).encode('ascii', 'xmlcharrefreplace'))
    tags.thead.decompose()

    for rows in tags.find_all('tr'):
        row = list()
