#!/usr/bin/python3
"""
Defines the BaseModel class
"""

from datetime import datetime
import models
import uuid

TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """A base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initializes the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(kwargs["created_at"], TIME_FORMAT)
            if hasattr(self, "updated_at") and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], TIME_FORMAT)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates 'updated_at' attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.strftime(TIME_FORMAT) if "created_at" in new_dict else None
        new_dict["updated_at"] = self.updated_at.strftime(TIME_FORMAT) if "updated_at" in new_dict else None
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
