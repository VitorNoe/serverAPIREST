from flask import jsonify, request
from flask_jwt_extended import create_access_token

def init_auth_routes(app):
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if username == "admin" and password == "password":
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        else:
            return jsonify({"msg": "Credenciais inválidas"}), 401