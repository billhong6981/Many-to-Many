#!/usr/bin/python3
"""
Flask App that integrates with BH_Todos static HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route('/8-bh/')
def bh_filters(the_id=None):
    """
    handles request to custom template with departments, employees & todos
    """
    departments = storage.all('Department')
    todos = storage.all('Todo')
    emps = storage.all('Employee')
    cache_id = uuid.uuid4()
    return render_template('8-bh.html',
                           departments=departments,
                           todos=todos,
                           emps=emps,
                           cache_id=cache_id)

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
