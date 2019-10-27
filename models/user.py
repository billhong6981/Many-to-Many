#!/usr/bin/python3
"""
User Class from Models Module
"""
import hashlib
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """
    User class handles all application users
    """
    if STORAGE_TYPE == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        department_id = Column(String(60),
                               ForeignKey('departments.id'),
                               nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
        department_id = ''
        description = ''

    def __init__(self, *args, **kwargs):
        """
        instantiates user object
        """
        if kwargs:
            pwd = kwargs.pop('password', None)
            if pwd:
                User.__set_password(self, pwd)
        super().__init__(*args, **kwargs)

    def __set_password(self, pwd):
        """
        custom setter: encrypts password to MD5
        """
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        secure_password = secure.hexdigest().lower()
        setattr(self, "password", secure_password)

    def is_match_password(self, email, pwd):
        """
        return True if user email and pwd are match
        hashlib.md5(pwd.encode("utf-8")).hexdigest().lower()
        """
        if email is None or pwd is None:
            return False
        if pwd == self.password and email == self.email:
            return True
        else:
            return False
