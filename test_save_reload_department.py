#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.department import Department

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Department --")
my_department = Department()
my_department.name = "Fetty"
my_department.save()
print(my_department)

print("-- Create a new User 2 --")
my_department2 = Department()
my_department2.name = "Fohn"
my_department2.save()
print(my_department2)
