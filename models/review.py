#!/usr/bin/python3
"""class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherits from BaseModel"""
    place_id = str()
    user_id = str()
    text = str()
