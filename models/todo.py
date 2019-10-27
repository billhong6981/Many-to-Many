#!/usr/bin/python3
"""
Todo Class from Models Module
"""
import os
from datetime import datetime, date, time, timedelta
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import backref
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class Todo(BaseModel, Base):
    """Todo class handles all application todos"""
    if STORAGE_TYPE == "db":
        __tablename__ = 'todos'
        title = Column(String(128), nullable=False)
        due_date = Column(DateTime, nullable=False)
        completed = Column(Integer, nullable=False, default=0)
        description = Column(String(1024), nullable=True)
        employee_todos = relationship('EmployeeTodo',
                                      backref='todos',
                                      cascade='delete')

    else:
        title = ''
        due_date = ''
        completed = 0
        description = ''

    def __init__(self, *args, **kwargs):
        """
        instantiates user object
        """
        if kwargs:
            if not isinstance(kwargs['due_date'], datetime):
                self.due_date = datetime.strptime(
                    kwargs['due_date'],"%Y-%m-%d"
                    )
            else:
                self.due_date = kwargs['due_date']
        super().__init__(*args, **kwargs)

    @property
    def date_to_left(self):
        day1 = datetime.strptime(self.due_date, "%Y-%m-%d")
        delta = day1 - datetime.now()
        return delta.days

    @property
    def is_past_due(self):
        day1 = datetime.strptime(self.due_date, "%Y-%m-%d")
        return day1 < datetime.now()
