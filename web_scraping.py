#!/usr/bin/python3

import re
from urllib.request import urlopen, Request


def country(url):
    '''Програма виводить назви країн тільки з першої сторінки сайту web scraping
    '''                                 

    country_request = Request(url) #getting page from server
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


url = 'http://example.webscraping.com/places/default/index/0'
print("Country: ")
country(url)