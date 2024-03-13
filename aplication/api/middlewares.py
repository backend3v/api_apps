import traceback
from functools import wraps
from flask import Flask, request, jsonify, session
from config import Config
from infrastructure.db_services import DB_Services
from infrastructure.exceptions import ApiError
import jwt
from mysql.connector.errors import IntegrityError


def middleware(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print(
          f'Name{f.__name__}\n|Args {str(*args)} |\n|kwds {str(**kwds)}')
        try:
            result = f(*args, **kwds)
            return result
        except ApiError as e:
            print(f"ERROR :: {traceback.format_exc()}\nINFO : {str(e.message)} : {e.code}")
            return jsonify({'message': e.message}), e.code
        except IntegrityError as e:
            return jsonify({'error': 'User Exist'}), 202
        except Exception as e:
            print(f"ERROR :: {traceback.format_exc()}\nINFO : {str(e)}")
            return jsonify({'error': 'Error Interno'}), 500
    return wrapper


def middleware_jwt(f, _cache={'users': []}):
    @wraps(f)
    def wrapper(*args, **kwds):
        
        # print(
        # f'Name{f.__name__}\n|Args {str(*args)} |\n|kwds {str(**kwds)}')
        try:
            print("args",str(*args))
            print("kwargs",str(**kwds))
            print("DATA ::: /mm :: ",str(request.headers))
            for i in session.keys():
                print(f"FIELD {i}/{session.get(i)}/")
            if not 'token' in session.keys():
                session['token'] = False
            if session['token']:
                token =  session['token_v']
                print(f"@User t :: {session['user']}" )
            else:
                token = str(request.headers.get("Authorization", None))
            clave_secreta = Config().secret_key
            print(f"Token :: {token}")
            header = jwt.decode(token.replace('"', ''), clave_secreta,
                                algorithms=Config().algorithm, options={"verify_signature": True})
            data_user = dict(header)
            email = data_user['user'][2]
            if email in _cache['users']:
                print("cache :: ", str(_cache))
            else:
                user = DB_Services.send_request(
                    f"SELECT * FROM users WHERE email='{email}'")
                if len(user) != 0:
                    _cache['users'].append(email)
                    session['token'] = True
                    session['token_v'] = token
                    session['user'] = data_user['user'][0]
                else:
                    return jsonify({'error': 'Usuario no existe'}), 304
            result = f(*args, **kwds)
            return result
        except ApiError as e:
            print(f"ERROR :: {traceback.format_exc()}\nINFO : {str(e.message)} : {e.code}")
            return jsonify({'message': e.message}), e.code
        except IntegrityError as e:
            return jsonify({'error': 'User Exist'}), 202
        except Exception as e:
            print(f"ERROR :: {traceback.format_exc()}\nINFO : {str(e)}")
            return jsonify({'error': 'Error Interno'}), 500
    return wrapper
