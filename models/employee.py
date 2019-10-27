#!/usr/bin/python3
"""
Employee Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import backref
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')

if STORAGE_TYPE == "db":
    class EmployeeTodo(Base):
        """ EmployeeTodo Class """
        __tablename__ = 'employee_todo'
        metadata = Base.metadata
        employee_id = Column(String(60),
                             ForeignKey('employees.id'),
                             nullable=False,
                             primary_key=True)
        todo_id = Column(String(60),
                         ForeignKey('todos.id'),
                         nullable=False,
                         primary_key=True)

class Employee(BaseModel, Base):
    """Employee class handles all application employees"""
    if STORAGE_TYPE == "db":
        __tablename__ = 'employees'
        email = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        department_id = Column(String(60),
                               ForeignKey('departments.id'),
                               nullable=False)
        description = Column(String(1024), nullable=True)
        todos = relationship('Todo', secondary="employee_todo",
                             viewonly=False)
    else:
        department_id = ''
        first_name = ''
        last_name = ''
        email = ''
        description = ''
        todo_ids = []

        @property
        def todos(self):
            """
            getter for todos list, i.e. todos attribute of self
            """
            if len(self.todo_ids) > 0:
                return todo_ids
            else:
                return None

        @todos.setter
        def todos(self, todo_obj):
            """
            setter for todo_ids
            """
            if todo_obj and todo_obj.id not in self.todo_ids:
                self.todo_ids.append(todo_obj.id)
