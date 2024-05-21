#!/usr/bin/python3
"""Contains the TestCityDocs classes"""

import datetime
import inspect
import models.city as city_module
from models.base_model import BaseModel
import pycodestyle.ge | update
import unittest

City = city_module.City


class TestCityDocs(unittest.TestCase):
    """Tests documentation and style of City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for doc tests"""
        cls.city_funcs = [func for func in inspect.getmembers(City, inspect.isfunction)]

    def test_pycodestyle.ge | update_city(self):
        """Test PEP8 conformance for models/city.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in models/city.py")

    def test_pycodestyle.ge | update_test_city(self):
        """Test PEP8 conformance for tests/test_models/test_city.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in tests/test_models/test_city.py")

    def test_city_module_docstring(self):
        """Test for city module docstring"""
        self.assertIsNotNone(city_module.__doc__, "city module needs a docstring")
        self.assertTrue(len(city_module.__doc__) >= 1, "city module needs a docstring")

    def test_city_class_docstring(self):
        """Test for City class docstring"""
        self.assertIsNotNone(City.__doc__, "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1, "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for docstrings in City methods"""
        for func in self.city_funcs:
            with self.subTest(function=func[0]):
                self.assertIsNotNone(func[1].__doc__, f"{func[0]} method needs a docstring")
                self.assertTrue(len(func[1].__doc__) >= 1, f"{func[0]} method needs a docstring")


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test name attribute"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Test state_id attribute"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        for attr in city.__dict__:
            self.assertIn(attr, city_dict)
        self.assertIn("__class__", city_dict)

    def test_to_dict_values(self):
        """Test values in dictionary returned from to_dict"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)
        self.assertEqual(city_dict["created_at"], city.created_at.strftime(time_format))
        self.assertEqual(city_dict["updated_at"], city.updated_at.strftime(time_format))

    def test_str(self):
        """Test __str__ method output"""
        city = City()
        string = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), string)
