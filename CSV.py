#!/usr/bin/env python 
# coding=utf-8
    
import pprint
import json
import requests
import pandas as pd

def read_json(file_name):
    json_data = None

    json_file = file_name #stop_areas.json'
    with open(json_file) as json_data:     
        data = json.load(json_data)

    pprint.pprint(data)
    #print(type(data))
    #print(data.keys())

read_json('stop_areas.json')# appeler ma fonction avec le nom de mon 'jsonfile'

'''partie request'''

URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
url_request = requests.get(url = URL, headers=headers)
raw_data = json.loads(url_request.text)

#print(url_request.json())
#print(type(raw_data))
#print(raw_data.keys())

areas = raw_data['stop_areas']

#faire une fonction qui enregistre mon fichier 

#MES LINKS

liste_links = [] #là ou je vais les stockés pour pouvoir les transformer en CSV par la suite 

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

#MES IDS 

def my_id(key_name) : 
    #key_name = "id"
    liste_id = [] 

    for loop_area in areas : 
        if type(loop_area) == dict :
            if key_name in loop_area.keys(): 
                local_id = loop_area[key_name]
                liste_id.append(local_id)
            else : 
                print("Missing key ids")
        else: 
            print("Unexpected format dict")

    #print(area['id'])
    #print(type(area), area)
    #print(len(liste_id))
    print(liste_id)
    #print(area.keys())

my_id("id")

#MES NOMS 
def my_name(key_name):
    #key_name= 'label'
    liste_names = []

    for loop_name in areas :
        if type(loop_name) == dict: 
            if key_name in loop_name.keys():
                local_name = loop_name[key_name]
                liste_names.append(local_name)
            else: 
                print("Missing key in the list")
        else: 
            print("Unexpected format: %s ", s(type(loop_name)))

    print(liste_names)

my_name('label')

#MES COORDONNEES 
def my_coord(key_name):
    #key_name = 'coord'
    liste_coord = []

    for loop_coord in areas: 
        if type(loop_coord) == dict: 
            if key_name in loop_coord.keys(): 
                local_coord = loop_coord[key_name]
                liste_coord.append(local_coord)
            else: 
                print("Missing key in the list")
        else: 
            print("Unexpected type")

    print(liste_coord)

my_coord('coord')

#TRANSFORMATION EN CSV de mes liens 
'''
df = pd.DataFrame(liste_links)  
    
df.to_csv('Mes_liens.csv') '''

#TRANSFORMATION EN CSV de mes names et coord 
'''
dict = {'ID': liste_id, 'NAME': liste_names, 'COORD': liste_coord}

df= pd.DataFrame(dict)

df.to_csv('Mon_csv.csv')
'''
#faire une fonction pour chaque key 
#faire une fonction qui prend toutes mes fonctions key pour créer un dictionnaire 
#faire une fonction avec ces deux fonctions pour créer des fichiers CSV 