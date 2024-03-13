import os
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjpbImp1bGlvIiwiMTIzNTY3NDQ0NDQ0OCIsImp1bGlvQG1haWwiLCIxMjMiLCJhcSJdLCJleHAiOjE3MTAwMzYxMDAsImlzcyI6ImluZ2VzaXMudW5pcXVpbmRpby5lZHUuY28ifQ.0nowsZdpkE3IwFyV9IGwsUAiW_HLxBudhkaIA4sGJAI"
test_jwt = f"""curl -i -H "Accept: application/json" -H "Content-Type: application/json" -H 'Authorization: {token}' http://localhost:8000/test_jwt"""
list_users = f"""curl -i -H "Accept: application/json" -H "Content-Type: application/json" -H 'Authorization: {token}' http://localhost:8000/users"""


update = f"""curl -d "phone=1235674444448" -H 'Authorization: {token}' -X POST http://localhost:8000/user/julio@mail"""
registro = """curl -d "name=otavio&password=123&job_place=alla&phone=123&email=otavito@mail.com" -X POST http://localhost:8000/registro"""
login = """curl -d "{'name'='julio','password'='123'}" -X POST http://localhost:8000/login_user"""

resource = """curl -d "name=test&type=link&theme=english&content={\"content\":\"www.google.com\"}" -X POST http://localhost:8000/resource"""
os.system(login)
