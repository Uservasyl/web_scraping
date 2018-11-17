#!/usr/bin/python3

import re, time
from urllib.request import urlopen, Request
url = 'http://example.webscraping.com/places/default/index/0'

def url_page(url, start, end):
    ''' Шукаємо сторінки на сайті webscraping.com'''
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
    '''Програма виводить інформацію про країну із сайту web scraping'''
    country_find = input("Введіть назву країни: \n")
    country_list = []
    while start < end:
        country_request = Request(url_page(url, start, end))
        country_page = urlopen(country_request).read()
        country_page = str(country_page)

        # шукаємо індекси країн на кожній окремій сторінці
        COUNTRY_TAG = [m.start() for m in re.finditer('.png" />', country_page)]

        for tag_index in COUNTRY_TAG:                         #створюємо список країн
            country_tag_size = len(COUNTRY_TAG)
            country_value_start = tag_index + country_tag_size -1
            country = ''
            for char in country_page[country_value_start:]:
                if char != '<':
                    country += char
                else:
                    break
            country_list.append(country)
        start += 1
        time.sleep(0.7)

    if country_find in country_list:                #перевіряємо чи країна є у списку
        url_country = 'http://example.webscraping.com/places/default/view/' + country_find + '-' + str(country_list.index(country_find) + 1)
        country_request_url = Request(url_country)
        country_page = urlopen(country_request_url).read()
        country_page = str(country_page)
        print(country_page)
    else:
        print(f"Такої країни як {country_find} немає в списку")

country(url, 0, 4)
