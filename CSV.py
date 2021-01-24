#!/usr/bin/env python 
# coding=utf-8
    
import pprint
import json
import requests
import pandas as pd

json_data = None

json_file = 'stop_areas.json' 
with open(json_file) as json_data:     
    data = json.load(json_data)

pprint.pprint(data)
print(type(data))
print(data.keys())


'''partie request'''

URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
url_request = requests.get(url = URL, headers=headers)
raw_data = json.loads(url_request.text)

#print(url_request.json())
#print(type(raw_data))
#print(raw_data.keys())

liste_links = [] #là ou je vais les stockés pour pouvoir les transformer en CSV par la suite 
liste_id = [] 
liste_names = []
liste_coord = []


#MES IDS 
areas = raw_data['stop_areas']

for loop_area in areas : 
    if type(loop_area) == dict :
        if "id" in loop_area.keys(): 
            local_id = loop_area["id"]
            liste_id.append(local_id)
        else : 
            print("Missing key ids")
    else: 
        print("Unexpected format dict")

#print(area['id'])
#print(type(area), area)
#print(len(liste_id))
#print(liste_id)
#print(area.keys())

#MES LINKS

my_links = raw_data['links']
my_link = my_links[0]
#print(my_link)

for loop_link in my_links: 
    if type(loop_link) == dict: 
        if "href" in loop_link.keys(): 
            local_href = loop_link["href"]
            liste_links.append(local_href)
        else: 
            print("Missing key in this list")
    else: 
        print("Unexpected format: %s", s(type(loop_link)))        

#print(len(liste_links))
#print(liste_links)


#MES NOMS 

for loop_name in areas :
    if type(loop_name) == dict: 
        if "label" in loop_name.keys():
            local_name = loop_name["label"]
            liste_names.append(local_name)
        else: 
            print("Missing key in the list")
    else: 
        print("Unexpected format: %s ", s(type(loop_name)))

#print(liste_names)

#MES COORDONNEES 

for loop_coord in areas: 
    if type(loop_coord) == dict: 
        if "coord" in loop_coord.keys(): 
            local_coord = loop_coord["coord"]
            liste_coord.append(local_coord)
        else: 
            print("Missing key in the list")
    else: 
        print("Unexpected type")

print(liste_coord)

#TRANSFORMATION EN CSV 

df = pd.DataFrame(liste_links)  
    
df.to_csv('Mes_liens.csv') 