#!/usr/bin/python3
""" Import unittest and created a class for unit test """
import os
from datetime import datetime
import unittest
from models.base_model import BaseModel
import models.base_model
from models.engine.file_storage import FileStorage
import models


class TestStorageDocumentation(unittest.TestCase):
    """ Create a tests for the file storage in documentation
    and requirements """

    def test_shebang(self):
        """ Test shebang in the front line """
        with open("models/engine/file_storage.py", mode='r') as _file:
            readShebang = _file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_shebang_test(self):
        """ Test shebang in the front line in test file """
        with open("tests/test_models/test_engine/test_file_storage.py", mode='r') as file:
            readShebang = file.read()
            lines = readShebang.splitlines()
            self.assertEqual(lines[0], '#!/usr/bin/python3')

    def test_module_doc(self):
        """ Module with sufficient documentation """
        self.assertTrue(len(models.engine.file_storage.__doc__) != 0)

    def test_class_doc(self):
        """ Class with sufficient documentation """
        self.assertTrue(len(FileStorage.__doc__) != 0)

    def test_methods_doc(self):
        """ Methods with sufficient documentation """
        self.assertTrue(len(FileStorage.all.__doc__) != 0)
        self.assertTrue(len(FileStorage.new.__doc__) != 0)
        self.assertTrue(len(FileStorage.save.__doc__) != 0)
        self.assertTrue(len(FileStorage.reload.__doc__) != 0)


class TestStorage(unittest.TestCase):
    """ Create a tests for the file storage in edge cases """

    def test_all(self):
        """ Check that method returns the dictionary __objects """
        object = models.storage.all()
        self.assertIsInstance(object, dict)

    def test_new(self):
        """ Check that method sets in __objects the obj with key
            <obj class name>.id """
        pass


    def test_reload(self):
        """ Deserialize the JSON file to __objects """
        pass
