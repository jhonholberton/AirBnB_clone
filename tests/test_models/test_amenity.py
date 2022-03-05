#!/usr/bin/python3
"""Unit test for the module Amenity"""

import unittest
from models.amenity import Amenity
from models import storage


class Test_Amenity(unittest.TestCase):
    """Test for the class Amenity"""
    instancia = Amenity()
    instancia.name = 'pepe2'

    data_base = storage.all()
    instancia_nombre = 'Amenity.' + instancia.id

    def test_amenityinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instancia_nombre).to_dict()
        clase_a = "<class 'models.amenity.Amenity'>"
        tiempo = "<class 'datetime.datetime'>"

        # Data types
        self.assertEqual(str(type(self.instancia)), clase_a)
        self.assertEqual(str(type(self.instancia.id)), "<class 'str'>")
        self.assertEqual(str(type(self.instancia.created_at)), tiempo)
        self.assertEqual(str(type(self.instancia.updated_at)), tiempo)

        # Basic features storage
        self.assertIn(self.instancia_nombre, self.data_base.keys())
        self.assertIn('created_at', features.keys())
        self.assertIn('updated_at', features.keys())
        self.assertIn('id', features.keys())
        self.assertIn('name', features.keys())

        test_dict = {"id": "a693d0ab-14d0-496b-b5db-02e4a7516d4e",
                     "created_at": "2022-03-04T15:08:52.299424",
                     "updated_at": "2022-03-04T15:08:52.300076",
                     "__class__": "Amenity",
                     "name": "pepe"}
        instance2 = Amenity(**test_dict)
        self.assertIsInstance(instance2, Amenity)
        self.assertEqual(instance2.id, "a693d0ab-14d0-496b-b5db-02e4a7516d4e")
        self.assertEqual(instance2.name, "pepe")

    def test_amenitysave(self):
        """Test for the method save"""
        dato_update = self.instancia.updated_at
        self.instancia.save()
        new_date = self.instancia.updated_at
        self.assertNotEqual(dato_update, new_date)

    def test_amenitytodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instancia.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instancia_nombre, self.data_base.keys())


if __name__ == '__main__':
    unittest.main()
