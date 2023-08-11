# from the app package (folder) we are importing the app Flask object we initialized from the __init__.py file
from app import app

from flask import render_template

# create route decorator
@app.route("/")
def index():
    return render_template("index.html")

# create /about decorator
@app.route("/about")
def about():
    return "<h1 style='color: red'>About Page!</h1>"