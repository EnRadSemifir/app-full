from flask_classful import FlaskView, route
import jsonpickle
from flask import abort
from flask import request
import services.user_service as us


class UserControler(FlaskView):
    route_base = '/api/users'

    @route('/')
    def get_users(self):
        return jsonpickle.encode(us.get_users()), 200

    @route('/<string:user_name>')
    def get_user_by_name(self, user_name):
        return jsonpickle.encode(us.get_user_by_name(user_name)), 200

    @route('/', methods=['POST'])
    def create_user(self):
        return jsonpickle.encode(us.create_user(request.json)), 201

    @route('/<int:user_id>', methods=['PUT'])
    def update_user(self, user_id):
        return jsonpickle.encode(us.update_user(user_id, request.json)), 200

    @route('/<int:user_id>', methods=['DELETE'])
    def delete_user(self, user_id):
        us.delete_user(user_id)
        return "Utilisateur supprimay", 200
