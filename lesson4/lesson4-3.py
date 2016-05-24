# -*- coding:utf-8 -*-
"""
Write a script to parse habraharb_all.xml and print each article's title,
author and all categories.
"""

import xml.etree.ElementTree as etree
from io import StringIO

fle_xml = etree.parse('habraharb_all.xml')

root = fle_xml.getroot()

alll =[]
for child in root.iter('item'):
    a = {}
    z = []
    for i in child:
        if i.tag == 'author':
            a['author'] = i.text
        if i.tag == 'title':
            a['title'] = i.text
        for x in i.iter('category'):
            z.append(x.text)
        a['category'] = z
        
    alll.append(a)   

for i in alll:
    print i