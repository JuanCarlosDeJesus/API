# from the app package (folder) we are importing the app Flask object we initialized from the __init__.py file
from app import app

from flask import render_template

# create route decorator
@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

# create /about decorator
@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/profile.html")