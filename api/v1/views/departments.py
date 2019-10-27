#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage, CNC


@app_views.route('/departments', methods=['GET', 'POST'])
def departments_no_id():
    """
    departments route to handle http method for requested with no id
    """
    if request.method == 'GET':
        all_departments = storage.all('Department')
        all_departments = [obj.to_json() for obj in all_departments.values()]
        return jsonify(all_departments)

    if request.method == 'POST':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        if req_json.get("name") is None:
            abort(400, 'Missing name')
        Department = CNC.get("Department")
        new_object = Department(**req_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/departments/<department_id>', methods=['GET', 'DELETE', 'PUT'])
def departments_with_id(department_id=None):
    """
    departments route to handle http method for requested department by id
    """
    department_obj = storage.get('Department', department_id)
    if department_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(department_obj.to_json())

    if request.method == 'DELETE':
        department_obj.delete()
        del department_obj
        return jsonify({})

    if request.method == 'PUT':
        req_json = request.get_json()
        if req_json is None:
            abort(400, 'Not a JSON')
        department_obj.bm_update(req_json)
        return jsonify(department_obj.to_json())
