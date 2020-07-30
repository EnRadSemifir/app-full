from flask_classful import FlaskView, route
from flask_sqlalchemy import SQLAlchemy
from flask import abort
from flask import request
from flask import jsonify
from models.user import User

class UsersControler(FlaskView):
    route_base = '/api/users/'

    @route('/')
    def get_users(self):
        users = []
        return jsonify(users)

    @route('/<int:user_id>')
    def get_user_by_id(self, user_id):
        user = 'ok'
        return jsonify(user)
    
    @route('/', methods=['POST'])
    def create_todo(self):
        todo = 'ok'
        return jsonify(todo)

    @route('/<int:user_id>', methods=['PUT'])
    def update_todo(self, user_id):
        todo = 'ok'
        return jsonify(todo)
    
    @route('/<int:user_id>', methods=['DELETE'])
    def delete_todo(self, user_id):
        result = 'ok'
        return jsonify(result)