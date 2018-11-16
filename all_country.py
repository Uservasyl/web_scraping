#!/usr/bin/python3

'''Програма виводить назви країн із сайту web scraping'''

import html, re
from urllib.request import urlopen, Request
url = 'http://example.webscraping.com/places/default/index/0'
def split_url(url, start, end):
    lst = url.split('/')
    s = int(lst[-1])
    start = s + start
    start = str(start)
    lst[-1] = start
    url = '/'.join(lst)
    return url

def country(url, start, end):
    #getting page from server
    while start < end:
        country_request = Request(split_url(url, start, end))
        country_page = urlopen(country_request).read()
        country_page = str(country_page)
        COUNTRY_TAG = [m.start() for m in re.finditer('.png" />', country_page)]
        for tag_index in COUNTRY_TAG:
            country_tag_size = len(COUNTRY_TAG)
            country_value_start = tag_index + country_tag_size -1
            country = ''
            for char in country_page[country_value_start:]:
                if char != '<':
                    country += char
                else:
                    break
            print('{}'.format(country))
        start += 1



# print("Country: ")
country(url, 0, 26)