#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage, CNC
from os import environ
STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/employees/<employee_id>/todos', methods=['GET'])
def todos_per_employee(employee_id=None):
    """
    todo route to handle http method for requested todos by employee
    """
    employee_obj = storage.get('Employee', employee_id)

    if request.method == 'GET':
        if employee_obj is None:
            abort(404, 'Not found')
        all_todos = storage.all('Todo')
        if STORAGE_TYPE == 'db':
            employee_todos = employee_obj.todos
        else:
            employee_todo_ids = employee_obj.todos
            employee_todos = []
            for amen in employee_todo_ids:
                employee_todos.append(storage.get('Todo', amen))
        employee_todos = [
            obj.to_json() for obj in employee_todos
            ]
        return jsonify(employee_todos)


@app_views.route('/employees/<employee_id>/todos/<todo_id>',
                 methods=['DELETE', 'POST'])
def todo_to_employee(employee_id=None, todo_id=None):
    """
    todos route to handle http methods for given by ID
    """
    employee_obj = storage.get('Employee', employee_id)
    todo_obj = storage.get('Todo', todo_id)
    if employee_obj is None:
        abort(404, 'Not found')
    if todo_obj is None:
        abort(404, 'Not found')

    if request.method == 'DELETE':
        if (todo_obj not in employee_obj.todos and
                todo_obj.id not in employee_obj.todos):
            abort(404, 'Not found')
        if STORAGE_TYPE == 'db':
            employee_obj.todos.remove(todo_obj)
        else:
            employee_obj.todo_ids.pop(todo_obj.id, None)
        employee_obj.save()
        return jsonify({}), 200

    if request.method == 'POST':
        if (todo_obj in employee_obj.todos or
                todo_obj.id in employee_obj.todos):
            return jsonify(todo_obj.to_json()), 200
        if STORAGE_TYPE == 'db':
            employee_obj.todos.append(todo_obj)
        else:
            employee_obj.todos(todo_obj)
        employee_obj.save()
        return jsonify(todo_obj.to_json()), 201
