#!/usr/bin/python3
"""Defines the BaseModel class."""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self):
        """init"""
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """save the apdate"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """to_dict"""
        dictt = self.__dict__.copy()
        dictt["created_at"] = dictt["created_at"].isoformat()
        dictt["updated_at"] = dictt["updated_at"].isoformat()
        dictt["__class__"] = BaseModel.__name__
        return dictt

    def __str__(self):
        """return this format: [<class name>] (<self.id>) <self.__dict__>"""
        name = BaseModel.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
