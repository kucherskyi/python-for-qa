# -*- coding:utf-8 -*-

"""
Write a function to get product price from web page for Deshevshe site.
Handle the case when a product is out of stock.
"""

# from xml.etree import ElementTree as etree

import requests
from lxml import etree, html
import string

LINK = 'http://deshevshe.ua/projector-acer/acer_c205_fwvga_150_ansi_lm_mrjh911001'

def parceurl(urla):

    item = {}
    responce = requests.get(urla)
    tree = html.fromstring(responce.content)
    printable = set(string.printable)
    item['name'] = filter(lambda x: x in printable, 
                          tree.xpath('//h1[@itemprop="name"]/text()')[0]).lstrip()
    item['category'] = filter(lambda x: x not in printable, 
                          tree.xpath('//h1[@itemprop="name"]/text()')[0])
    item['price'] = tree.xpath('//span[@itemprop="price"]/text()')[0]
    aval = tree.xpath('//div[@class="wareAvail"]/text()')[0]
    if aval == 'Є в наявності'.decode('utf-8'):
        item['avaliable'] = 'True'
    elif aval == 'Немає в наявності'.decode('utf-8'):
        item['avaliable'] = 'Афдіу'
    return item

if __name__ == '__main__':
    print parceurl(LINK)
