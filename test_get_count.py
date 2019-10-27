#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage

print("All objects: {}".format(storage.count()))
print("User objects: {}".format(storage.count("User")))
print("Department objects: {}".format(storage.count("Department")))
print("Employee objects: {}".format(storage.count("Employee")))
print("Todo objects: {}".format(storage.count("Todo")))

first_user_id = list(storage.all("User").values())[0].id
print("First user: {}".format(storage.get("User", first_user_id)))

first_department_id = list(storage.all("Department").values())[0].id
print("First department: {}".format(storage.get("Department", first_department_id)))

first_employee_id = list(storage.all("Employee").values())[0].id
print("First employee: {}".format(storage.get("Employee", first_employee_id)))

first_todo_id = list(storage.all("Todo").values())[0].id
print("First todo: {}".format(storage.get("Todo", first_todo_id)))
