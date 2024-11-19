from flask import Flask, request, jsonify
   from flask_jwt_extended import JWTManager, create_access_token, jwt_required

   app = Flask(__name__)
   app.config['JWT_SECRET_KEY'] = 'secret_key'
   jwt = JWTManager(app)

   users = []

   @app.route('/register', methods=['POST'])
   def register():
       username = request.json.get('username')
       password = request.json.get('password')
       users.append({'username': username, 'password': password})
       return jsonify(message="User registered successfully"), 201

   @app.route('/login', methods=['POST'])
   def login():
       username = request.json.get('username')
       password = request.json.get('password')
       user = next((u for u in users if u['username'] == username and u['password'] == password), None)
       if user:
           access_token = create_access_token(identity=username)
           return jsonify(access_token=access_token), 200
       return jsonify(message="Bad username or password"), 401

   @app.route('/protected', methods=['GET'])
   @jwt_required()
   def protected():
       return jsonify(message="This is a protected route"), 200

   if __name__ == '__main__':
       app.run(debug=True)
