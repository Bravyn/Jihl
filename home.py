from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Welcome to Jihl </h1>"

@app.route('/about')
def about():
    return "<h2> About section </h2>"

@app.route('/products')
def products():
    return "<h3> Products section </h3>"

@app.route('/services')
def services():
    return "<h3> Services section </h3>"