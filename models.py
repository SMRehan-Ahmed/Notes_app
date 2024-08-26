from . import db # imports the db variable from __init__ file
from flask_login import UserMixin # a custom class to handle user login
from sqlalchemy.sql import func
# TABLES of my database : 


class User(db.Model, UserMixin) : # inheritied
    id = db.Column(db.Integer , primary_key = True) # PRIMARY KEY
    email = db.Column(db.String(150), unique = True) # Unique => no other entry can have same email
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note') # Stores multiple notes of a user
    

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000)) # notes
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # FOREIGN KEY REFERRING TO ID OF USER IN USER TABLE 
