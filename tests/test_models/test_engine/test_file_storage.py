#!/usr/bin/python3
""" Module with Unittest for the FileStorage class.
    """
import inspect
import unittest
import os

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """ Testing the FileStorage class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.b = FileStorage()
        self.file = storage._FileStorage__file_path
        self.b.save()
        self.storage = FileStorage()
    
    def test_new(self):
        """Test for the method new()"""
        self.assertIn('new', dir(self.b))

    def test_all(self):
        """Test for the method all()"""
        self.assertIn('all', dir(self.b))
        self.assertIsInstance(self.b, FileStorage)
        dictt = self.storage.all()
        self.assertEqual(type(dictt), dict)

    def test_module_documentation(self):
        """ Test if FileStorage module is documented.
            """
        self.assertTrue(FileStorage.__doc__)

    def test_class_documentation(self):
        """ Test if FileStorage class is documented.
            """
        self.assertTrue(FileStorage.__doc__)

    def test_methods_documentation(self):
        """ Test if all FileStorage methods are documented.
            """
        methods = inspect.getmembers(FileStorage)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic FileStorage instances.
            """
        self.assertIsInstance(self.b, FileStorage)

    def test_save_method(self):
        """ Check the save() method.
            """
        b1 = BaseModel()
        self.b.new(b1)
        self.b.save()
        self.assertIn('save', dir(self.b))
        self.b.save()
        self.assertTrue(os.path.isfile(self.file))

    def test_reload_method(self):
        """ Check the reload() method.
            """
        b1 = BaseModel()
        self.b.new(b1)
        self.b.save()
        key_to_search = "BaseModel.{}".format(b1.id)
        self.b.reload()
        file_dict = self.b.all()
        self.assertTrue(key_to_search in file_dict.keys())
