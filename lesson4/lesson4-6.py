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

import lxml
import requests

req = requests.get('https://python-for-qa.herokuapp.com/login',
                   auth = ('admin', 'password'))

print req.cookies['X-AUTH-TOKEN']