# The Adjective Nouns -- Andrew Juang, Noakai Aronesty, Eric Guo
# SoftDev
# K15 -- Sessions Greetings
# 2021-10-18

from flask import Flask, render_template, request, session

app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    #
    # print("***DIAG: request.args ***")
    # print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(session)
    if len(session) !=0:
        session.pop('eric')
    print(request.headers)
    return render_template( 'login.html')


@app.route("/auth", methods=['GET','POST'])
def authenticate():
    # print("\n\n\n")
    # print("***DIAG: this Flask obj ***")
    # print(app)
    # print("***DIAG: request obj ***")
    # print(request)
    # print("***DIAG: request.args ***")
    # print(request.args)
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username'])
    # print("***DIAG: request.headers ***")
    print(request.headers)
    if request.method == 'GET':
        if request.args.get('username') != 'eric' and request.args.get('password') != 'guo': #if both inputs are wrong tells them both are wrong
            return render_template('login.html',input='Username and password are ')
        elif request.args.get('username') != 'eric': #if only username is wrong, tell them only username is wrong
            return render_template('login.html',input='Username is ')
        elif request.args.get('password') != 'guo': #if only password is wrong, tell them only password is wrong
            return render_template('login.html',input='Password is ')
        else:
            session[request.args.get('username')] = request.args.get('password')
            return render_template('response.html',username=request.args.get('username'), method=request.method)  #response to a form submission
    elif request.method == 'POST':
        if request.form.get('username') != 'eric' and request.form.get('password') != 'guo': #if both inputs are wrong tells them both are wrong
            return render_template('login.html',input='Username and password are ')
        elif request.form.get('username') != 'eric': #if only username is wrong, tell them only username is wrong
            return render_template('login.html',input='Username is ')
        elif request.form.get('password') != 'guo': #if only password is wrong, tell them only password is wrong
            return render_template('login.html',input='Password is ')
        else:
            session[request.form.get('username')] = request.form.get('password')
            return render_template('response.html',username=request.form.get('username'), method=request.method)  #response to a form submission




if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.secret_key='foo'
    app.debug = True
    app.run()
