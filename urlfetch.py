#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reusable url fetching module
"""

import csv
import urllib2

from bs4 import BeautifulSoup


def fetch_url(url):
    """
    URL fetcher
    :param url: (String) URL to fetch
    :return: (string) URL data
    """
    try:
        return urllib2.urlopen(urllib2.Request(url))
    except urllib2.URLError as error:
        if hasattr(error, 'reason'):
            print r"Could not connect to server."
            print r'Reason: ', error.reason
        elif hasattr(error, 'code'):
            print r"The server couldn't fulfill the request."
            print r"Error code: ", error.code


class DataFinder(object):
    """
    Find data within HTML
    """

    def __init__(self, html_text):
        """
        Constructor
        :param html_text: (String) HTML text
        """
        self.soup = BeautifulSoup(html_text, 'lxml')
        self.header = []
        self.data = []
        self.has_header = False
        self.has_data = False

    def get_data_header(self):
        """
        Return data header
        :return: (List) Data headers
        """
        if self.has_header:
            return self.header
        return self.has_header

    def get_data_rows(self):
        """
        Return data rows
        :return: (List) Data rows
        """
        if self.has_data:
            return self.data
        return self.has_data

    def html_get_node(self, tag, attrs):
        """
        Return a portion of the HTML code
        :param tag: (String) HTML tag
        :param attrs: (Dict) HTML tag attributes
        :return: (Object) Tag object
        """
        return self.soup.find_all(tag, attrs)

    def html_tag_search(self, tag, props, sep=''):
        """
        Find tags by tag name and properties
        :param tag: (String) Tag name
        :param props: (Dict) Tag properties
        :param sep: (String) Separator Character
        :return: (List) Data columns
        """
        data = self.soup.find_all(tag, props)
        return [row.get_text(sep, strip=True) for row in data]

    def html_css_search(self, attr, sep=''):
        """
        Find tags by CSS attributes
        :param attr: (String) CSS attribute
        :param sep: (String) Separator character
        :return: (List) Data columns
        """
        data = self.soup.select(attr)
        return [row.get_text(sep, strip=True) for row in data]

    def html_func_search(self, func, sep=''):
        """
        Leverages a boolean function to match tags.
        :param func: (Function) Filtering function
        :param sep: (String) Separator character
        :return: (List) Data columns
        """
        data = self.soup(func)
        return [row.get_text(sep, strip=True) for row in data]

    def to_csv(self, file_name, mode='ab'):
        """
        Write header and data to CSV
        :param file_name: (String) Output file name.
        :param mode: (String)
            ab = Append
            wb = (Over)Write
        :return: None
        """
        with open(file_name, mode) as outfile:
            csv_writer = csv.writer(outfile)
            if self.has_header:
                csv_writer.writerows(self.header)
            csv_writer.writerows(self.data)
