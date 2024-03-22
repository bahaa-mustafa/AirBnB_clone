#!/usr/bin/python3
"""Base model for our program"""


from datetime import *
import uuid


class BaseModel:
    """base class that
    defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary