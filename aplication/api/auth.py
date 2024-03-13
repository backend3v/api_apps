from config import Config
import jwt
from datetime import datetime, timedelta


def generar_token_jwt(user):
    clave_secreta = Config().secret_key
    tiempo_expiracion = datetime.utcnow() + timedelta(minutes=Config().ttl_token)
    token_jwt = jwt.encode({
        'user': user,
        'exp': tiempo_expiracion,
        'iss': Config().iss
    }, clave_secreta, algorithm=Config().algorithm)
    return token_jwt
