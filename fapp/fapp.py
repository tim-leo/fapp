# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/validusers')
def validusers():
    return render_template('validusers.html')

@app.route('/contact')
def validusers():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug = True)
