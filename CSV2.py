#!/usr/bin/env python 
# coding=utf-8
    
import pprint
import json
import requests
import pandas as pd

station_paris_lyon = []

url_lyon = "https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025"
headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
url_stop_request = requests.get(url = url_lyon, headers=headers)
stop_raw_data = json.loads(url_stop_request.text)

#pprint.pprint(stop_raw_data)
#print(url_stop_request.json())
#print(type(stop_raw_data)) # a dict

#print(stop_raw_data.keys())

journeys = stop_raw_data["journeys"]

#pprint.pprint(journeys) 

#print(type(journeys))#c'est une liste

'''for journey in journeys[0].keys(): 
    print(type(journeys[0][journey]), journey)'''

my_sections = journeys[0]["sections"] #pour aller dans mon element sections dans ma liste Journeys, section est un dictionnaire
#print(type(my_sections)) # my_section est une list

'''for section in my_sections: 
    print(type(section), section) #ici chaque élement de ma liste my_sections est un dictionnaire '''

section_name = my_sections[1] #from', 'links', 'arrival_date_time', 'additional_informations', 'co2_emission', 'display_informations', 'to', 'base_arrival_date_time', 'base_departure_date_time', 'departure_date_time', 'geojson', 'duration', 'type', 'id', 'data_freshness', 'stop_date_times'

#pprint.pprint(section_name["stop_date_times"]) #stop_date_time est une liste 

stops = section_name["stop_date_times"]

#le nombre de stations que j'ai -2 car ils comptabilisent toutes mes gares et je ne veux pas celle de départ ni celle d'arrivée 
nbr_stations = len(stops) - 2
print(nbr_stations)

#avoir toutes mes stations dans une liste 
for stop in stops:
    if "stop_point" in stop.keys(): 
        name_station = stop["stop_point"]["label"]
        station_paris_lyon.append(name_station)
        print(stop.keys()) # mes clés de chaque stations entre Paris et Gare de Lyon 'stop_point', 'links', 'arrival_date_time', 'additional_informations', 'departure_date_time', 'base_arrival_date_time', 'base_departure_date_time']
print(station_paris_lyon)

#Durée d'attente entre chaque arrêt: arrival_date_tim - departure_date_time  > je reste dans ma stops liste 
stations_arrival_time = []
stations_departure_time = []

for stop in stops: 
    if "arrival_date_time" in stop.keys():
        arrival = stop["arrival_date_time"]
        stations_arrival_time.append(arrival)
print(stations_arrival_time)

for stop in stops: 
    if "departure_date_time" in stop.keys():
        departure = stop["departure_date_time"]
        stations_departure_time.append(departure)
print(stations_departure_time)



'''first_station = stops[0]["stop_point"] 
print(first_station["label"])'''


'''<class 'str'> status
<class 'dict'> distances : {'taxi': 0, 'car': 0, 'walking': 0, 'bike': 0, 'ridesharing': 0}
<class 'list'> links
<class 'list'> tags
<class 'int'> nb_transfers
<class 'dict'> durations : {'taxi': 0, 'walking': 0, 'car': 0, 'ridesharing': 0, 'bike': 0, 'total': 8220}
<class 'str'> arrival_date_time
<class 'list'> calendars
<class 'str'> departure_date_time
<class 'str'> requested_date_time
<class 'dict'> fare
<class 'dict'> co2_emission
<class 'str'> type
<class 'int'> duration
<class 'list'> sections :'''

            

'''Rajouter les logs, pour m'informer sur mes potentiels erreurs'''
'''Avoir une structure claire de mon api, mon arbre'''
'''Trouver un format final pour que mon user puisse le lire: fichier texte ? json? '''