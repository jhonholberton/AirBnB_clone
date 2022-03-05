#!/usr/bin/python3
"""Unit test for the module User"""

import unittest
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test for the class User"""
    instance = User()
    data_base = storage.all()
    instancia_nombre = 'User.' + instance.id
    instance.first_name = 'Pepe'
    instance.email = "pepeprogramador@holberton.com"
    instance.password = "pepeproblemas21"
    instance.first_name = "Andres"
    instance.last_name = "Pardo"

    def test_userinit(self):
        """Test for the method __init__"""
        features = self.data_base.get(self.instancia_nombre).to_dict()
        clase_u = "<class 'models.user.User'>"
        tiempo = "<class 'datetime.datetime'>"

        # Data types
        self.assertEqual(str(type(self.instance)), clase_u)
        self.assertEqual(str(type(self.instance.id)), "<class 'str'>")
        self.assertEqual(str(type(self.instance.created_at)), tiempo)
        self.assertEqual(str(type(self.instance.updated_at)), tiempo)

        # Basic features storage
        self.assertIn(self.instancia_nombre, self.data_base.keys())
        self.assertIn('created_at', features.keys())
        self.assertIn('updated_at', features.keys())
        self.assertIn('id', features.keys())
        self.assertIn('first_name', features.keys())
        self.assertIn('email', features.keys())
        self.assertIn('password', features.keys())
        self.assertIn('first_name', features.keys())
        self.assertIn('last_name', features.keys())

        test_dict = {"id": "cccef82a-6597-4249-9a09-bf8d5a8491c0",
                     "created_at": "2022-03-04T19:29:11.035622",
                     "updated_at": "2022-03-04T19:29:11.035663",
                     "__class__": "User",
                     "first_name": "Andres",
                     "last_name": "Pardo",
                     "password": "6543210",
                     "email": "Andresprogramador@holberton.com"}
        instance2 = User(**test_dict)
        self.assertTrue(isinstance(instance2, User))
        self.assertEqual(instance2.id, "cccef82a-6597-4249-9a09-bf8d5a8491c0")
        self.assertEqual(instance2.first_name, "Andres")
        self.assertEqual(instance2.last_name, "Pardo")
        self.assertEqual(instance2.email, "Andresprogramador@holberton.com")
        self.assertEqual(instance2.password, "6543210")

    def test_userstr(self):
        """Test for the method __str__"""
        p = '[User] ({}) {}'.format(self.instance.id, self.instance.__dict__)
        my_string = self.instance.__str__()
        self.assertEqual(p, my_string)

    def test_usersave(self):
        """Test for the method save"""
        dateofupdate = self.instance.updated_at
        self.instance.save()
        new_date = self.instance.updated_at
        self.assertNotEqual(dateofupdate, new_date)

    def test_usertodict(self):
        """Test for the method to_dict"""
        type_of_dict = str(type(self.instance.to_dict()))
        self.assertEqual(type_of_dict, "<class 'dict'>")
        self.assertIn(self.instancia_nombre, self.data_base.keys())


if __name__ == '__main__':
    unittest.main()
