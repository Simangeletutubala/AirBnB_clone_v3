#!/usr/bin/python3
"""This module creates a State class"""

import models
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
#from models import HBNB_TYPE_STORAGE



class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
    
    #if models.storage_type == 'db':
      
    #elif models.storage_type == 'file':
    #    @property
    #    def cities(self):
    #        from models import storage
    #       city_list = []
    #        for city in storage.all(City).values():
    #            if city.state_id == self.id:
    #                city_list.append(city)
    #        return city_list
