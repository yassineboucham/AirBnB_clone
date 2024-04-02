#!/usr/bin/python3
"""
Defines the BaseModel class.

"""


import json


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        objs = FileStorage.__objects
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        objs[key] = obj

    def save(self):
        with open(self.__file_path, "w") as jsonf:
            json.dump(self.__objects, jsonf)

    def reload(self):
        try:
            with open(self.__file_path, "r") as jsonf:
                self.__objects = json.load(jsonf).items()
        except Exception:
            return
