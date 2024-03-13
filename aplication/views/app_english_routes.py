
from aplication.api.middlewares import middleware, middleware_jwt
from flask import request, jsonify, request, make_response, redirect,render_template, session,url_for,flash
from infrastructure.resource_services import create as resource_create
from infrastructure.exceptions import ApiError
class AppEnRoutes:
    def __init__(self, app):
        self.app = app
        # @self.app.route('/test', methods=['GET'])
        # @middleware
        # def testing():
        #     return jsonify({'body': 'Hello !!'})

        # @self.app.route('/test_jwt', methods=['GET'])
        # @middleware_jwt
        # def testing_jwt():
        #     return jsonify({'body': 'Hello !!'})

        @app.route('/app_english', methods=['GET'])
        @middleware_jwt
        def index_app_en():
            
            return render_template('app_english.html')
        
