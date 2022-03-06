#!/usr/bin/python3
# File: test_file_storage.py
# Authors: Imanol Asolo - Alex Arévalo
# email(s): <3848@holbertonschool.com>
#           <3915@holbertonschool.com>

"""
This Module Defines Unittest for models/engine/file_storage.py.
"""

import os
import json
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
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        us = User()
        pl = Place()
        st = State()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.save()
        models.storage.reload()
        key = models.storage.all().keys()
        val = models.storage.all().values()
        self.assertIn("BaseModel." + bm.id, key)
        self.assertIn("User." + us.id, key)
        self.assertIn("Place." + pl.id, key)
        self.assertIn("State." + st.id, key)
        self.assertIn("City." + ct.id, key)
        self.assertIn("Amenity." + am.id, key)
        self.assertIn("Review." + rv.id, key)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        bm = BaseModel()
        us = User()
        pl = Place()
        st = State()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(pl)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + bm.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("City." + ct.id, save_text)
            self.assertIn("Amenity." + am.id, save_text)
            self.assertIn("Review." + rv.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        us = User()
        pl = Place()
        st = State()
        ct = City()
        am = Amenity()
        rv = Review()
        models.storage.new(bm)
        models.storage.new(us)
        models.storage.new(pl)
        models.storage.new(st)
        models.storage.new(ct)
        models.storage.new(am)
        models.storage.new(rv)
        models.storage.save()
        models.storage.reload()
        obj = models.storage.all()
        self.assertIn("BaseModel." + bm.id, obj)
        self.assertIn("User." + us.id, obj)
        self.assertIn("Place." + pl.id, obj)
        self.assertIn("State." + st.id, obj)
        self.assertIn("City." + ct.id, obj)
        self.assertIn("Amenity." + am.id, obj)
        self.assertIn("Review." + rv.id, obj)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
