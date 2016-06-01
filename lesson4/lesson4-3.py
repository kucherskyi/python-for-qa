# -*- coding:utf-8 -*-
"""
Write a script to parse habraharb_all.xml and print each article's title,
author and all categories.
"""

import xml.etree.ElementTree as etree
from io import StringIO

a  = 'habraharb_all.xml'
def parser(file):
    
    fle_xml = etree.parse(file)
    root = fle_xml.getroot()
    all_items = []
    for child in root.iter('item'):
        items = {}
        cat = []
        for item in child:
            if item.tag == 'author':
                items['author'] = item.text
            if item.tag == 'title':
                items['title'] = item.text
            for category in item.iter('category'):
                cat.append(category.text)
            items['category'] = cat
        all_items.append(items)   
    return all_items

if __name__ == '__main__':
    print parser(a)