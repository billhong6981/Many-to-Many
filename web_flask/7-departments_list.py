#!/usr/bin/python3
"""
Sript that starts a Flask web application
"""
from flask import Flask, render_template, jsonify
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
        method to handle teardown
    """
    storage.close()


@app.route('/departments_list', strict_slashes=False)
def department_list():
    """
        method to render departments
    """
    departments = storage.all('Department').values()
    return render_template("7-departments_list.html", departments=departments)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
