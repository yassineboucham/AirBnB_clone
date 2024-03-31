#!/usr/bin/python3

"""

The module defines a BaseModel class that will be

"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The base class that other classes will inheret from
    Args:
        id: A string that is assigned a unique identifier
        created_at: datetime of the created insetance
        updated_at: datetime of the created insetance, it will be updated
    """
    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def save(self):
        """Update the updated time to the current"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return dictionary representaion of the object"""
        dict_clone = {**self.__dict__}
        dict_clone['created_at'] = dict_clone["created_at"].isoformat()
        dict_clone['updated_at'] = dict_clone['updated_at'].isoformat()
        dict_clone["__class__"] = type(self).__name__
        return dict_clone

    def __str__(self):
        """Friendly string representaion of object"""
        str_format = (type(self).__name__, self.id, self.__dict__)
        return "[{}] ({}) {}".format(*str_format)