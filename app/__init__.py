from flask_restplus import Api
from flask import Blueprint


from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.place_controller import api as place_ns
from .main.controller.review_controller import api as review_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/api/user')
api.add_namespace(auth_ns, path='/api')
api.add_namespace(place_ns, path='/api/place')
api.add_namespace(review_ns, path='/api/review')
