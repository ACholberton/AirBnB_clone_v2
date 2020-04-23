#!/usr/bin/python3
"""
script that starts a Flask web application
"""


from flask import Flask, render_template


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Python_text(text='is cool'):
    """runs application on host 0.0.0.0 port 5000  and returns python is cool
    if text is None otherwise return python + text"""
    if text is None:
        return 'Python is cool'
    else:
        return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """runs application on host 0.0.0.0 port 5000  and returns a number"""
    if n is int:
        return "{} is a number".format(n)
    else:
        pass


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """runs application on host 0.0.0.0 port 5000  and display an html page
    if the number is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template_odd(n):
    """runs application on host 0.0.0.0 port 5000  and display an html page
    if the number  is an integer"""
    return reder_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
