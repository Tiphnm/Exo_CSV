#!/usr/bin/env python 
# coding=utf-8
    
from CSV import *

''' Je navigue ici dans l'API de la SNCF afin d'avoir des informations sur certaines gares et arrêts.
Par-exemple ci dessous je réussis à avoir les informations concernant les stations entre Paris et Lyon: comme les noms, coordoonées 
géographiques ou encore le temps d'arrêt entre chacunes d'elles.'''

my_class = ReadingSncfApi() 
#my_class.read_links("stop_areas_tiph.json") #Lecture de mon fichier Json en pprint pour qu'il soit plus lisible 
#my_class.my_id('id') # Création d'une liste avec l'id de mes arrêts 
#my_class.my_name('label') # Création d'une liste avec le nom de mes arrêts 
#my_class.my_coord('coord') # Création d'une liste avec les coordonnées géographiques de mes arrêts 
#my_class.csv_convert_info('Mon_csv.csv') # Je convertis enfin toutes ces données dans un fichier CSV pour que les infos soient plus lisibles 
my_class.lyon_read_json() # Je lis mon fichier Json uniquement dédié aux gares entre Paris et Lyon
my_class.number_station() #Fontion me permettant d'avoir le nombre de stations entre ces deux gares (varient dans la journée)
#my_class.stops_name() #Fontion me permettant d'avoir le nom de ces chaques gares 
#my_class.stops_waiting_time()# Fonction me permettant d'avoir le temps d'arrêt 