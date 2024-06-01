from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


users = [
    User("user1", generate_password_hash("password"), "user"),
    User("admin1", generate_password_hash("password"), "admin")
]


app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)


def authenticate(username, password):
    user = next((user for user in users if user.username == username), None)
    if user and check_password_hash(user.password, password):
        return user

def identity(payload):
    username = payload['identity']
    return next((user for user in users if user.username == username), None)


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = authenticate(username, password)
    if not user:
        return jsonify({"message": "Bad username or password"}), 401
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token), 200


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = identity()
    return jsonify(logged_in_as=current_user.username, role=current_user.role), 200


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"error": "Token has expired"}), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"error": "Invalid token"}), 401

if __name__ == '__main__':
    app.run()
