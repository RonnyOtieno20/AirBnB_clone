#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""

import datetime
import inspect
import models
import pycodestyle
import time
import unittest
from unittest import mock

BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for docstring tests"""
        cls.base_funcs = [func for func in inspect.getmembers(BaseModel, inspect.isfunction)]

    def test_pycodestyle(self):
        """Test pycodestyle conformance"""
        paths = ['models/base_model.py', 'tests/test_models/test_base_model.py']
        for path in paths:
            checker = pycodestyle.Checker(path)
            errors = checker.check_all()
            self.assertEqual(errors, 0, f"Found pycodestyle issues in {path}")

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNotNone(module_doc, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for BaseModel class docstring"""
        self.assertIsNotNone(BaseModel.__doc__, "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1, "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func[0]):
                self.assertIsNotNone(func[1].__doc__, f"{func[0]} method needs a docstring")
                self.assertTrue(len(func[1].__doc__) > 1, f"{func[0]} method needs a docstring")


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    @mock.patch('models.storage')
    def test_instantiation(self, mock_storage):
        """Test object creation"""
        inst = BaseModel()
        self.assertIsInstance(inst, BaseModel)
        inst.name = "Holberton"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime.datetime,
            "updated_at": datetime.datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIsInstance(inst.__dict__[attr], typ)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(inst.name, "Holberton")
        self.assertEqual(inst.number, 89)

    def test_datetime_attributes(self):
        """Test datetime attributes"""
        inst1 = BaseModel()
        time.sleep(1e-4)
        inst2 = BaseModel()
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_uuid(self):
        """Test UUID validity"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        for inst in [inst1, inst2]:
            with self.subTest(uuid=inst.id):
                self.assertIsInstance(inst.id, str)
                self.assertRegex(inst.id, uuid_pattern)
        self.assertNotEqual(inst1.id, inst2.id)

    def test_to_dict(self):
        """Test conversion to dictionary"""
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        model_dict = model.to_dict()
        expected_attrs = ["id", "created_at", "updated_at", "name", "my_number", "__class__"]
        self.assertCountEqual(model_dict.keys(), expected_attrs)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "Holberton")
        self.assertEqual(model_dict['my_number'], 89)

    def test_to_dict_values(self):
        """Test values in dictionary"""
        bm = BaseModel()
        new_dict = bm.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertEqual(new_dict["created_at"], bm.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(new_dict["updated_at"], bm.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

    def test_str(self):
        """Test __str__ method"""
        inst = BaseModel()
        string = f"[BaseModel] ({inst.id}) {inst.__dict__}"
        self.assertEqual(str(inst), string)

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test save method"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.save.called)
