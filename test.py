import unittest
import os 
from CSV import ReadingSncfApi  #*importe tout 

class Testing_reading_json(unittest.TestCase):
        def test_reading(self):
            testClass = ReadingSncfApi() #je crée une classe 
            testClass.read_json('stop_areas_tiph.json') #j'appelle la fonction de ma classe 
            self.assertTrue(os.path.exists('stop_areas_tiph.json'))

if __name__ == '__main__':
    unittest.main(verbosity =0)
