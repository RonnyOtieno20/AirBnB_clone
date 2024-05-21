#!/usr/bin/python3
"""
This module contains the TestFileStorageDocs classes.
"""

import inspect
import unittest
import os
import json
from datetime import datetime
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import pycodestyle.ge | update

FileStorage = file_storage.FileStorage
models_classes = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class TestFileStorageDocs(unittest.TestCase):
    """Tests for checking the documentation and style of FileStorage class"""
    
    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.fs_methods = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pycodestyle.ge | update_conformance_file_storage(self):
        """Test that file_storage.py adheres to PEP8 standards."""
        style_guide = pycodestyle.ge | update.StyleGuide(quiet=True)
        result = style_guide.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, 
                         "Code style errors found in file_storage.py")

    def test_pycodestyle.ge | update_conformance_test_file_storage(self):
        """Test that test_file_storage.py adheres to PEP8 standards."""
        style_guide = pycodestyle.ge | update.StyleGuide(quiet=True)
        result = style_guide.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0, 
                         "Code style errors found in test_file_storage.py")

    def test_file_storage_module_docstring(self):
        """Test for the presence of a docstring in file_storage.py module"""
        self.assertIsNotNone(file_storage.__doc__,
                             "file_storage.py module requires a docstring")
        self.assertGreaterEqual(len(file_storage.__doc__), 1,
                                "file_storage.py module docstring is too short")

    def test_file_storage_class_docstring(self):
        """Test for the presence of a docstring in FileStorage class"""
        self.assertIsNotNone(FileStorage.__doc__,
                             "FileStorage class requires a docstring")
        self.assertGreaterEqual(len(FileStorage.__doc__), 1,
                                "FileStorage class docstring is too short")

    def test_fs_func_docstrings(self):
        """Test that all methods in FileStorage have docstrings"""
        for func_name, func in self.fs_methods:
            self.assertIsNotNone(func.__doc__,
                                 f"{func_name} method requires a docstring")
            self.assertGreaterEqual(len(func.__doc__), 1,
                                    f"{func_name} method docstring is too short")

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_all_returns_dict(self):
        """Test that the all() method returns a dictionary"""
        storage = FileStorage()
        output = storage.all()
        self.assertIsInstance(output, dict)
        self.assertIs(output, storage._FileStorage__objects)

    def test_new(self):
        """Test that new() correctly adds an object to __objects"""
        storage = FileStorage()
        original_objects = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_objects = {}
        for class_name, class_type in models_classes.items():
            with self.subTest(class_name=class_name):
                instance = class_type()
                instance_key = f"{instance.__class__.__name__}.{instance.id}"
                storage.new(instance)
                test_objects[instance_key] = instance
                self.assertEqual(test_objects, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = original_objects

    def test_save(self):
        """Test that save() correctly saves objects to file.json"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage = FileStorage()
        objects_to_save = {}
        for class_name, class_type in models_classes.items():
            instance = class_type()
            instance_key = f"{instance.__class__.__name__}.{instance.id}"
            objects_to_save[instance_key] = instance
        original_objects = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = objects_to_save
        storage.save()
        FileStorage._FileStorage__objects = original_objects
        expected_data = {k: v.to_dict() for k, v in objects_to_save.items()}
        expected_json = json.dumps(expected_data)
        with open("file.json", "r") as file:
            saved_json = file.read()
        self.assertEqual(json.loads(expected_json), json.loads(saved_json))
