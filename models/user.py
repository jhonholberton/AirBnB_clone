#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseModel"""
    email = str()
    password = str()
    first_name = str()
    last_name = str()
