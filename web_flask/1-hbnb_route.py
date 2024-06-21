#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Displays Hello HBNB!
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """
    Displays 'HBNB'.
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)