from app import app, database
from flask import render_template, request, jsonify, redirect, session
from functools import wraps
from user.models import User
from module.models import Module

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
    # Get all the modules from the database
    storeModules = database.modules.find({})

    # Turn the 1D array into a 2D array with rows of modulesPerRow
    transformedModuleList = [[]]
    modulesPerRow = 3
    transformedIndex = 0

    for it, elt in enumerate(storeModules):
        if it % modulesPerRow == 0 and it != 0:
            transformedIndex += 1
            transformedModuleList.append([])

        transformedModuleList[transformedIndex].append(elt)
    

    print (transformedModuleList)
    return render_template("public/store.html", marketItems = transformedModuleList)

@app.route("/store/modules/<moduleID>")
def module_store_page(moduleID):
    
    module = database.modules.find_one({"_id" : moduleID})

    return render_template("public/module_page.html", module = module)

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
def log_out():
    return User().SignOut()

# TODO: Implement Login 
@app.route("/login", methods=["GET", "POST"])
@login_prohibited
def login ():
    if request.method == "POST":
        data, err = User().LogIn(request.form)

        if err == 401:
            return render_template("public/login.html", error = data.json["error"])
        else:
            return redirect("/profile")

    return render_template("public/login.html", error = None) 

# TODO: Implement Profiles
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile ():
    if request.method == "POST":

        data, errorCode = Module().CreateModule(request.form)
        if errorCode != 200:
            return render_template("public/profile.html", success = False, error = data.json["error"])
        else:
            return render_template("public/profile.html", success = True, error = None)


    return render_template("public/profile.html", success = None, error = None) 


# TODO: Display User Modules
@app.route("/profile/mymodules")
@login_required
def profile_modules ():
    return "Profile Modules"

