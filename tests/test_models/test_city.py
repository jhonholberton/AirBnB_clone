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


if __name__ == '__main__':
    unittest.main()
