
from aplication.api.middlewares import middleware, middleware_jwt
from flask import request, jsonify, request, make_response, redirect,render_template, session,url_for,flash
from infrastructure.resource_services import create as resource_create
from infrastructure.exceptions import ApiError
class HomeRoutes:
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

        @app.route('/')
        @middleware
        def index():
            user_ip = request.remote_addr
            token = session.get('token')
            print(f"Token ::: {token}")
            if token:
                response = make_response(redirect('/home'))
                # response.set_cookie("Authorization", token)
                # response.headers
                return response
            else:
                response = make_response(redirect('/login'))
                return response
            #response = make_response(redirect('/hello'))
            #response.set_chomeookie('user_ip', user_ip)
            return render_template('index.html')
        
        @app.route('/home',methods=['POST','GET'])
        @middleware_jwt
        def home():
            user = session.get('user')
            print(f"User ::: {user}")
            #response = make_response(redirect('/hello'))
            #response.set_cookie('user_ip', user_ip)
            context = {'username':user}
            return render_template('home.html', **context)
        
