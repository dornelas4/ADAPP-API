from flask_restplus import Namespace, fields


class PlaceDto:
    api = Namespace('place', description='place related operations')
    place = api.model('place', {
        'name' : fields.String(description='name of the place'),
        'place_id' : fields.String(description='unique place identifier'),
       
        'rating' : fields.Integer(description='place rating'),
        'longitude' : fields.String(description='place longitude'),
        'latitude' : fields.String(description='place latitude'),
        'wheelchair' : fields.Boolean(description='wheelchair accessibility'),
        'parking' : fields.Boolean(description='parking accessibility'),
        'bathroom' : fields.Boolean(description='bathroom accessibility'),
        'elevator' : fields.Boolean(description='elevator accessibility'),
        'doors' : fields.Boolean(description='doors accessibility')
       
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class ReviewDto:
    api = Namespace('review',description = 'review related operations')
    review = api.model('review', {
        'pid' : fields.String(description = "ID of parent place"),
        'review' : fields.String(description = "Review of place")
     
    })