
from aplication.api.middlewares import middleware, middleware_jwt
from flask import request, jsonify, session,render_template

from infrastructure.db_services import DB_Services
from domain.user import User
from infrastructure.user_services import list as user_list
from infrastructure.user_services import update as user_update
from infrastructure.user_services import login as user_login
from infrastructure.user_services import create as user_create
from infrastructure.exceptions import ApiError
class UserRoutes:
    def __init__(self, app):
        self.app = app
        @self.app.after_request
        def after_request(response):
            response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
            response.headers["Access-Control-Allow-Credentials"] = "true"
            response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
            response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
            return response
        @self.app.route('/exit', methods=['POST','GET'])
        @middleware
        def exit():
            session.clear()
            return render_template('login.html')
        @self.app.route('/registro', methods=['POST'])
        @middleware
        def registro():
            data = dict(request.form)
            if 'name' in data.keys() and 'password' in data.keys() and 'email' in data.keys():
                user_create(data)
                return jsonify({'mensaje': 'Usuario registrado correctamente'}), 201
            else:
                raise ApiError(message="Required Name, email and Password fields",code=400)

        @self.app.route('/login', methods=['POST','GET'])
        @middleware
        def login():
            if request.method == 'POST':
                data = dict(request.form)
                print("data",str(data))
                if 'name' in data.keys() and 'password' in data.keys():
                    token,user = user_login(data)
                    user = user[0]
                    print(str(type(user))," ",str(user))
                    session['token'] = True
                    session['token_v'] = token.decode()
                    session['user'] = user[0]
                    return render_template('home.html')
                else:
                    raise ApiError(message="Required Name and Password fields",code=400)
            if request.method == 'GET':
                if 'token_v' in session.keys():
                    print("Token ",session.get('token_v'))
                user = session.get('user')
                print(f"User ::: {user}")
                #response = make_response(redirect('/hello'))
                #response.set_cookie('user_ip', user_ip)
                return render_template('login.html')

        @self.app.route('/users', methods=['GET'])
        @middleware_jwt
        def listar_usuarios():
            usuarios_list = user_list()
            return jsonify({'usuarios': usuarios_list}), 200

        @self.app.route('/user/<email>', methods=['POST'])
        @middleware_jwt
        def actualizar_usuarios(email):
            data = dict(request.form)
            usuarios_list = []
            if len(data) > 0:
                usuarios_list = user_update(email=email,data=data)
            return jsonify({'user': usuarios_list}), 200

        @self.app.route('/user', methods=['DELETE'])
        @middleware_jwt
        def eliminar_usuarios():
            usuarios = DB_Services.send_request("SELECT * FROM usuarios")
            usuarios_list = []
            for user in usuarios:
                usuario_dict = {
                    'id': user[0],
                    'nombre': user[1],
                    'email': user[3],
                }
                usuarios_list.append(usuario_dict)
            return jsonify({'user': usuarios_list}), 200
