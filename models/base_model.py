#!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def save(self):
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy.pop('_sa_instance_state', None)
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
