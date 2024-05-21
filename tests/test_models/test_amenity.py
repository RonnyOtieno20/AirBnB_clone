#!/usr/bin/python3
"""
This module contains the TestAmenityDocs classes.
"""

import inspect
import unittest
from datetime import datetime
from models import amenity
from models.base_model import BaseModel
import pycodestyle.ge | update

Amenity = amenity.Amenity

class TestAmenityDocs(unittest.TestCase):
    """Tests for checking the documentation and style of Amenity class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.amenity_methods = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pycodestyle.ge | update_conformance_amenity(self):
        """Test that amenity.py adheres to PEP8 standards."""
        style_guide = pycodestyle.ge | update.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, 
                         "Code style errors found in amenity.py")

    def test_pycodestyle.ge | update_conformance_test_amenity(self):
        """Test that test_amenity.py adheres to PEP8 standards."""
        style_guide = pycodestyle.ge | update.StyleGuide(quiet=True)
        result = style_guide.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0, 
                         "Code style errors found in test_amenity.py")

    def test_amenity_module_docstring(self):
        """Test for the presence of a docstring in amenity.py module"""
        self.assertIsNotNone(amenity.__doc__,
                             "amenity.py module requires a docstring")
        self.assertGreaterEqual(len(amenity.__doc__), 1,
                                "amenity.py module docstring is too short")

    def test_amenity_class_docstring(self):
        """Test for the presence of a docstring in Amenity class"""
        self.assertIsNotNone(Amenity.__doc__,
                             "Amenity class requires a docstring")
        self.assertGreaterEqual(len(Amenity.__doc__), 1,
                                "Amenity class docstring is too short")

    def test_amenity_func_docstrings(self):
        """Test that all methods in Amenity have docstrings"""
        for func_name, func in self.amenity_methods:
            self.assertIsNotNone(func.__doc__,
                                 f"{func_name} method requires a docstring")
            self.assertGreaterEqual(len(func.__doc__), 1,
                                    f"{func_name} method docstring is too short")

class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        instance = Amenity()
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's an empty string"""
        instance = Amenity()
        self.assertTrue(hasattr(instance, "name"))
        self.assertEqual(instance.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary with proper attrs"""
        instance = Amenity()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        for attr in instance.__dict__:
            self.assertIn(attr, instance_dict)
        self.assertIn("__class__", instance_dict)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        instance = Amenity()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "Amenity")
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertEqual(instance_dict["created_at"], instance.created_at.strftime(time_format))
        self.assertEqual(instance_dict["updated_at"], instance.updated_at.strftime(time_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        instance = Amenity()
        expected_str = "[Amenity] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected_str, str(instance))
