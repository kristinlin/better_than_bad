#Fabiha Ahmed, Kristin Lin
#SoftDev pd09
#Work07 -- It's login, login, it's better than bad, it's good!
#2017-10-04

from flask import Flask, render_template, request, session
import os

form = Flask(__name__)

form.secret_key = os.urandom(8)

#boolean to check if logged in
login = False

@form.route('/', methods = ['POST', 'GET'])
def root():
    if not login:
        return render_template("root.html")
    else:
        return render_template("result.html", usr = session['usr'])

#Correct username: softdev
#Correct password: pd09
@form.route('/result', methods = ['POST', 'GET'])
def requests():
    #are you logged in already?
    if login:
        return render_template("result.html", usr = session['usr'])
    #either POST or GET method
    if request.method == 'POST':
        usr = request.form["usr"]
        pwd = request.form["pwd"]
    else:
        usr = request.args['usr']
        pwd = request.args['pwd']
    #If username and password are correct, then results
    if usr == 'softdev' and pwd == 'pd09':
        global login 
        login = True
        session['usr'] = usr
        return render_template("result.html", usr = usr)
    #else send to error page, with booleans for password and username
    else:
        return render_template("error.html", cUsr = (usr == 'softdev'),
        cPwd = (pwd == 'pd09'))

#logout route
@form.route('/logout', methods = ['POST', 'GET'])
def logout():
    #either POST or GET method
    if request.method == 'POST':
        log = request.form['log']
    else:
        log = request.args['log']
    global login
    login = False
    usr = session['usr']
    session.pop('usr') #end session
    return render_template('logout.html', usr = usr)
    
if __name__ == "__main__":
    form.debug = True
    form.run()
