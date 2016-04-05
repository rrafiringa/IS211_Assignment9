#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
Part II: Apple Stock
"""

from urlfetch import *

URL = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
HTML = fetch_url(URL)
TABLE_DATA = DataFinder(HTML)

HEADER = TABLE_DATA.get_tag_by_css('th[class$="head1"]')

TRS = TABLE_DATA.get_tag_by_attr('tr')

FIELDS = '|{:^14}|{:^8}|'
SEP = '-------------------------'

ROWS = list()

ROWS.append(HEADER)

for tr in TRS:
    tds = tr.find_all('td')
    row = []
    if len(tds) == 7:
        for td in tds:
            row.append(str(td.get_text(strip=True)))
    if len(row) > 0:
        ROWS.append(row)

print 'AAPL stock close price by date:'
print SEP
for row in ROWS:
    date_, open_, high_, low_, close_, vol_, adj_ = row
    print FIELDS.format(date_, close_)
    print SEP
