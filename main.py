from flask import Flask, render_template, request

form = Flask(__name__)

@form.route('/')
def root():
    return render_template("root.html")

@form.route('/result', methods = ['POST', 'GET'])
def requests():
    if request.method == 'POST':
        usr = request.form["usr"]
        pwd = request.form["pwd"]
    else:
        usr = request.args['usr']
        pwd = request.args['pwd']
    if usr == 'softdev' and pwd == 'pd09':
        return render_template("result.html", usr)
    else:
        return render_template("error.html",
                               cUsr = (usr == 'softdev'),
                               cPwd = (pwd == 'pd09'))


if __name__ == "__main__":
    form.debug = True
    form.run()
