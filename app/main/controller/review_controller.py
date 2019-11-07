from flask import request
from flask_restplus import Resource
from ..util.dto import ReviewDto
from ..service.review_service import get_a_review, get_all_reviews,save_new_review,update_review,delete_review


from ..util.decorator import token_required, admin_token_required
api = ReviewDto.api
_review = ReviewDto.review



@api.route('/reviews')
class ReviewList(Resource):
    @api.doc('list of reviews')
    @api.marshal_list_with(_review, envelope='data')
    #@token_required
    def get(self):
        """List all registered places"""
        return get_all_reviews()

    @api.response(201, 'Place successfully added.')
    @api.doc('add a new revies')
    @api.expect(_review, validate=True)
    #@token_required
    def post(self):
         """Creates a new Place """
         data = request.json
         return save_new_review(data=data)

    @api.param('rid', 'review to be edited')
    @api.response(200, 'review successfully updated.')
    @api.doc('update a specific review')
    @api.expect(_review, validate=True)
    def put(self):
        """ update a specific place """
        data = request.json
        rid = request.rid
        return update_review(rid,data)

@api.route('/')
@api.param('place_id','Place id')
@api.response(404, 'Place not found.')
class Review(Resource):
    @api.doc('get a specific review')
    @api.marshal_with(_review)
    #@admin_token_required
    def get(self, rid):
        """get a review given its identifier"""
        review = get_a_review(rid)
        if not review:
            api.abort(404)
        else:
            return review

    @api.response(200, 'review successfully removed.')
    @api.doc('delete a specific review')
    def delete(self, rid):
        """ delete a specific review """
        return delete_place(rid)