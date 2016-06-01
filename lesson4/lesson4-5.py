"""
Having data file with web site clients clients.json, find clients who don't
have access to web service (site uses Basic Authentication).
"""

import json
import requests

def client_auth():
    
    clients = json.load(open('clients.json'))
    accesses = {}
    access_denied = []
    access_granted = []
    
    def auththent(name, passwrd):
        
         web_service = "https://python-for-qa.herokuapp.com/login"
         authent = requests.get(web_service, auth=(name,passwrd))
         return authent.status_code
     
    for client in clients:
        if auththent(client['name'], client['password']) == 200:
             access_granted.append(client['name'])
        elif auththent(client['name'], client['password']) == 401:
            access_denied.append(client['name'])
    accesses['granted'] = access_granted
    accesses['denied'] = access_denied
    return accesses['denied']

if __name__ == '__main__':
    print client_auth()