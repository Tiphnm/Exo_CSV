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

    #pprint.pprint(data)
    #print(type(data))
    #print(data.keys())

read_json('stop_areas.json')# appeler ma fonction avec le nom de mon 'jsonfile'

'''partie request'''


URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
raw_data = None

def read_json():#crée mon fichier json 
    url_request = requests.get(url = URL, headers=headers)
    with open("stop_areas_tiph.json", mode = "w") as file : 
        json.dump(url_request.json(), file)
        #retourne rien, juste pour sauvegarder le json
def_read_json = read_json()

def read_links(): # enregistre mes liens 
    with open("stop_areas_tiph.json") as json_stop_areas_file: 
        raw = json.load(json_stop_areas_file) #pas besoin de s car mon fichier est déjà convertis en text dans ma fonction précédente
    return raw

raw_data = read_links()


def loop_links(): # reads and saves json

    my_links = raw_data['links']    

    liste_links = [] 
    
    for loop_link in my_links: 
            if type(loop_link) == dict: 
                if "href" in loop_link.keys(): 
                    local_href = loop_link["href"]
                    liste_links.append(local_href)
                else: 
                    print("Missing key in this list")
            else: 
                print("Unexpected format: %s", s(type(loop_link)))  

    #print(type(liste_links))             
    return liste_links
 
def_loop_links = loop_links()

#MES IDS 
areas = raw_data['stop_areas']

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
    return liste_id

liste_id = my_id("id")
print("TEST", liste_id)

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

    #print(liste_names)
    return liste_names

liste_names = my_name('label')

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
    return liste_coord

liste_coord = my_coord('coord')

#TRANSFORMATION EN CSV de mes names et coord 

def csv_convert_info(liste1, liste2, liste3):
    my_dict = {'ID': liste1, 'NAME': liste2, 'COORD': liste3}
    print("This my list", liste1)

    df= pd.DataFrame(my_dict)

    df.to_csv('Mon_csv.csv')

    return csv_convert_info

def_csv_convert_info = csv_convert_info(liste_id, liste_names, liste_coord)

#TRANSFORMATION EN CSV de mes liens 
'''
df = pd.DataFrame(liste_links)  
    
df.to_csv('Mes_liens.csv') 
'''
    #faire une fonction pour chaque key 
    #faire une fonction qui prend toutes mes fonctions key pour créer un dictionnaire 
    #faire une fonction avec ces deux fonctions pour créer des fichiers CSV 