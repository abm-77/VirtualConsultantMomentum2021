from flask import Flask, jsonify, session, redirect
from app import database
from passlib.hash import pbkdf2_sha256
import uuid

class User:
    
    def StartSession(self, user):
        del user["password"]
        session["logged_in"] = True
        session["user"] = user
        return jsonify(user), 200
    
    def SignUp (self, form):

        # Create the User Object
        user = {
                "_id" : uuid.uuid4().hex,
                "name" : form["name"],
                "email" : form["email"],
                "password" : form["password"],
        }

        if user["password"] != form["confirm_password"]:
            return jsonify({"error": "Please ensure your passwords match."}), 400
        
        # Encrypt User's Password
        user["password"] = pbkdf2_sha256.encrypt(user["password"])
       
        # Make Sure New User Isn't In Database
        if database.users.find_one({ "email" : user["email"] }):
            return jsonify({"error" : "Email address is already in use."}), 400
        
        # Return if Succes
        if database.users.insert_one(user):
            return self.StartSession(user) 
        
        # Sign Up Fails
        return jsonify({"error" : "Sign up failed."}), 400

    def SignOut (self):
        session.clear()
        return redirect("/")

    def LogIn (self, form):
        user = database.users.find_one({"email": form["email"]})

        if user and pbkdf2_sha256.verify(form["password"], user["password"]):
            return self.StartSession(user)
        
        return jsonify({"error": "Invalid credentials."}), 401
