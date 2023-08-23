# from the app package (folder) we are importing the app Flask object we initialized from the __init__.py file
from app import app

from flask import render_template

# create route decorator
@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():
    
    my_name = "Carl"    
    age = 52
    langs = ['Visual Basic','HTML','Python','Javascript']
    friends = {
        'Tom': 34,
        'Amy': 60,
        'Tony': 56,
        'Clarissa': 23
        }
    colors = ('Red','Green')
    cool = True
    
    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url
        
        def pull(self):
            return f"Pulling Repo {self.name}"
        
        def clone(self):
            return f"Cloning Repo {self.url}"
    
    my_remote = GitRemote(
        name = "Flask Jinja",
        description = "Template design Tutorial",
        url = "https://github/JuanCarlosDeJesus/jinja.git"
    )
    
    def repeat(x, qty):
        return x * qty
              
    
    return render_template("public/jinja.html",
                            my_name = my_name,
                            age=age,
                            langs=langs,
                            friends=friends,
                            colors=colors,
                            cool=cool,
                            GitRemote=GitRemote,
                            repeat=repeat,
                            my_remote=my_remote
                            )

# create /about decorator
@app.route("/about")
def about():
    return render_template("public/about.html")