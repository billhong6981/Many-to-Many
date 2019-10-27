#!/usr/bin/python3
"""
Department Class from Models Module
"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class Department(BaseModel, Base):
    """Department class handles all application departments"""
    if STORAGE_TYPE == "db":
        __tablename__ = 'departments'
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        employees = relationship('Employee', backref='department', cascade='delete')
        users = relationship('User', backref='department', cascade='delete')

    else:
        name = ''
        description = ''

        @property
        def employees(self):
            """
            getter method, returns list of Employee objs from storage
            linked to the current Department
            """
            employee_list = []
            for employee in models.storage.all("Employee").values():
                if employee.department_id == self.id:
                    employee_list.append(employee)
            return employee_list

        @property
        def users(self):
            """
            getter method, returns list of user objs from storage
            linked to the current Department
            """
            all_users =  models.storage.all("User").values()
            user_list = [ user for user in all_users
                          if user.department_id == self.id]
            return user_list
