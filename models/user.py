#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: emais
        password: password for
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")
