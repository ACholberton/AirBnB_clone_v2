#!/usr/bin/python3
"""
script that starts a Flask web application
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """runs application on host 0.0.0.0 port 5000"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HBNB():
    """runs application on host 0.0.0.0 port 5000 and returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
        """runs application on host 0.0.0.0 port 5000  and returns c + text"""
        return 'C {}'.format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
