#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.employee import Employee
from models.user import User
from models.department import Department
from models.todo import Todo

fs = FileStorage()

# All States
all_users = fs.all("User")
all_departments = fs.all("Department")
all_employees = fs.all("Employee")
all_todos = fs.all("Todo")
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

# Create a new User
new_user = Todo()
new_user.name = "California"
fs.new(new_user)
fs.save()
print("New User: {}".format(new_user))

# All Users
all_users = fs.all("Todo")
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])

# Delete the new User
fs.delete(new_user)

# All Users
all_users = fs.all("Todo")
print("All Users: {}".format(len(all_users.keys())))
for user_key in all_users.keys():
    print(all_users[user_key])
