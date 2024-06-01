#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def username(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if username:
        users[username] = data
        return jsonify({"message": "user added", "user": data}), 201
    else:
        return jsonify({"error": "username is required"}), 404


if __name__ == "__main__":
    app.run(debug=True)
