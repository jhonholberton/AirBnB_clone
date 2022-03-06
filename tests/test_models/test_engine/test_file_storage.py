#!/usr/bin/python3
"""
This Module Defines Unittest for models/engine/file_storage.py.
"""

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """
    Unittests for testing methods of the FileStorage class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_path(self):
        self.assertEqual(str, type(models.storage.path()))

    def test_all(self):
        ob = FileStorage()
        my_dict = ob.all()
        self.assertEqual(dict, type(my_dict))
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        b = BaseModel()
        models.storage.new(b)
        models.storage.save()
        objects_dict = models.storage.all()
        keys = objects_dict.keys()
        b_key = "BaseModel." + b.id
        self.assertTrue(b_key in keys)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        """Check save method."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        c_date = '2017-09-28T21:05:54.119427'
        u_date = '2017-09-28T21:05:54.119572'
        id_val = "b_save"

        b = BaseModel(id=id_val, created_at=c_date, updated_at=u_date,)
        models.storage.new(b)
        models.storage.save()

        objects_dict = models.storage.all()
        keys = objects_dict.keys()
        b_key = "BaseModel." + b.id
        b_dict = b.to_dict()

        with open("file.json", "r") as file:
            json_text = file.read()
        json_dict = eval(json_text)
        self.assertTrue(b_key in json_dict.keys())
        self.assertEqual(json_dict[b_key], b_dict)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """ Check the reload() method.
            """
        self.storage_test = FileStorage()
        base_model_test = BaseModel()
        self.storage_test.new(base_model_test)
        self.storage_test.save()
        key_to_search = "BaseModel.{}".format(base_model_test.id)
        self.storage_test.reload()
        file_dict = self.storage_test.all()
        self.assertTrue(key_to_search in file_dict.keys())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
