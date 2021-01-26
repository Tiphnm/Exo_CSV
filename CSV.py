#!/usr/bin/env python 
# coding=utf-8
    
import pprint
import json
import requests
import pandas as pd

class ReadingSncfApi(): 
    def __init__(self): 
        self.URL = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
        self.raw_data = None 
        self.json_data = None
        self.data = None
        self.url_request = None
        self.raw = None
        self.liste_links = []
        self.liste_id = []
        self.liste_names = []
        self.liste_coord = []

    def read_json(self, file_name):
        self.json_file = file_name #stop_areas.json'
        with open(self.json_file, "r") as json_data:     
            self.data = json.load(json_data)

        #pprint.pprint(self.data)
        #print(type(data))
        #print(data.keys())

#l'executer dans un autre fichier ou teste en dehors de ma classe
#    read_json('stop_areas.json')# appeler ma fonction avec le nom de mon 'jsonfile' 

    def write_json(self, file_name):#crée mon fichier json uniquement de mes "stop_areas"
        self.url_request = requests.get(url = self.URL, headers= self.headers)
        with open(file_name, mode = "w") as file : #mon nom de fichie est "stop_areas_tiph.json"
            json.dump(self.url_request.json(), file)
            #retourne rien, juste pour sauvegarder le json

 #   def_write_json = write_json()

    def read_links(self, file_name): # enregistre mes liens 
        with open(file_name) as json_stop_areas_file: #"stop_areas_tiph.json"
            self.raw = json.load(json_stop_areas_file) #pas besoin de s car mon fichier est déjà convertis en text dans ma fonction précédente

    def loop_links(self, dict_key): # reads and saves json

        for loop_link in self.raw['links']: 
                if type(loop_link) == dict: 
                    if dict_key in loop_link.keys(): #dict_key = "href"
                        local_href = loop_link[dict_key]
                        self.liste_links.append(local_href)
                    else: 
                        print("Missing key in this list")
                else: 
                    print("Unexpected format: %s", s(type(loop_link)))  

        #print(type(liste_links))             
        return self.liste_links
    

    #MES IDS 

    def my_id(self, key_name) : 
        #key_name = "id"

        for loop_area in self.raw['stop_areas']: 
            if type(loop_area) == dict :
                if key_name in loop_area.keys(): 
                    local_id = loop_area[key_name]
                    self.liste_id.append(local_id)
                else : 
                    print("Missing key ids")
            else: 
                print("Unexpected format dict")

        #print(area['id'])
        #print(type(area), area)
        #print(len(liste_id))
        #print(self.liste_id)
        #print(area.keys())
        return self.liste_id

    #MES NOMS 
    def my_name(self, key_name):
        #key_name= 'label'

        for loop_name in self.raw['stop_areas'] :
            if type(loop_name) == dict: 
                if key_name in loop_name.keys():
                    local_name = loop_name[key_name]
                    self.liste_names.append(local_name)
                else: 
                    print("Missing key in the list")
            else: 
                print("Unexpected format: %s ", s(type(loop_name)))

        #print(self.liste_names)
        return self.liste_names

    #MES COORDONNEES 
    def my_coord(self, key_name):
        #key_name = 'coord'
        
        for loop_coord in self.raw['stop_areas']: 
            if type(loop_coord) == dict: 
                if key_name in loop_coord.keys(): 
                    local_coord = loop_coord[key_name]
                    self.liste_coord.append(local_coord)
                else: 
                    print("Missing key in the list")
            else: 
                print("Unexpected type")

        print(self.liste_coord)
        return self.liste_coord

'''
    #TRANSFORMATION EN CSV de mes names et coord 

    def csv_convert_info(liste1, liste2, liste3):
        my_dict = {'ID': liste1, 'NAME': liste2, 'COORD': liste3}
        print("This my list", liste1)

        df= pd.DataFrame(my_dict)

        df.to_csv('Mon_csv.csv')

        return csv_convert_info

    def_csv_convert_info = csv_convert_info(liste_id, liste_names, liste_coord)

        #faire une fonction pour chaque key 
        #faire une fonction qui prend toutes mes fonctions key pour créer un dictionnaire 
        #faire une fonction avec ces deux fonctions pour créer des fichiers CSV 
'''
my_class = ReadingSncfApi() #j'instancie pour pouvoir appeler une fonction de ma classe plus proprement 
my_class.read_links("stop_areas_tiph.json")
my_class.my_coord('coord') #je mets pas de self, je suis à l'extérieur de ma classe fonction, je mets dans mes parenthèses mon argument 