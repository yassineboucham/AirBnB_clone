#!/usr/bin/python3

"""

The module defines a BaseModel class that will be
a template for other classes in a software system

"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self):
        """init"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """return this format: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}"\
            .format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """save the apdate"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to_dict"""
        dictt = {**self.__dict__}
        dictt["__class__"] = BaseModel.__name__
        dictt["created_at"] = dictt["created_at"].isoformat()
        dictt["updated_at"] = dictt["updated_at"].isoformat()
        return dictt
