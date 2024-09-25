from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
@app.route('/hello/<name>', methods = ['GET', 'POST'])
def index(name = None):
    if request.method == 'POST':
        input_val = request.form.get('inputBox')
        return render_template("hello.html", person = input_val)
    return render_template("hello.html", person = name)



@app.route('/about')
def about():
    return "<h2> About section </h2>"

@app.route('/products')
def products():
    return "<h3> Products section </h3>"

@app.route('/services')
def services():
    return "<h3> Services section </h3>"