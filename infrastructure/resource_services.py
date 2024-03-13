from infrastructure.db_services import DB_Services
from domain.resource import Resource
from infrastructure.exceptions import ApiError
from aplication.api.auth import generar_token_jwt

def list():
    usuarios = DB_Services.send_request("SELECT * FROM resources")
    usuarios_list = []
    for user in usuarios:
        user = Resource({'name': user[0],'type': user[1], 'theme': user[2], 'content': user[3]})
        print(f"USER :: {user}")
        usuarios_list.append(user.get())
    return usuarios_list

def update(email,data):
    set_text = ""
    usuarios_list = []
    for k, v in data.items():
        set_text += f"{k} = {v},"
    usuarios = DB_Services.send_request(
        f"SELECT * FROM resources WHERE email='{email}'")
    if  len(usuarios) < 0:
        usuarios = DB_Services.send_request(
        f"UPDATE resources SET {set_text[:-1]} WHERE email='{email}'", commit=True)
        for user in usuarios:
            usuario_dict = Resource({'name': user[0],'type': user[1], 'theme': user[2], 'content': user[3]})
            usuarios_list.append(usuario_dict.get())
    else:
        raise ApiError(message="Nothing for modify",code=204)
    return usuarios_list


    
def create(data):
    print("type data d ",str(type(data['content'])))
    DB_Services.send_request(
        f"INSERT INTO resources (name, type, theme, content) VALUES ('{data['name']}', '{data['type']}', '{data['theme']}', '{data['content']}')", commit=True)
    return True