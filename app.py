from flask import Flask, request, jsonify
import jwt, datetime
from functools import wraps
from crypto_utils import encrypt_message, decrypt_message
import datetime
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
SECRET_KEY = 'c'  # Replace with a secure random key

# JWT Login route
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')

#     if not username:
#         return jsonify({'error': 'Username is required'}), 400

#     payload = {
#         'user_id': username,
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
#     }

#     token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

#     # For PyJWT >= 2.0, this is already a str; if bytes, decode
#     if isinstance(token, bytes):
#         token = token.decode('utf-8')

#     return jsonify({'token': token})

# Protected route
@app.route('/messages', methods=['POST'])
def store_message():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        return jsonify({'error': 'Unauthorized'}), 401

    token = auth_header.split(' ')[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        user_id = payload['user_id']
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

    data = request.get_json()
    message = data.get('message')

    return jsonify({'user': user_id, 'message': message}), 201

# JWT Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    payload = {
        'user_id': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    if isinstance(token, bytes):
        token = token.decode('utf-8')

    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True)
