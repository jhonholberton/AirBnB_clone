#!/usr/bin/python3
"""Model base for all modules and class"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """class baseModel"""

    def __init__(self, *args, **kwargs):
        """method init of class, with instance attributes"""
        if (kwargs):
            for k, v in kwargs.items():
                if k in ('created_at', "updated_at"):
                    self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """return description of class str format"""
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """update atributte updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
            keys/values of __dict__ of the instance
        """
        dic_ret = self.__dict__.copy()
        dic_ret['__class__'] = type(self).__name__
        dic_ret['updated_at'] = str(dic_ret['updated_at'].isoformat())
        dic_ret['created_at'] = str(dic_ret['created_at'].isoformat())
        return dic_ret
