from flask import Flask, jsonify, redirect, session
from app import database 
import uuid

class Module:

    def CreateModule (self, form):

        module = {
                "_id":     uuid.uuid4().hex,
            "name":        form["moduleName"],
            "description": form["moduleDescr"],
            "image":       "",
            "price":       form["modulePrice"],
            "creator_id":  session["user"]["_id"]
        }
        
        owner = database.users.find_one({"_id": module["creator_id"]})

        if owner:
            module["author"] = owner["name"]
        else:
            return jsonify({"error": "The user who wants to create this account doesn't exist!"}), 400

        if database.modules.insert_one(module):
            return None, 200

        return jsonify({"error": "There was an error creating this module!"}), 400
