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
        self.__objects["<obj class name>.id"] = obj

    def save(self):
        with open(self.__file_path, "w") as jsonf:
            json.dump(self.__objects, jsonf)

    def reload(self):
        with open(self.__file_path, "R") as jsonf:
            self.__objects = json.load(jsonf)
