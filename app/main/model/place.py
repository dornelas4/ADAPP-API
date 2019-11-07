from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
from sqlalchemy.orm import relationship

class Place(db.Model):
    """ Place Model for storing place related details """
    __tablename__ = "place"

    place_id = db.Column(db.String(255),primary_key = True , nullable=False)
    review = relationship('Review')
    
    name = db.Column(db.String(255), nullable=True)
    latitude = db.Column(db.String(255), nullable=True)
    longitude = db.Column(db.String(255),  nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    wheelchair = db.Column(db.Boolean,nullable = True)
    parking  = db.Column(db.Boolean,nullable = True)
    bathroom  = db.Column(db.Boolean,nullable = True)
    elevator  = db.Column(db.Boolean,nullable = True)
    doors  = db.Column(db.Boolean,nullable = True)