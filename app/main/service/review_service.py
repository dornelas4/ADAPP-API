import uuid
import datetime

from app.main import db
from app.main.model.review import Review
from sqlalchemy import or_

def get_all_reviews():
    return Review.query.all()

def delete_review(rid):
    
    if Review.query.filter_by(review_id=rid).delete():
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

def update_review(rid,data):

    review = Review.query.filter(or_(Review.review_id == rid)).first()
    if review:
        review.review = data['review']
    
     

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

def save_new_review(data):
    
   
    new_review = Review(
        place_id =data['pid'],
        review=data['review'],
        
      
    )
    response_object = {
        'status': 'sucess',
        'message': 'Place was created',
    }
    db.session.add(new_review)
    db.session.commit()
    return response_object, 201
   
def get_a_review(rid):
   
    return Review.query.filter_by(review_id=rid).first()