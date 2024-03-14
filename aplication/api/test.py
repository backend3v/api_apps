
from aplication.api.middlewares import middleware, middleware_jwt
from flask import request, jsonify, session,render_template

from infrastructure.db_services import DB_Services
from domain.user import User
from infrastructure.user_services import list as user_list
from infrastructure.user_services import update as user_update
from infrastructure.user_services import login as user_login
from infrastructure.user_services import create as user_create
from infrastructure.exceptions import ApiError
class TestRoutes:
    def __init__(self, app):
        self.app = app
        @self.app.after_request
        def after_request(response):
            response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
            response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
            return response
        @self.app.route('/test', methods=['GET'])
        @middleware
        def testing():
            return jsonify({'body': 'Hello !!'})

        