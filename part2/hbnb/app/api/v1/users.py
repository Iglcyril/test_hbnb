from flask import request
from flask_restx import Namespace, Resource
from app.services.facade import facade

api = Namespace('users', description='User related operations')


@api.route('/')
class UserList(Resource):
    def post(self):
        """Create a new user"""
        user_data = request.get_json()
        if not user_data:
            return {"error": "No user data"}, 400
        try:
            user = facade.create_user(user_data)
            return user.to_dict(), 201
        except (ValueError, TypeError) as e:
            return {"error": str(e)}, 400

    def get(self):
        """Get a list of all users"""
        users = facade.get_all_users()
        return [user.to_dict() for user in users], 200


@api.route('/<string:user_id>')
class UserResource(Resource):
    def get(self, user_id):
        """Get a user by ID"""
        user = facade.user_repo.get(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return user.to_dict(), 200
