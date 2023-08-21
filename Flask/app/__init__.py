# By adding the __init__.py in the app folder you turned it into a module. Package file - all imports done here
from flask import Flask


app = Flask(__name__)

# to avoid circular import error, from the app folder we are importing the views file
from app import views
from app import admin_views
