#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"
@app.route('/data')
def json_response():
    return jsonify(users)
@app.route('/status')
def status():
    return "ok"
@app.route('/users/<username>')
def user_data(username):
    return jsonify(users[username])
@app.route('/add_user', methods=['POST'])
def add_user():
    users = request.get_json()
    print(users)
    return jsonify(users)



if __name__ == "__main__": app.run()