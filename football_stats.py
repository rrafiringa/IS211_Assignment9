#!/usr/bin/env python
# -*- Coding: utf-8 -*-

# Part I:

from urlfetch import *

URL = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns'
HTML = fetch_url(URL)
HATTR = 'th > a'
DATTR = 'tr[class^="row"]'
HTDATA = DataFinder(HTML)
HEADER = HTDATA.html_css_search(HATTR)
DATA = HTDATA.html_css_search(DATTR, ',')
TABLE = [dict(zip(HEADER, ROW.split(','))) for ROW in DATA]
HSEP = '---------------------------------------------------'
print '{:^20}|{:^5}|{:^12}|{:^10}'.format('Player', 'Team', 'Touchdown', 'Position')
print HSEP
for idx in xrange(20):
    player = TABLE[idx]['Player']
    team = TABLE[idx]['Team']
    tdown = TABLE[idx]['TD']
    pos = TABLE[idx]['Pos']
    print '{:^20}|{:^5}|{:^12}|{:^10}'.format(player, team, tdown, pos)
    print HSEP
