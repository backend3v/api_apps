from infrastructure.db_services import DB_Services
from domain.user import User
from infrastructure.exceptions import ApiError
from aplication.api.auth import generar_token_jwt

def list():
    usuarios = DB_Services.send_request("SELECT * FROM users")
    usuarios_list = []
    for user in usuarios:
        user = User({'name': user[0],'phone': user[1], 'email': user[2], 'password': user[3], 'job_place': user[4]})
        print(f"USER :: {user}")
        usuarios_list.append(user.get())
    return usuarios_list

def update(email,data):
    set_text = ""
    usuarios_list = []
    for k, v in data.items():
        set_text += f"{k} = {v},"
    usuarios = DB_Services.send_request(
        f"SELECT * FROM users WHERE email='{email}'")
    if  len(usuarios) < 0:
        usuarios = DB_Services.send_request(
        f"UPDATE users SET {set_text[:-1]} WHERE email='{email}'", commit=True)
        for user in usuarios:
            usuario_dict = User({'name': user[0],'phone': user[1], 'email': user[2], 'password': user[3], 'job_place': user[4]})
            usuarios_list.append(usuario_dict.get())
    else:
        raise ApiError(message="Nothing for modify",code=204)
    return usuarios_list

def login(data):
    user = DB_Services.send_request(
        f"SELECT * FROM users WHERE name='{data['name']}' AND password='{data['password']}'")
    if len(user) != 0:
        # token = JWT.jwt_encode_callback({'identity': user[0]})
        token = generar_token_jwt(user[0])
        return token,user
    else:
        raise ApiError(message="Invalid Credentials",code=401)
    
def create(data):
    DB_Services.send_request(
        f"INSERT INTO users (name, phone, email, password, job_place) VALUES ('{data['name']}', '{data['phone']}', '{data['email']}', '{data['password']}', '{data['job_place']}')", commit=True)
    return True