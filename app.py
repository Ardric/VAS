import sqlite3
from flask import Flask, render_template, flash, g, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, IntegerField, FileField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)


class SubmissionForm(Form):
    author = StringField('Author', [validators.Length(min=1, max=100)])
    institution = StringField('Institution', [validators.Length(min=1, max=100)])
    email = StringField('Email', [validators.Length(min=1, max=100)])
    title = StringField('Title', [validators.Length(min=1, max=100)])
    section= IntegerField('Section', [validators.Length(min=1, max=4)])
    year = IntegerField('Year', [validators.Length(min=4, max=4)])
    file = FileField('File')

@app.route('/Submit', methods=['GET', 'POST'])
def Submit():
    form = SubmissionForm(request.form)
    if request.method == 'POST' and form.validate():
        
        return 
    return render_template('SubmitForm.txt', form=form)



class AdminLoginForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=100), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=1, max=100), validators.DataRequired()])

@app.route('/AdminLogin', methods=['GET', 'POST'])
def Login():
    form = AdminLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        return
    return render_template('AdminForm.txt', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
