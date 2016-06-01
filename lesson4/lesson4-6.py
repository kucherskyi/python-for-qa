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
import collections

from lxml import etree
import requests
import xmltodict

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def inttostr(dic):
    for k,v in dic.items():
        if isinstance(v, int) or isinstance(v, float):
            dic[k] = '{}'.format(v)
        if isinstance(v, bool):
            dic[k] = '{}'.format(v).lower()
        try:
            dic[k] = v.replace('\r\n','')
        except:
            pass
        if isinstance(v, list):
            try:
                dic[k] = map(inttostr, v)
            except:
                pass
    return dic


        
        
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
dat222 = json.dumps(data_json)
data_json = json.loads(data_json)
data_xml = map(convert, z)
data_json = map(convert, data_json)
for i in data_json: 
    inttostr(i)


def compare(xml,json):
    
    def compval(a,b):
        dif = []
        for v in a.values():
            for s in b.values():
                if  v!= s:
                    dif.append('{}{}'.format(v, s))
        return dif

    differ = []
    for el in xml:
        for ele in json:
            if el['guid'] == ele['guid']:
                if cmp(ele, el) != 0:
                    differ.append(compval(el, ele))
                    
    return differ 
    

for i in compare(data_xml, data_json):
    print i