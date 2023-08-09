# from the app package (folder) we are importing the app Flask object we initialized from the __init__.py file
from app import app


# create route decorator
@app.route("/admin/dashboard")
def admin_dashboard():
    return "Admin Dashboard"

# create /about decorator
@app.route("/admin_profile")
def admin_profile():
    return "Admin Profile"