#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: A tuple of arguments (not used).
            **kwargs: A dictionary of key-value pairs to initialize
                the instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: A dictionary representation of the instance.
        """
        dict_repr = self.__dict__.copy()
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        return dict_repr
