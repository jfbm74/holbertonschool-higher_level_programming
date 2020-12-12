#!/usr/bin/python3
""" class City and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement="auto"
    )

    name = Column(
        String(128),
        nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False,
    )
