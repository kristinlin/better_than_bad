from flask import Flask, render_template, request

form = Flask(__name__)

@form.route('/')
def root():
    return render_template("root.html")

#Correct username: softdev
#Correct password: pd09
@form.route('/result', methods = ['POST', 'GET'])
def requests():
    #either POST or GET method
    if request.method == 'POST':
        usr = request.form["usr"]
        pwd = request.form["pwd"]
    else:
        usr = request.args['usr']
        pwd = request.args['pwd']
    #If username and password are correct, then results
    if usr == 'softdev' and pwd == 'pd09':
        return render_template("result.html", usr = usr)
    #else send to error page, with booleans for password and username
    else:
        cUsr = (usr == 'softdev')
        cPwd = (pwd == 'pd09')
        return render_template("error.html", cUsr = cUsr, cPwd = cPwd)


if __name__ == "__main__":
    form.debug = True
    form.run()
