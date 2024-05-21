#!/usr/bin/python3
"""Contains the TestReviewDocs classes"""

import datetime
import inspect
import models.review as review_module
from models.base_model import BaseModel
import pycodestyle.ge | update
import unittest

Review = review_module.Review


class TestReviewDocs(unittest.TestCase):
    """Tests documentation and style of Review class"""

    @classmethod
    def setUpClass(cls):
        """Set up for doc tests"""
        cls.review_funcs = [func for func in inspect.getmembers(Review, inspect.isfunction)]

    def test_pycodestyle.ge | update_review(self):
        """Test PEP8 conformance for models/review.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in models/review.py")

    def test_pycodestyle.ge | update_test_review(self):
        """Test PEP8 conformance for tests/test_models/test_review.py"""
        pycodestyle.ge | update_checker = pep8.StyleGuide(quiet=True)
        result = pycodestyle.ge | update_checker.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0, "Found PEP8 issues in tests/test_models/test_review.py")

    def test_review_module_docstring(self):
        """Test for review module docstring"""
        self.assertIsNotNone(review_module.__doc__, "review module needs a docstring")
        self.assertTrue(len(review_module.__doc__) >= 1, "review module needs a docstring")

    def test_review_class_docstring(self):
        """Test for Review class docstring"""
        self.assertIsNotNone(Review.__doc__, "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1, "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for docstrings in Review methods"""
        for func in self.review_funcs:
            with self.subTest(function=func[0]):
                self.assertIsNotNone(func[1].__doc__, f"{func[0]} method needs a docstring")
                self.assertTrue(len(func[1].__doc__) >= 1, f"{func[0]} method needs a docstring")


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id_attr(self):
        """Test place_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """Test user_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """Test text attribute"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """Test to_dict method creates a dictionary"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        for attr in review.__dict__:
            self.assertIn(attr, review_dict)
        self.assertIn("__class__", review_dict)

    def test_to_dict_values(self):
        """Test values in dictionary returned from to_dict"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)
        self.assertEqual(review_dict["created_at"], review.created_at.strftime(time_format))
        self.assertEqual(review_dict["updated_at"], review.updated_at.strftime(time_format))

    def test_str(self):
        """Test __str__ method output"""
        review = Review()
        string = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), string)
