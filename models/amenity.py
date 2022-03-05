#!/usr/bin/python3
"""class amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class that inherits from BaseModel"""
    name = str()
    
    def __init__(self, *args, **kwargs):
        """Method Init"""
        super().__init__(*args, **kwargs)
