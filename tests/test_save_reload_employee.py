#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.employee import Employee

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Employee --")
my_user = Employee()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = Employee()
my_user2.first_name = "John"
my_user2.email = "airbnb2@holbertonshool.com"
my_user2.save()
print(my_user2)
