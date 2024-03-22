#!/usr/bin/python3
"""Base model for our program"""


from datetime import *
import uuid


class BaseModel:
    """base class that
    defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = int(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return self.__dict__
