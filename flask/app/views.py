from app import app
from flask import render_template


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
# TODO: Implement Signup
@app.route("/signup")
def signup():
    return "Signup"

# TODO: Implement Login 
@app.route("/login")
def Login ():
    return "Login"

# TODO: Implement Profiles
@app.route("/profile/<userID>")
def profile (userID):
    return "Profile"

@app.route("/profile/<userID>/mymodules")
def profile_modules (userID):
    return "Profile Modules"

