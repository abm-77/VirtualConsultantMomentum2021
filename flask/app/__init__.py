from flask import Flask
import pymongo 


app = Flask(__name__)


# Secret Key
app.config["SECRET_KEY"] =
app.config["SECURITY_PASSWORD_SALT"] = ""

# Database
client = pymongo.MongoClient("")
database = client["project_luna"]

from app import views

