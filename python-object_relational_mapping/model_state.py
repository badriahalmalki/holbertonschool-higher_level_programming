#!/usr/bin/python3
"""SQLAlchemy model for a State and declarative Base.

Defines the State class mapped to the MySQL table `states` and exposes
the `Base` declarative base for use by other modules.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State model for the states table with id and name columns."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
