#!/usr/bin/python3
"""
Test cases for the city class
"""

from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
        unitesst for city class
    """

    def issub_class(self):
        """
            test if city class is sub class of base model
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "update_at"))

    def test_name(self):
        """
            test class attribute name
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
    
    def test_state_id(self):
        """
            test class attribute state_id
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        

    def test_to_dictcity(self):
        """
            test to dict method with city and the type
            and content
        """
        city = City()
        dict_cont = city.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in city.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        dict_con = city.to_dict()
        self.assertEqual(dict_con["__class__"], "City")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            city.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            city.updated_at.strftime(time_format))


if __name__ == "__main__":
    unittest.main()
