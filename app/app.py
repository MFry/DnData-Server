from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os

# ---------------------------------------------------------------------------- #
# App Config.                                                                  #
# ---------------------------------------------------------------------------- #

app = Flask(__name__)
#app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''


def factors(num):
    return [x for x in range(1, num+1) if num%x==0]


@app.route('/factors/<int:num>')
def factors_route(num):
    return f'The factors of {num} are {factors(num)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
