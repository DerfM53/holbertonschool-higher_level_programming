#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

password = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def home():
    return "Hello, {}!".format(auth.current_user())

@app.route('/login', methods=[POST])
@jwt_required()
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401
    
access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route('/data')
def json_response():
    user = list(users.keys())
    return jsonify(user)


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def user_data(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user['username']
    users[username] = {
        "username": new_user.get('username'),
        "name": new_user.get('name'),
        "age": new_user.get('age'),
        "city": new_user.get('city')
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
