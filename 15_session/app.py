# The Adjective Nouns -- Andrew Juang, Noakai Aronesty, Eric Guo
# SoftDev
# K15 -- Sessions Greetings
# 2021-10-18

from os import urandom
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Secret key for session
app.secret_key = urandom(32)

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    if 'username' in session:
        return render_template('response.html',username=session['username'])
    return render_template('login.html')

@app.route("/auth", methods=['GET','POST'])
def authenticate():
    # Variables
    method = request.method
    username = request.form.get('username')
    password = request.form.get('password')

    if method == 'GET':
        return redirect(url_for('disp_loginpage'))
    if method == 'POST':
        if username != 'eric' and password != 'guo':
            return render_template('login.html',input='Username and password are ')
        elif username != 'eric':
            return render_template('login.html',input='Username is ')
        elif password != 'guo':
            return render_template('login.html',input='Password is ')
        else:
            session['username'] = 'eric'
            return render_template('response.html',username=session['username'])

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('disp_loginpage'))



if __name__ == "__main__":
    app.debug = True
    app.run()
