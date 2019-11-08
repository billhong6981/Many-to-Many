#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.todo import Todo

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Employee --")
obj_arg = {
    'title': 'Shipping',
    'completed': 0,
    'due_date': "2019-10-06",
    }
my_user = Todo(**obj_arg)
my_user.save()

print(my_user)
a = my_user.date_to_left
print("today is {}".format(a))
print(my_user.is_past_due)
