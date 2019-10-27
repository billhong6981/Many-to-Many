#!/usr/bin/python3
"""
    Flask route that returns json respone
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage, CNC
from os import environ
STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')

@app_views.route('/logins/', methods=['POST'])
def load_login():
    """
    verifies user email and password for login page
    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    all_users = [u for u in storage.all('User').values()]
    if all_users is None:
        abort(404, 'Not found')

    pswd = req_json.get('password')
    cache_id = req_json.get('cache_id')
    for user in all_users:
        if user.email == req_json.get('email'):
            if user.is_match_password(user.email, pswd):
                return jsonify({"cache_id": cache_id}), 200
    abort(404, 'Not match')


@app_views.route('/departmentform/', methods=['POST'])
def load_departmentform():
    """
    load department form
    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    s = """
        <form id="department1">
        <section>
          <p>
          <label for="name">
          Name:
          </label> <br />
          <input type="text" id="name" name="name">
          </p>
        <p>
          <label for="description">
            Description:
          </label><br />
          <textarea id="msg" name="description"></textarea>
        </p>
        </section>
        <section class="right_button">
          <button class="department1" type="submit">Add Department</button>
        </section>
      </form>
    """
    dic = {}
    dic['form'] = s
    return jsonify(dic)


@app_views.route('/employeeform/', methods=['POST'])
def load_employeeform():
    """
    load employee form
    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    s = """
        <form id="employee1">
        <section>
          <label for="departmentId">
          Department Id:
          </label> <br />
          <input type="text" id="departmentId" name="department_id">
          <p>
            <label for="firstName">
              First Name:
            </label> <br />
            <input type="text" id="firstName" name="first_name">
          </p>
          <p>
            <label for="lastName">
              Last Name:
            </label> <br />
            <input type="text" id="lastName" name="last_name">
          </p>
          <p>
            <label for="email">
              Email:
            </label> <br />
            <input type="text" id="email" name="email">
          </p>
        <p>
        </p>
        </section>
        <section class="right_button">
          <button class="employee1" type="submit">Add Employee</button>
        </section>
      </form>
    """
    dic = {}
    dic['form'] = s
    return jsonify(dic)


@app_views.route('/todoform/', methods=['POST'])
def load_todoform():
    """
    load department form
    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    s = """
        <form id="todo1">
        <section>
          <label for="title">
          Title:
          </label> <br />
          <input type="text" id="name" name="title">
          <p>
            <label for="date">
              Due date:
            </label> <br />
            <input type="date" id="date" name="due_date">
          </p>
          <p>
            <label for="completed">
              Completed:
            </label> <br />
            <select id="completed" name="completed">
              <option value=1>True</option>
              <option value=0>False</option>
            </select>
          </p>
        <p>
          <label for="description">
            Description:
          </label><br />
          <textarea id="msg" name="description"></textarea>
        </p>
        </section>
        <section class="right_button">
          <button class="todo1" type="submit">Add Todo</button>
        </section>
      </form>
    """
    dic = {}
    dic['form'] = s
    return jsonify(dic)


@app_views.route('/employeetodoform/', methods=['POST'])
def load_employeetodoform():
    """
    load employeetodo form
    """
    req_json = request.get_json()
    if req_json is None:
        abort(400, 'Not a JSON')
    s = """
        <form id="employeetodo1">
         <p></p>
        <section>
         <p>
          <label for="employeeId">
          Employee Id:
          </label> <br />
          <input type="text" id="employeeid" name="employee_id">
         </p>
         <p>
          <label for="todoId">
          Todo Id:
          </label> <br />
          <input type="text" id="todoid" name="todo_id">
         </p>
        </section>
         <p></p>
        <section class="right_button">
          <button class="employeetodo1" type="submit">Add Todo to Employee</button>
        </section>
      </form>
    """
    dic = {}
    dic['form'] = s
    return jsonify(dic)


@app_views.route('/todos/', methods=['GET', 'POST'])
def todos_no_id(todo_id=None):
    """
        todos route that handles http requests no ID given
    """
    if request.method == 'GET':
        all_todos = storage.all('Todo')
        all_todos = [obj.to_json() for obj in all_todos.values()]
        return jsonify(all_todos)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get('title') is None:
            abort(400, 'Missing job title')
        if req_json.get('due_date') is None:
            abort(400, 'Missing due date')
        if req_json.get('completed') is None:
            abort(400, 'Missing completed status')
        Todo = CNC.get('Todo')
        new_object = Todo(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/todos/<todo_id>', methods=['GET', 'DELETE', 'PUT'])
def todos_with_id(todo_id=None):
    """
    todos route that handles http requests with ID given
    """
    todo_obj = storage.get('Todo', todo_id)
    if todo_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(todo_obj.to_json())

    if request.method == 'DELETE':
        todo_obj.delete()
        del todo_obj
        return jsonify({}), 200

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        todo_obj.bm_update(req_json)
        return jsonify(todo_obj.to_json()), 200

@app_views.route('/todos/<todo_id>/employees', methods=['GET'])
def employees_per_todo(todo_id=None):
    """
    todo route to handle http method for request to search employees
    """
    todo_obj = storage.get('Todo', todo_id)
    all_employees = [e for e in storage.all('Employee').values()]
    todos_employees = []
    if request.method == 'GET':
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
