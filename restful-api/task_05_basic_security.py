#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'votre_clé_secrète_ici'
jwt = JWTManager(app)

users = {
    "user1": {"password": generate_password_hash("password1"), "role":
"user"},
    "admin1": {"password": generate_password_hash("adminpass"), "role":
"admin"}
}


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username in users and check_password_hash(
            users[username]["password"], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={'role': users[username]['role']}
        )
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401


@app.route('/jwt-protected')
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted",
                    "user": current_user}), 200


@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if users[current_user]['role'] == 'admin':
        return jsonify({"message": "Admin Access: Granted"}), 200
    else:
        return jsonify({"message": "Admin Access: Denied"}), 403


if __name__ == '__main__':
    app.run(debug=True)
