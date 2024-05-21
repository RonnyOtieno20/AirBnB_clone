##!/usr/bin/python3
"""Contains the TestPlaceDocs classes"""

import datetime
import inspect
import models.place as place_module
from models.base_model import BaseModel
import pycodestyle.ge | update
import unittest

Place = place_module.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests documentation and style of Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for doc tests"""
        cls.place_funcs = [func for func in inspect.getmembers(Place, inspect.isfunction)]

    def test_pycodestyle.ge | update_place(self):
        """Test PEP8 conformance for models/place.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in models/place.py")

    def test_pycodestyle.ge | update_test_place(self):
        """Test PEP8 conformance for tests/test_models/test_place.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in tests/test_models/test_place.py")

    def test_place_module_docstring(self):
        """Test for place module docstring"""
        self.assertIsNotNone(place_module.__doc__, "place module needs a docstring")
        self.assertTrue(len(place_module.__doc__) >= 1, "place module needs a docstring")

    def test_place_class_docstring(self):
        """Test for Place class docstring"""
        self.assertIsNotNone(Place.__doc__, "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1, "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """Test for docstrings in Place methods"""
        for func in self.place_funcs:
            with self.subTest(function=func[0]):
                self.assertIsNotNone(func[1].__doc__, f"{func[0]} method needs a docstring")
                self.assertTrue(len(func[1].__doc__) >= 1, f"{func[0]} method needs a docstring")


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_city_id_attr(self):
        """Test city_id attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """Test user_id attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_name_attr(self):
        """Test name attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_description_attr(self):
        """Test description attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_rooms_attr(self):
        """Test number_rooms attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertIsInstance(place.number_rooms, int)
        self.assertEqual(place.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test number_bathrooms attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test max_guest attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertIsInstance(place.max_guest, int)
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test price_by_night attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertIsInstance(place.price_by_night, int)
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """Test latitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertIsInstance(place.latitude, float)
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_attr(self):
        """Test longitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertIsInstance(place.longitude, float)
        self.assertEqual(place.longitude, 0.0)

    def test_amenity_ids_attr(self):
        """Test amenity_ids attribute"""
        place = Place()
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertIsInstance(place.amenity_ids, list)
        self.assertEqual(len(place.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        for attr in place.__dict__:
            self.assertIn(attr, place_dict)
        self.assertIn("__class__", place_dict)

    def test_to_dict_values(self):
        """Test values in dictionary returned from to_dict"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)
        self.assertEqual(place_dict["created_at"], place.created_at.strftime(time_format))
        self.assertEqual(place_dict["updated_at"], place.updated_at.strftime(time_format))

    def test_str(self):
        """Test __str__ method output"""
        place = Place()
        string = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), string)
