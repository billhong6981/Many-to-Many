#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Employee --")
obj_arg = {
    'password': 'root2',
    'first_name': "Betty2",
    'last_name': "Holberton2",
    'email': "airbnb@holbertonshool.com"
    }
my_user = User(**obj_arg)
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.password = "demo"
my_user2.first_name = "John"
my_user2.email = "airbnb2@holbertonshool.com"
my_user2.save()
print(my_user2)
