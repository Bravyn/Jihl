from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def index(name = None):
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