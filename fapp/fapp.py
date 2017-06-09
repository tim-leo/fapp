# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)

@app.route('/')
def index():
   return render_template('index.htlm')

if __name__ == '__main__':
   app.run(debug = True)
