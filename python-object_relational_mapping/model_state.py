#!/usr/bin/python3

"""
This module defines the State class which represents a table structure for 'states' in a database.
It utilizes SQLAlchemy, an Object-Relational Mapping (ORM) library, to abstract and interact with the database using Python classes and objects.
    
classe:
state: Defines the structure of the 'states' table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """
    Defines a State class for the 'states' table with 'id' (primary key) 
    and 'name' attributes.
    """
    
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
