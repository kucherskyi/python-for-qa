# -*- coding:utf-8 -*-

"""
Write a function to get product price from web page for Deshevshe site.
Handle the case when a product is out of stock.
"""

# from xml.etree import ElementTree as etree

import requests
from lxml import etree, html
from xml.etree.ElementTree import ParseError
from io import StringIO, BytesIO
import re

LINK = 'http://deshevshe.ua/mobile-asus/asus_zenfone_6_a600cg_gold'

responce = requests.get(LINK)
tree = html.fromstring(responce.content)

name_item = tree.xpath('//h1[@itemprop="name"]/text()')
price =tree.xpath('//span[@itemprop="price"]/text()')
pri =tree.xpath('//div[@class="wareAvail"]/text()')

if 'Немає в наявності' in responce.content:
    avalible = True
else:
    avalible = False

print name_item[0]
print price[0]
print pri[0]
