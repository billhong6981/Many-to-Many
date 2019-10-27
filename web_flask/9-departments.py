#!/usr/bin/python3
"""
    Sript that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
import os
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/departments', strict_slashes=False)
def department_list():
    """
        method to render departments
    """
    departments = storage.all('Department').values()
    return render_template(
        "9-departments.html",
        departments=departments,
        condition="departments_list")


@app.route('/departments/<id>', strict_slashes=False)
def departments_id(id):
    """
        method to render department ids
    """
    try:
        department_id = storage.get('Department', id)
        return render_template(
            '9-departments.html',
            department_id=department_id,
            condition="department_id")
    except:
        return render_template('9-departments.html', condition="not_found")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
