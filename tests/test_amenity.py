#!/usr/bin/python3

"""All the test for the amenity model are implemented"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity class"""

    def test_Amenity_inheritance(self):
        """ tests that the Amenity Inherits from BaseModel"""
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_Amenity_attributes(self):
        """Test that the calass of Amenity had a name attribute"""
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_Amenity_attributes_Type(self):
        """Test that Amenity class had a name attribute'type"""
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)

    def setUp(self):
        """Setup the unit tests"""
        self.obj1 = Amenity()
        self.obj2 = Amenity()
        self.obj3 = Amenity()
        self.obj4 = Amenity()
        self.obj11 = Amenity(**self.obj1.to_dict())
        self.obj22 = Amenity(**self.obj2.to_dict())
        self.obj33 = Amenity(**self.obj3.to_dict())

    def test_init(self):
        """Test initialization without kwargs"""
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)
        self.assertNotEqual(self.obj1.id, self.obj2.id)
        self.assertNotEqual(self.obj3.id, self.obj4.id)
        self.assertEqual(self.obj1.__class__.__name__, "Amenity")

    def test_id_uniqueness(self):
        """Check if id is always universal unique"""
        alot_of_ids = [Amenity().id for i in range(1000)]
        self.assertEqual(len(set(alot_of_ids)), 1000)

    def test_types(self):
        """Test the properties types"""
        self.assertIsInstance(self.obj1, Amenity)
        self.assertIsInstance(self.obj11, Amenity)
        self.assertIsInstance(self.obj33.id, str)

    def test_init_kwargs(self):
        """Test initialization with kwargs"""
        self.assertIsInstance(self.obj11.id, str)
        self.assertIsInstance(self.obj11.created_at, datetime)
        self.assertIsInstance(self.obj11.updated_at, datetime)
        self.assertEqual(self.obj2.id, self.obj22.id)
        self.assertEqual(self.obj3.updated_at, self.obj33.updated_at)
        self.assertEqual(self.obj3.created_at, self.obj33.created_at)
        self.assertEqual(self.obj11.__class__.__name__, "Amenity")

    def test_init_args(self):
        """The case where args are given"""
        args = [i for i in range(20)]
        obj = Amenity(*args)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict(self):
        """Test the to_dict method"""
        returned_dict = self.obj2.to_dict()
        self.assertEqual(returned_dict["__class__"], "Amenity")
        self.assertIsInstance(returned_dict["created_at"], str)
        self.assertIsInstance(returned_dict["updated_at"], str)
        self.assertEqual(len(self.obj22.to_dict()), 4)
        self.assertIsInstance(returned_dict, dict)
        self.assertDictEqual(self.obj33.to_dict(), self.obj33.to_dict())

    def test_save(self):
        """Test the save method"""
        before_save = self.obj1.updated_at
        before_save_create = self.obj1.created_at
        self.obj1.save()
        after_save_create = self.obj1.created_at
        after_save = self.obj1.updated_at
        self.assertNotEqual(before_save, after_save)
        self.assertEqual(before_save_create, after_save_create)

    def test_str(self):
        """Test the str method"""
        format_str = (self.obj1.id, self.obj1.__dict__)
        str_rep = "[Amenity] ({}) {}".format(*format_str)
        self.assertEqual(str_rep, str(self.obj1))
        format_str = (self.obj2.id, self.obj2.__dict__)
        str_rep = "[Amenity] ({}) {}".format(*format_str)
        self.assertEqual(str_rep, str(self.obj2))
