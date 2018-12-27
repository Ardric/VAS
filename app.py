import sqlite3
from flask import Flask, render_template, flash, g, redirect, url_for, session, logging, request
from wtforms import Form, StringField, TextAreaField, PasswordField, IntegerField, FileField, validators
from passlib.hash import sha512_crypt

app = Flask(__name__)

class SubmissionForm(Form):
    author = StringField('Author', [validators.Length(min=1, max=100)])
    institution = StringField('Institution', [validators.Length(min=1, max=100)])
    email = StringField('Email', [validators.Length(min=1, max=100)])
    title = StringField('Title', [validators.Length(min=1, max=100)])
    section= IntegerField('Section')
    year = IntegerField('Year')
    file = FileField('File')

@app.route('/Submit', methods=['GET', 'POST'])
def Submit():
    form = SubmissionForm(request.form)
    if request.method == 'POST' and form.validate():        
        author = form.author.data
        institution = form.institution.data
        email = form.email.data
        title = form.title.data
        section = form.section.data
        year = form.year.data
        file = form.file.data

        conn = sqlite3.connect('C:/Users/WDLowdermilk/AppData/Local/Programs/Python/Python37-32/VAS/VAS.db')
        c = conn.cursor()
        c.execute('INSERT INTO PresenterInfo (Author, Institution, Email, Title, Section, Year, File) VALUES (?,?,?,?,?,?,?)',
                      (author, institution, email, title, section, year, file))
        conn.commit()
        conn.close()

        return render_template('Completed.txt')
        
    return render_template('SubmitForm.txt', form=form)

class AdminLoginForm(Form):
    username = StringField('Username', [validators.Length(min=1, max=100), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=1, max=100), validators.DataRequired()])

@app.route('/AdminLogin', methods=['GET', 'POST'])
def Login():
    form = AdminLoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = sha512_crypt.encrypt(str(form.password.data))

        conn = sqlite3.connect('VAS.db')
        c = conn.cursor()
        for row in c.execute('SELECT password FROM Admin WHERE username = ?', username):
            if row[0] == password:
                #Redirect to Admin view page
                return
        return

    return render_template('AdminForm.txt', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
