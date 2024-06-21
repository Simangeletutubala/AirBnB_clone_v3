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

@app.route('/c/<text>')
def c_with_params(text):
    """
    Displays 'C' followed by the value of <text>.
    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)