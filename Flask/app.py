from flask import Flask

# create a flask object
app = Flask(__name__)

# create route decorator
@app.route("/")
def index():
    return "Hello World!"

# create /about decorator
@app.route("/about")
def about():
    return "<h1 style='color: red'>About Page!</h1>"


if __name__ == "__main__":
    app.run()


"""
setting up your environment:
run:
export FLASK_APP=<filename.py>
run:
export FLASK_ENV=development - or production
"""