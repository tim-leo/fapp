# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)


@app.route('/')
@app.route('/index')
def index():
    title = "A Fancy Title"
    return render_template('index.html', title=title)


@app.route('/validusers')
def validusers():
    return render_template('validusers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


if __name__ == '__main__':
    app.run(debug = True)
