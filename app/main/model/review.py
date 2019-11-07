from .. import db , flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class Review(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "review"

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    place_id = db.Column(db.Integer, ForeignKey('place.place_id'))

    review = db.Column(db.String(255), unique=True, nullable=False)
  
   
