#!/usr/bin/python3
"""
Sript that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bh():
    """
    function to return Hello BH!
    """
    return "Hello BH!"


@app.route('/bh', strict_slashes=False)
def bh():
    """
    function to return BH
    """
    return "BH"
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
