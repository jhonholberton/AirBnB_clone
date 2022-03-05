#!/usr/bin/python3
"""Unit test for the module City"""

import unittest
from models.city import City
from models import storage


class Test_City(unittest.TestCase):
    """Test for the class City"""
    instancia = City()
    instancia.state_id = 'Betty'
    instancia.name = 'Bogota'

    data_base = storage.all()
    instancia_nombre = 'City.' + instancia.id

    def test_cityinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instancia_nombre).to_dict()
        clase_c = "<class 'models.city.City'>"
        tiempo = "<class 'datetime.datetime'>"

        # Data types
        self.assertEqual(str(type(self.instancia)), clase_c)
        self.assertEqual(str(type(self.instancia.id)), "<class 'str'>")
        self.assertEqual(str(type(self.instancia.created_at)), tiempo)
        self.assertEqual(str(type(self.instancia.updated_at)), tiempo)

        # Basic features storage
        self.assertIn(self.instancia_nombre, self.data_base.keys())
        self.assertIn('created_at', features.keys())
        self.assertIn('updated_at', features.keys())
        self.assertIn('id', features.keys())
        self.assertIn('name', features.keys())
        self.assertIn('state_id', features.keys())

        test_dict = {"id": "6d60b737-bb76-4f09-9bad-b7fcd5d8d1ed",
                     "created_at": "2022-03-04T19:26:49.736081",
                     "updated_at": "2022-03-04T19:26:49.737133",
                     "__class__": "City",
                     "state_id": "123",
                     "name": "Paipa"}

        instance2 = City(**test_dict)

        self.assertIsInstance(instance2, City)
        self.assertEqual(instance2.id, "6d60b737-bb76-4f09-9bad-b7fcd5d8d1ed")
        self.assertEqual(instance2.state_id, "123")
        self.assertEqual(instance2.name, "Paipa")

    def test_citysave(self):
        """Test for the method save"""
        dato_update = self.instancia.updated_at
        self.instancia.save()
        new_date = self.instancia.updated_at
        self.assertNotEqual(dato_update, new_date)

    def test_citystr(self):
        """Test for the method __str__"""
        p = '[City] ({}) {}'.format(self.instancia.id, self.instancia.__dict__)
        my_string = self.instancia.__str__()
        self.assertEqual(p, my_string)

    def test_citytodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instancia.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instancia_nombre, self.data_base.keys())


if __name__ == '__main__':
    unittest.main()
