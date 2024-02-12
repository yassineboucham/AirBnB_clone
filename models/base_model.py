#!/usr/bin/python3
"""

models/base_model.py

"""
import uuid
from datetime import datetime

class BaseModel:
    """ Base Model """

    def __init__(self):
        """init"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str"""
        print("[{}] ({}) {}").format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict"""
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
