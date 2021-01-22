#!/usr/bin/env python 
# coding=utf-8
    
import pprint
import json
import requests

json_data = None

json_file = 'stop_areas.json' 
with open(json_file) as json_data:     
    data = json.load(json_data)

pprint.pprint(data)
print(type(data))
print(data.keys())

URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
url_request = requests.get(url = URL, headers=headers)
print(url_request)
print(url_request.json())