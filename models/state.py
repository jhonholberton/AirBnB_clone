#!/usr/bin/python3
"""class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class that inherit from BaseModel"""
    name = str()

    def __init__(self, *args, **kwargs):
        """Method Init"""
        super().__init__(*args, **kwargs)
