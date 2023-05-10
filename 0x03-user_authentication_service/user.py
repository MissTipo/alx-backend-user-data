#!/usr/bin/env python3
"""User model."""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from typing import Optional


Base = declarative_base()


class User(Base):
    """Class User"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(
            self,
            email: str,
            hashed_password: str,
            session_id: Optional[str],
            reset_token: Optional[str]):
        """Instantiates User class."""
        email = self.email
        hashed_password = self.hashed_password
        session_id = self.session_id
        reset_token = self.reset_token
