#!/usr/bin/python3

"""
This module creates a State class for database
'states' using SQLAlchemy for ORM.
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
