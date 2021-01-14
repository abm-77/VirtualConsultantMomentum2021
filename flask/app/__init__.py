from flask import Flask
import pymongo 


app = Flask(__name__)


# Secret Key
app.config["SECRET_KEY"] = b']\xdf\x8d\x03\x8f\xaf\xde\xa7\x89\x18\x83U\xce\xbf\xa6t'
app.config["SECURITY_PASSWORD_SALT"] = "temporary"

# Database
client = pymongo.MongoClient("mongodb+srv://BeaverAdmin:zkzueLbNEWpEuo9j@cluster0.0ypwg.mongodb.net/project_luna?retryWrites=true&w=majority")
database = client["project_luna"]

from app import views

