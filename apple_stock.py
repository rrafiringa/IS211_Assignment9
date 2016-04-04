#!/usr/bin/env python
# -*- Coding: utf-8 -*-

from urlfetch import *

URL = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
HTML = fetch_url(URL)
TABLE_DATA = DataFinder(HTML)
DATANODE = TABLE_DATA.html_get_node('table', {'class': 'yfnc_datamodoutline1'})
HEADER = DATANODE.find('th')
print HEADER
