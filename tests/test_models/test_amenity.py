#!/usr/bin/python3
"""
Test cases for the Amenity class
"""

from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
        unitesst for amenity class
    """

    def issub_class(self):
        """
            test if amenity class is sub class of base model
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "update_at"))

    def test_name(self):
        """
            test class attribute email
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dictAmenity(self):
        """
            test to dict method with amenity and the type
            and content
        """
        amenity = Amenity()
        dict_cont = amenity.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in amenity.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity = Amenity()
        dict_con = amenity.to_dict()
        self.assertEqual(dict_con["__class__"], "Amenity")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            amenity.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            amenity.updated_at.strftime(time_format))


if __name__ == "__main__":
    unittest.main()
