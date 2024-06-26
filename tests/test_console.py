#!/usr/bin/python3
"""Unit tests for the HBNBCommand class"""

import unittest
import json
from unittest.mock import patch
from io import StringIO
import os
import pycodestyle
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment"""
        cls.console = HBNBCommand()
        cls.file_path = "test.json"
        FileStorage._FileStorage__file_path = cls.file_path
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove(cls.file_path)
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """Test for documentation"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.__init__.__doc__)
        for func in dir(HBNBCommand):
            self.assertIsNotNone(getattr(HBNBCommand, func).__doc__)

    def test_pycodestyle_conformance(self):
        """Test for PEP8 conformance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py', 'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

    def test_file_permissions(self):
        """Test file permissions"""
        self.assertTrue(os.access('console.py', os.R_OK))
        self.assertTrue(os.access('console.py', os.W_OK))
        self.assertTrue(os.access('console.py', os.X_OK))

    def test_help_output(self):
        """Test help output for commands"""
        commands = ["create", "all", "show", "destroy", "update"]
        for command in commands:
            with patch('sys.stdout', new=StringIO()) as help_output:
                self.console.onecmd(f"help {command}")
                self.assertTrue(len(help_output.getvalue()) > 0)

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create Holberton")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as output:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(output.getvalue()) > 0)

    # More test cases for other commands...

if __name__ == '__main__':
    unittest.main()
