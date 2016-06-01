# -*- coding:utf-8 -*-
"""
Write a program to compare web service result in XML and JSON formats. Here is
the information about web service:

- url: https://python-for-qa.herokuapp.com/data
- uses token based authentication, token should be passed in request
header: X-AUTH-TOKEN
- to get token send GET request to https://python-for-qa.herokuapp.com/login
(Basic Authentication, user=``admin``, password=``password``)
- service returns data in XML and JSON formats based on Accept header
"""

import json

from lxml import etree
import requests
import xmltodict


req = requests.get('https://python-for-qa.herokuapp.com/login',
                   auth = ('admin', 'password'))
token = json.loads(req.content)['token']

co = requests.Session()
data_url = 'https://python-for-qa.herokuapp.com/data'
co.headers.update({'X-AUTH-TOKEN': token})
data_xml = co.get(data_url, headers = {'Accept': 'application/xml'} ).content
data_json = co.get(data_url, headers = {'Accept': 'application/json'} ).content

z = json.dumps(xmltodict.parse(data_xml), indent=4)
z = json.loads(z)['items']['item']
data_json = json.loads(data_json)

for i in data_json:
    for k,v in i.items():
        i[k] = str(v).decode()
        if isinstance(i[k], list):
            i[k] = '[ {} ]'.format(str(i[k])) 
            
        
    i['isActive'] = str(i['isActive']).lower()

"""a1 = open('json.json','w')"""
'''a2 = open('xml.json','w')
a1.write(data_json)
a2.write(json.dumps(z, indent=2))'''



def rec():
    all_sorted = []
    daaa = iter(data_json)
    for i in z:
        sss = daaa.next()
        if i != sss:
            print i
            print sss
        else:
            rec()  
    
rec()