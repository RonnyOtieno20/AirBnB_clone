#!/usr/bin/python
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance"""
        super().__init__(*args, **kwargs)
