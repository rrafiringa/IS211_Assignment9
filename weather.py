#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
Part III: Weather data
"""

import datetime

from urlfetch import *

now = datetime.datetime.now()
today = now.day

URL = 'https://www.wunderground.com/history/airport/KNYC/2015/4/1/MonthlyHistory.html'
HTML = fetch_url(URL)
SAMPLE = DataFinder(HTML)

DATA = SAMPLE.get_tag_by_attr('table', {'id': 'obsTable'})
HEADER = list()
ROWS = list()

for tags in DATA:
    for head in tags.find_all('th'):
        HEADER.append(unicode(head.get_text(strip=True)).encode('ascii', 'ignore'))
    tags.thead.decompose()
    row = list()
    for tbody in tags.find_all('tbody'):
        row = unicode(tbody.tr.get_text('|', strip=True)).encode('ascii', 'ignore').replace('\n', '').split('|')
        ROWS.append(row)

DFIELDS = '|{:^14}|{:^6}|{:^6}|{:^6}|'

HFIELDS = '|{:^14}|{:^20}|'

SEP = '-------------------------------------'

print '\nPast and present temperatures:'

print SEP
date_, temps_ = HEADER[0], HEADER[1]
FIRST = ROWS.pop(0)
HFIELDS = HFIELDS.format(date_, temps_)
print HFIELDS
print SEP
SECOND = DFIELDS.format(FIRST[0],
                        FIRST[1],
                        FIRST[2],
                        FIRST[3])
print SECOND
print SEP

for row in ROWS:
    day_, hi_, mid_, lo_ = row[0], row[1], row[2], row[3]
    print DFIELDS.format(day_, hi_, mid_, lo_)
    print SEP
    if str(day_) == str(today):
        print '\nForecasted temperatures:'
        print SEP
        print HFIELDS
        print SEP
        print SECOND
        print SEP
