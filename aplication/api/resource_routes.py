
from aplication.api.middlewares import middleware, middleware_jwt
from flask import request, jsonify
from infrastructure.resource_services import create as resource_create
from infrastructure.exceptions import ApiError
class ResourceRoutes:
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

        @self.app.route('/resource', methods=['POST'])
        @middleware
        def create_resource():
            data = dict(request.form)
            if 'name' in data.keys() and 'type' in data.keys() and 'theme' in data.keys() and 'content' in data.keys():
                resource_create(data)
                return jsonify({'mensaje': 'Success'}), 201
            else:
                raise ApiError(message="Required Name, email and Password fields",code=400)

        # @self.app.route('/login', methods=['POST'])
        # @middleware
        # def login():
        #     data = dict(request.form)
        #     if 'name' in data.keys() and 'password' in data.keys():
        #         token = user_login(data)
        #         return jsonify({'token': token}), 200
        #     else:
        #         raise ApiError(message="Required Name and Password fields",code=400)

        # @self.app.route('/users', methods=['GET'])
        # @middleware_jwt
        # def listar_usuarios():
        #     usuarios_list = user_list()
        #     return jsonify({'usuarios': usuarios_list}), 200

        # @self.app.route('/user/<email>', methods=['POST'])
        # @middleware_jwt
        # def actualizar_usuarios(email):
        #     data = dict(request.form)
        #     usuarios_list = []
        #     if len(data) > 0:
        #         usuarios_list = user_update(email=email,data=data)
        #     return jsonify({'user': usuarios_list}), 200

        # @self.app.route('/user', methods=['DELETE'])
        # @middleware_jwt
        # def eliminar_usuarios():
        #     usuarios = DB_Services.send_request("SELECT * FROM usuarios")
        #     usuarios_list = []
        #     for user in usuarios:
        #         usuario_dict = {
        #             'id': user[0],
        #             'nombre': user[1],
        #             'email': user[3],
        #         }
        #         usuarios_list.append(usuario_dict)
        #     return jsonify({'user': usuarios_list}), 200
