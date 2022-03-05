#!/usr/bin/python3
"""Module to create files JSON"""

import json


class FileStorage():
    """class to manipulate json file"""
    __file_path = 'file.json'
    __objects = {}

    def path(self):
        """File route"""
        return self.__file_path

    def all(self):
        """returns variable __objects"""
        self.reload()
        return self.__objects

    def new(self, obj):
        """method to create key and dictionary"""
        self.obj = obj
        self.key = type(obj).__name__ + '.' + str(obj.id)
        self.__objects[self.key] = obj

    def save(self):
        """method to save changes in the json file"""
        for k, v in self.__objects.items():
            if type(v) is not dict:
                self.__objects[k] = v.to_dict()
        with open(self.__file_path, "w") as my_file:
            json.dump(self.__objects, my_file)

    def reload(self):
        """method to update variable __objec"""
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User
        try:
            with open(self.__file_path, "r") as my_file:
                my_dic_json = json.load(my_file)
                for k in my_dic_json.keys():
                    my_class = my_dic_json[k]['__class__']
                    self.__objects[k] = eval(my_class)(**my_dic_json[k])
        except Exception:
            self.__objects = {}
