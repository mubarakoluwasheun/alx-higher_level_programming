#!/usr/bin/python3
"""Defines class city."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State

# Base = dekarative_base()


class City(Base):
    """
    Class City; instance of Base
    Linked to MySQL table "city"
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True) # autoincrements
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
