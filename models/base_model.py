#!/usr/bin/python3
"""Base model for our program"""


from datetime import *
import uuid


class BaseModel:
    """base class that
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items:
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)

            else:
                self.created_at = datetime.now()

            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)

            else:
                self.updated_at = datetime.now()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """convert our data to dictionary and return it"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
