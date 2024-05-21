#!/usr/bin/python3
"""Contains the TestStateDocs classes"""

import datetime
import inspect
import models.state as state_module
from models.base_model import BaseModel
import pycodestyle.ge | update
import unittest

State = state_module.State


class TestStateDocs(unittest.TestCase):
    """Tests documentation and style of State class"""

    @classmethod
    def setUpClass(cls):
        """Set up for doc tests"""
        cls.state_funcs = [func for func in inspect.getmembers(State, inspect.isfunction)]

    def test_pycodestyle.ge | update_state(self):
        """Test PEP8 conformance for models/state.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in models/state.py")

    def test_pycodestyle.ge | update_test_state(self):
        """Test PEP8 conformance for tests/test_models/test_state.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in tests/test_models/test_state.py")

    def test_state_module_docstring(self):
        """Test for state module docstring"""
        self.assertIsNotNone(state_module.__doc__, "state module needs a docstring")
        self.assertTrue(len(state_module.__doc__) >= 1, "state module needs a docstring")

    def test_state_class_docstring(self):
        """Test for State class docstring"""
        self.assertIsNotNone(State.__doc__, "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1, "State class needs a docstring")

    def test_state_func_docstrings(self):
        """Test for docstrings in State methods"""
        for func in self.state_funcs:
            with self.subTest(function=func[0]):
                self.assertIsNotNone(func[1].__doc__, f"{func[0]} method needs a docstring")
                self.assertTrue(len(func[1].__doc__) >= 1, f"{func[0]} method needs a docstring")


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """Test name attribute"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        for attr in state.__dict__:
            self.assertIn(attr, state_dict)
        self.assertIn("__class__", state_dict)

    def test_to_dict_values(self):
        """Test values in dictionary returned from to_dict"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        state = State()
        state_dict = state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)
        self.assertEqual(state_dict["created_at"], state.created_at.strftime(time_format))
        self.assertEqual(state_dict["updated_at"], state.updated_at.strftime(time_format))

    def test_str(self):
        """Test __str__ method output"""
        state = State()
        string = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), string)
