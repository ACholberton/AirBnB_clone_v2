#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
from models.state import State
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list(self):
    """display a HTML page, listens on port 5000 of the 0.0.0.0 host
    and routes all states"""
    state = storage.all("States")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """closes the session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
