from app import app, database
from flask import render_template, request, jsonify, redirect, session
from functools import wraps
from user.models import User

# Decorators
def login_required(f):
    @wraps(f)
    def wrap (*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")
    return wrap

def login_prohibited(f):
    @wraps(f)
    def wrap (*args, **kwargs):
        if not 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")
    return wrap

# Home Page
@app.route("/")
def index():
    return render_template("public/index.html") 

### STORE VIEWS ###
# TODO: Implement Storefront
@app.route("/store")
def store ():
    return "Store"

@app.route("/store/module/<moduleID>")
def module_store_page(moduleID):
    return f"Module Store Page: {moduleID}"

@app.route("/testmodule")
def testmodule ():
    return render_template("public/testmodule.html")


### MODULE VIEWS ###
@app.route("/modules/<moduleID>")
def module_content_page(moduleID):
    return f"Module Page: {moduleID}"


### USER VIEWS ###
@app.route("/signup", methods=["GET", "POST"])
@login_prohibited
def signup():
    if request.method == "POST":
        data, err = User().SignUp(request.form)

        if err == 400:
            return render_template("public/signup.html", error = data.json["error"])
        else:
            return redirect("/profile")

    return render_template("public/signup.html", error = None)

@app.route("/signout")
def LogOut():
    return User().SignOut()

# TODO: Implement Login 
@app.route("/login", methods=["GET", "POST"])
@login_prohibited
def Login ():
    if request.method == "POST":
        data, err = User().LogIn(request.form)

        if err == 401:
            return render_template("public/login.html", error = data.json["error"])
        else:
            return redirect("/profile")

    return render_template("public/login.html", error = None) 

# TODO: Implement Profiles
@app.route("/profile")
@login_required
def profile ():
    return render_template("public/consumer_profile.html") 


# TODO: Display User Modules
@app.route("/profile/<userID>/mymodules")
@login_required
def profile_modules (userID):
    return "Profile Modules"

