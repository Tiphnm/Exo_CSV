#!/usr/bin/env python 
# coding=utf-8
    
import pprint
import json
import requests
import pandas as pd
import datetime
import logging 

logging.basicConfig(filename='loggings.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an error:')

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
        self.url_lyon = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
        self.lyon_url_request = None
        self.station_paris_lyon = []
        self.stops = None

        #rajouter mon file_name dans le init car je l'utilise en général 
        #pareil pour le json.file
    logging.info("Reading my json file : start")     
    def read_json(self, file_name):

        self.json_file = file_name #stop_areas.json'
        with open(self.json_file, "r") as json_data:     
            self.data = json.load(json_data)

        pprint.pprint(self.data)
    logging.info("Reading my json file : end")

        #print(type(data))
        #print(data.keys())

#l'executer dans un autre fichier ou teste en dehors de ma classe
#    read_json('stop_areas.json')# appeler ma fonction avec le nom de mon 'jsonfile' 
    
    logging.info("Reading my json file, only stop_areas : start")     
    def write_json(self, file_name):#crée mon fichier json uniquement de mes "stop_areas"
        self.url_request = requests.get(url = self.URL, headers= self.headers)
        with open(file_name, mode = "w") as file : #mon nom de fichie est "stop_areas_tiph.json"
            json.dump(self.url_request.json(), file)
            #retourne rien, juste pour sauvegarder le json

    logging.info("Reading my json file, only stop_areas : end")     

    def read_links(self, file_name): # enregistre mes liens 
        with open(file_name) as json_stop_areas_file: #"stop_areas_tiph.json"
            self.raw = json.load(json_stop_areas_file) #pas besoin de s car mon fichier est déjà convertis en text dans ma fonction précédente
   

    logging.info("Saving all my links : start")     

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

    logging.info("Saving all my links : end")     


    #MES IDS 

    logging.info("Saving all my stops's ID in a list : start")     

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
        print(self.liste_id)
        #print(area.keys())

    logging.info("Saving all my stops's ID in a list : end")     

    #MES NOMS 

    logging.info("Saving all my stops's names in a list : start")     

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

        print(self.liste_names)

    logging.info("Saving all my stops's names in a list : end")     


    #MES COORDONNEES 

    logging.info("Saving all my stops's coord in a list : start")     

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

    logging.info("Saving all my stops's coord in a list : end")     

    #TRANSFORMATION EN CSV de mes names et coord 

    logging.info("Saving all my lists in a CSV file: start")     

    def csv_convert_info(self, file_name): # mes listes sont dans le init, pas besoin de les mettre en argument
        my_dict = {'ID': self.liste_id, 'NAME': self.liste_names, 'COORD': self.liste_coord}

        df= pd.DataFrame(my_dict)

        df.to_csv(file_name) #'Mon_csv.csv'   

    logging.info("Saving all my lists in a CSV file: end")     
    
    
    #################################################PARTIE LYON#################################################

    logging.info("Reading my file on Lyon in json : start")     

    def lyon_read_json(self):
        self.lyon_url_request = requests.get(url = self.url_lyon, headers= self.headers)
        self.lyon_raw_data = json.loads(self.lyon_url_request.text)
        #pprint.pprint(self.lyon_raw_data)

    logging.info("Reading my file on Lyon in json : end")     


    logging.info("Counting the number of station bewteen Paris and Lyon: start")     

    def number_station(self): 
        journeys = self.lyon_raw_data["journeys"]
        my_sections = journeys[0]["sections"]
        section_name = my_sections[1]
        self.stops = section_name["stop_date_times"]
        nbr_stations = len(self.stops) - 2
        print(nbr_stations)

    logging.info("Counting the number of station bewteen Paris and Lyon: end")     
    
    logging.info("Saving the list of my stations' names : start")     

    def stops_name(self):
        for stop in self.stops:
            if "stop_point" in stop.keys(): 
                name_station = stop["stop_point"]["label"]
                self.station_paris_lyon.append(name_station)
                #print(stop.keys()) # mes clés de chaque stations entre Paris et Gare de Lyon 'stop_point', 'links', 'arrival_date_time', 'additional_informations', 'departure_date_time', 'base_arrival_date_time', 'base_departure_date_time']
        print(self.station_paris_lyon)
    
    logging.info("Saving the list of my stations' names : end")     

    
    logging.info("Calculating delta of time between arrivals and departures: start")     

    def stops_waiting_time(self): 
        for stop in self.stops: 
            if "base_arrival_date_time" in stop.keys():
                arrival = stop["base_arrival_date_time"]
                arrival_time = datetime.datetime.strptime(arrival, "%Y%m%dT%H%M%S")
                #print(arrival_time)

            if "base_departure_date_time" in stop.keys():
                departure = stop["base_departure_date_time"]
                departure_time = datetime.datetime.strptime(departure,"%Y%m%dT%H%M%S")
                #print(departure_time)
        
            stop_time = (departure_time - arrival_time)
            print(stop_time)

    logging.info("Calculating delta of time between arrivals and departures: ends")     

my_class = ReadingSncfApi() #j'instancie pour pouvoir appeler une fonction de ma classe plus proprement 
#my_class.read_links("stop_areas_tiph.json")
#my_class.my_id('id')
#my_class.my_name('label')
#my_class.my_coord('coord') #je mets pas de self, je suis à l'extérieur de ma classe fonction, je mets dans mes parenthèses mon argument 
#my_class.csv_convert_info('Mon_csv.csv')
#my_class.lyon_read_json()
#my_class.number_station()
#my_class.stops_name()
#my_class.stops_waiting_time()