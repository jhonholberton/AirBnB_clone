#!/usr/bin/python3
"""
Test cases for the place class
"""

from models.base_model import BaseModel
from models.place import Place
import unittest


class Testplace(unittest.TestCase):
    """
        unitesst for place class
    """

    def issub_class(self):
        """
            test if place class is sub class of base model
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "update_at"))

    def test_name(self):
        """
            test class attribute name
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
    
    def test_city_id(self):
        """
            test class attribute city_id
        """
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
    
    def test_user_id(self):
        """
            test class attribute user_id
        """
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        
    def test_description(self):
        """
            test class attribute description
        """
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        
    def test_number_rooms(self):
        """
            test class attribute number_rooms
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        
    def test_number_bathrooms(self):
        """
            test class attribute number_bathrooms
        """
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        
    def test_max_guest(self):
        """
            test class attribute max_guest
        """
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        
    def test_price_by_night(self):
        """
            test class attribute price_by_night
        """
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        
    def test_latitude(self):
        """
            test class attribute latitude
        """
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        
    def test_longitude(self):
        """
            test class attribute longitude
        """
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        
    def test_amenity_ids(self):
        """
            test class attribute amenity_ids
        """
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])
        

    def test_to_dictPlace(self):
        """
            test to dict method with place and the type
            and content
        """
        place = Place()
        dict_cont = place.to_dict()
        self.assertEqual(type(dict_cont), dict)
        for attr in place.__dict__:
            self.assertTrue(attr in dict_cont)
            self.assertTrue("__class__" in dict_cont)

    def test_dict_value(self):
        """
            test the returned dictionar values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        dict_con = place.to_dict()
        self.assertEqual(dict_con["__class__"], "Place")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
            dict_con["created_at"],
            place.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_con["updated_at"],
            place.updated_at.strftime(time_format))


if __name__ == "__main__":
    unittest.main()
