#!/usr/bin/python3
"""This module creates a User class"""

from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class City(BaseModel):
    """Class for managing city objects"""

    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="city", cascade="all, delete-orphan")