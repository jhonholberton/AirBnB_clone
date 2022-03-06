#!/usr/bin/python3
""" Module with Unittest for the FileStorage class.
    """
import inspect
import unittest
import os

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestBaseModel(unittest.TestCase):
    """ Testing the FileStorage class of the program.
        """

    instance1 = FileStorage()
    file = storage._FileStorage__file_path
    storage = FileStorage()
    b = FileStorage()
    b.save()
    
    def test_all(self):
        """Test for the method all()"""
        self.assertIn('all', dir(self.instance1))
        self.assertIsInstance(self.instance1, FileStorage)
        dictt = storage.all()
        self.assertEqual(type(dictt), dict)

    def test_new(self):
        """Test for the method new()"""
        self.assertIn('new', dir(self.instance1))

    def test_save_method(self):
        """ Check the save() method.
            """
        b1 = BaseModel()
        self.b.new(b1)
        self.b.save()
        self.assertIn('save', dir(self.b))
        self.b.save()
        self.assertTrue(os.path.isfile(self.file))
        
    def test_save2(self):
        '''Test saving a instances of each type'''
        base = BaseModel()
        storage.new(base)

        user = User()
        storage.new(user)

        state = State()
        storage.new(state)

        place = Place()
        storage.new(place)

        city = City()
        storage.new(city)

        amenity = Amenity()
        storage.new(amenity)

        review = Review()
        storage.new(review)

        storage.save()

        with open(self.file) as f:
            string = f.read()
            self.assertIn("BaseModel." + base.id, string)
            self.assertIn("User." + user.id, string)
            self.assertIn("State." + state.id, string)
            self.assertIn("Place." + place.id, string)
            self.assertIn("City." + city.id, string)
            self.assertIn("Amenity." + amenity.id, string)
            self.assertIn("Review." + review.id, string)

    def test_reload(self):
        """Test for the method reload()"""
        self.assertIn('reload', dir(self.instance1))
        objects = storage.all()
        base = BaseModel()
        storage.save()
        storage.reload()
        key_to_search = "BaseModel.{}".format(base.id)
        self.assertIn("BaseModel." + base.id, objects.keys())
        self.assertTrue(key_to_search in objects.keys())

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
        
    def test_path_method(self):
        """Check path method"""
        self.assertIn('path', dir(self.instance1))
        self.assertIsInstance(self.instance1, FileStorage)
        cad = storage.path()
        self.assertEqual(type(cad), str)


if __name__ == '__main__':
    unittest.main()
