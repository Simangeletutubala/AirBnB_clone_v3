#!/usr/bin/python3
"""This module creates a Place class"""
import models
from os import getenv
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """Class for managing place objects"""

    __tablename__ = 'places'
    
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    
    # Define the relationship with Review
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    
    # Define the many-to-many relationship with Amenity
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    
    @property
    def reviews(self):
        return [review for review in self.reviews if review.place_id == self.id]
    
    @amenities.setter
    def amenities(self, obj):
        if isinstance(obj, Amenity):
            if obj not in self.amenities:
                self.amenities.append(obj)
        else:
            return
