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


@app.route('/employees_by_departments', strict_slashes=False)
def employee_department_list():
    """
        method to render departments from storage
    """
    departments = storage.all('Department').values()
    return render_template("8-employees_by_departments.html", departments=departments)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
