#!/usr/bin/python3

import re, time
from urllib.request import urlopen, Request
url = 'http://example.webscraping.com/places/default/index/0'

def url_page(url, start, end):
    ''' Шукаємо сторінки на сайті webscraping.com
    '''
    #start - індекс першої сторінки сайту
    #end - індекс останньої сторінки
    lst = url.split('/')
    s = int(lst[-1])
    start = s + start
    start = str(start)
    lst[-1] = start
    url = '/'.join(lst)
    return url

def country(url, start, end):
    '''Програма виводить назви країн із сайту web scraping'''
    while start < end:
        country_request = Request(url_page(url, start, end))
        country_page = urlopen(country_request).read()
        country_page = str(country_page)
        # шукаємо індекси країн на кожній окремій сторінці
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
        time.sleep(1)



print("Country: ")
country(url, 0, 25)

