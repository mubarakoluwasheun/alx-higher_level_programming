#!/usr/bin/python3
"""Defines class State."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class State; instance of Base
    Linked to MySQL table "states"
    """
    __tablename__ = "states"
    id = column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)