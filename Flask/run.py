# we are importing the app Flask object from the app package folder __init__.py file
from app import app 


if __name__ == "__main__":
    app.run(debug=True)


"""
setting up your environment:
run:
export FLASK_APP=<filename.py>
run:
export FLASK_ENV=development - or production
"""