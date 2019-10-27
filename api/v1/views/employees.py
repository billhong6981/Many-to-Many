#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage, CNC
from os import environ
STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/employees/', methods=['GET'])
def employees_no_id(employee_id=None):
    if request.method == 'GET':
        employee_all = storage.all('Employee')
        result = [obj.to_json() for obj in employee_all.values()]
        return jsonify(result)

@app_views.route('/departments/<department_id>/employees', methods=['GET', 'POST'])
def employees_per_department(department_id=None):
    """
    employees route to handle http method for requested employees by department
    """
    department_obj = storage.get('Department', department_id)
    if department_obj is None:
        return make_response(jsonify('{}'), 400)

    if request.method == 'GET':
        all_employees = storage.all('Employee')
        department_employees = [obj.to_json() for obj in all_employees.values()
                       if obj.department_id == department_id]
        return jsonify(department_employees)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            return make_response(jsonify('Not a JSON'), 400)

        department_id = req_json.get("department_id")
        if department_id is None:
            abort(400, 'Missing department_id')
        department_obj = storage.get('Department', department_id)
        if department_obj is None:
            abort(404, 'Not found Department')
        if req_json.get("first_name") is None:
            abort(400, 'Missing first_name')
        if req_json.get("last_name") is None:
            abort(400, 'Missing last_name')
        if req_json.get("email") is None:
            abort(400, 'Missing email')

        Employee = CNC.get("Employee")
        new_object = Employee(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/employees/<employee_id>', methods=['GET', 'DELETE', 'PUT'])
def employees_with_id(employee_id=None):
    """
    employees route to handle http methods for given employee
    """
    employee_obj = storage.get('Employee', employee_id)
    if employee_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(employee_obj.to_json())

    if request.method == 'DELETE':
        employee_obj.delete()
        del employee_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        employee_obj.bm_update(req_json)
        return jsonify(employee_obj.to_json()), 200


@app_views.route('/employees_search', methods=['POST'])
def employees_search():
    """
    employees route to handle http method for request to search employees
    """
    all_employees = [obj for obj in storage.all('Employee').values()]
    all_departments = [d for d in storage.all('Department').values()]
    req_json = request.get_json()
    if req_json is None:
        return make_response(jsonify('Not a JSON'), 400)

    departments = req_json.get('departments')
    for depart in all_departments:
        if departments and depart.id in departments and depart.name == "AllDepartments":
            all_employees = [obj.to_json() for obj in all_employees]
            return jsonify(all_employees)

    if departments and len(departments) > 0:
        department_employees = [employee.id for employee in all_employees if employee.department_id in departments]
    else:
        department_employees = []

    employees = req_json.get('employees', None)
    if employees and len(employees) > 0:
        department_employees = employees

    if len(department_employees) > 0:
        all_employees = [e.to_json() for e in all_employees if e.id in department_employees]
    else:
        all_employees = [{}]
    return jsonify(all_employees)


@app_views.route('/todos_get', methods=['POST'])
def todos_getchar():
    """
    todos route to handle http method for request to search todos
    """
    all_todos = [obj for obj in storage.all('Todo').values()]
    req_json = request.get_json()
    if req_json is None:
        return make_response(jsonify('Not a JSON'), 400)

    todos = req_json.get('todos', None)
    if todos and len(todos) > 0:
        all_todos = [t.to_json() for t in all_todos if t.id in todos]
    else:
        all_todos = [t.to_json() for t in all_todos]
    return jsonify(all_todos)


@app_views.route('/employees_gettodo', methods=['POST'])
def employee_get():
    """
    employee per todos
    """
    all_employees = storage.all('Employee').values()
    req_json = request.get_json()
    if req_json is None:
        return make_response(jsonify('Not a JSON'), 400)

    employees = req_json.get('employees')

    if employees and len(employees) > 0:
        employees = [e.id for e in all_employees if e.id in employees]
    else:
        return jsonify([{}])

    todos = []
    for e_id in employees:
        emp_obj = storage.get('Employee', e_id)
        for obj in emp_obj.todos:
            todos.append(obj)
    todos_employees = [
        obj.to_json() for obj in todos
    ]
    return jsonify(todos_employees)


@app_views.route('/todos_search', methods=['POST'])
def todos_search():
    """
    todo route to handle http method for request to search employees
    """
    all_todos = storage.all('Todo').values()
    req_json = request.get_json()
    if req_json is None:
        return make_response(jsonify('Not a JSON'), 400)

    todos = req_json.get('todos')

    if todos and len(todos) > 0:
        todos = [todo.id for todo in all_todos if todo.id in todos]
    else:
        return jsonify([{}])

    all_employees = [e for e in storage.all('Employee').values()]
    todos_employees = []

    for todo_id in todos:
        todo_obj = storage.get('Todo', todo_id)

        if todo_obj is None:
            abort(404, 'Not found')
        for emp_obj in all_employees:
            employee_todos = emp_obj.todos
            employee_todos = [
                obj for obj in employee_todos
                ]
            for a in employee_todos:
                if todo_id == a.id:
                    todos_employees.append(emp_obj)
    todos_employees = [
        obj.to_json() for obj in todos_employees
    ]
    return jsonify(todos_employees)
