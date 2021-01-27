import unittest
import os 
from CSV import ReadingSncfApi  #*importe tout 

class Testing_reading_json(unittest.TestCase):
        def test_reading(self):
            testClass = ReadingSncfApi() #je crée une classe 
            testClass.read_json('stop_areas.json') #j'appelle la fonction de ma classe 
            self.assertTrue(os.path.exists('stop_areas.json'))
        def test_read_links(self):
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')
            self.assertTrue(os.path.exists('stop_areas_tiph.json'))

        def test_loop_links(self):
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')
            testClass.loop_links('href')
            self.assertTrue(type(testClass.liste_links) == list)

        def test_my_id(self): 
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')
            testClass.my_id("id")
            self.assertTrue(type(testClass.liste_id) == list)

        def test_my_name(self): 
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')      
            testClass.my_name("label")
            self.assertTrue(type(testClass.liste_names) == list)     

        def test_my_coord(self):
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')   
            testClass.my_coord("coord")
            self.assertTrue(type(testClass.liste_coord) == list)

        def test_id_list_full(self):
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')
            testClass.my_id("id")
            self.assertTrue(len(testClass.liste_id) > 0)
        
        def test_name_list_full(self): 
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')      
            testClass.my_name("label")
            self.assertTrue(len(testClass.liste_names) > 0)

        def test_coord_list_full(self): 
            testClass = ReadingSncfApi()
            testClass.read_links('stop_areas_tiph.json')   
            testClass.my_coord("coord")
            self.assertTrue(len(testClass.liste_coord) > 0)
            
        def test_create_csv(self): 
            testClass = ReadingSncfApi()
            testClass.read_links("stop_areas_tiph.json")
            testClass.my_id('id')
            testClass.my_name('label')
            testClass.my_coord('coord')
            testClass.csv_convert_info('Mon_csv.csv')
            my_boolean = (len(testClass.liste_id) > 0) and (len(testClass.liste_names) >0) and (len(testClass.liste_coord)> 0)
            self.assertTrue(my_boolean)
            self.assertTrue(os.path.exists('mon_csv.csv'))

            #compiler existence des 3 listes

if __name__ == '__main__':
    unittest.main(verbosity =0)
