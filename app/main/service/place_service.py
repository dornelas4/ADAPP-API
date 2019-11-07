import uuid
import datetime

from app.main import db
from app.main.model.place import Place
from sqlalchemy import or_

def get_all_places():
    return Place.query.all()

def delete_place(latitude, longitude):
    place_id = "{}.{}".format(latitude, longitude)
    if Place.query.filter_by(place_id=place_id).delete():
        db.session.commit()
        response_object = {
            'status': 'sucess',
            'message': 'Place was deleted', 
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Place does not exit. Please try another place id',
        }
        return response_object, 409

def update_place(data):
    placed_id = "{}.{}".format(data['latitude'], data['longitude'])
    place = Place.query.filter(or_(Place.place_id == placed_id)).first()
    if place:
        place.name = data['name']
    
        place.rating = data['rating']
        place.accessibilities = data['accessibilities']
        place.latitude = data['latitude']
        place.longitude = data['longitude']
        place.wheelchair = data['wheelchair']
        place.parking = data['parking']
        place.bathroom = data['bathroom']
        place.elevator = data['elevator']
        place.doors = data['doors']

        response_object = {
            'status': 'success',
            'message': 'Place was updated',
        }
      
        db.session.commit()
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Place does not exist. Please select a valid place.',
        }
        return response_object, 409

def save_new_place(data):
    placed_id = "{}.{}".format(data['latitude'], data['longitude'])
    place = Place.query.filter(or_(Place.place_id == placed_id)).first()
    if not place:
        new_place = Place(
            place_id=placed_id,
            name=data['name'],
            
            rating=data['rating'],
            longitude=data['longitude'],
            latitude=data['latitude'],
            wheelchair = data['wheelchair'],
            parking = data['parking'],
            bathroom = data['bathroom'],
            elevator = data['elevator'],
            doors = data['doors']
        )
        response_object = {
            'status': 'sucess',
            'message': 'Place was created',
        }
        db.session.add(new_place)
        db.session.commit()
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Place already exists. Please add another one.',
        }
        return response_object, 409

def get_a_place(latitude, logitud):
    place_id = "{}.{}".format(latitude, logitud)
    return Place.query.filter_by(place_id=place_id).first()