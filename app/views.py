from app import app
from flask import render_template

# Home Page
@app.route("/")
def index():
    return render_template("public/index.html") 

