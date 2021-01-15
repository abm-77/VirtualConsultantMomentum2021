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
        
        if database.modules.insert_one(module):
            return None, 200

        return jsonify({"error": "There was an error creating this module!"}), 400
