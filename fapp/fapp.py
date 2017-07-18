# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import boto3
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from boto3.dynamodb.conditions import Key, Attr
from flask_dynamo import Dynamo

app = Flask(__name__) # create the application instance :)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

print(table.key_schema)

#
# dynamodb = boto3.resource('dynamodb')

class UserForm(Form):
    usernames = StringField('Username', [validators.Length(min=3, max=25)])
    # password = PasswordField(validators.Length(min=3))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserForm(request.form)
    # repo = table.query

    if request.method == 'POST' and form.validate():
        usernames=request.form['usernames']
        isuser = table.get_item(
            Key={
                'username': 'usernames'
            }
        )
        print (isuser)
        print (usernames)
        print("penis")
        if form.validate():
            flash('eat a dick ' + usernames)
        else:
            flash('all form fields required choad')

    title = "A Fancy Title"
    return render_template('index.html', title=title, form=form)


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
