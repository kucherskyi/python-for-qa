# -*- coding:utf-8 -*-

"""
Write a function to get product price from web page for Deshevshe site.
Handle the case when a product is out of stock.
"""

# from xml.etree import ElementTree as etree

import requests
from lxml import etree, html

LINK = 'http://deshevshe.ua/projector-acer/acer_c205_fwvga_150_ansi_lm_mrjh911001'

def parceurl(urla):
    
    responce = requests.get(urla)
    tree = html.fromstring(responce.content)
    name_item = tree.xpath('//h1[@itemprop="name"]/text()')[0]
    price =tree.xpath('//span[@itemprop="price"]/text()')[0]
    avaliable =tree.xpath('//div[@class="wareAvail"]/text()')[0]
    print name_item
    print price
    print avaliable

parceurl(LINK)
