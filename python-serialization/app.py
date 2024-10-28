from flask import Flask, jsonify, request

app = Flask(__name__)

# Liste de tâches prédéfinie
tasks = [
    {"id": 1, "title": "Faire les courses"},
    {"id": 2, "title": "Apprendre Python"},
    {"id": 3, "title": "Faire du sport"}
]

# Utilisateurs autorisés (dans un vrai scénario, utilisez une base de données sécurisée)
users = {
    "user1": "motdepasse1",
    "user2": "motdepasse2"
}

def authenticate(username, password):
    return username in users and users[username] == password

@app.route('/tasks', methods=['GET'])
def get_tasks():
    username = request.headers.get('Username')
    password = request.headers.get('Password')
    
    if not authenticate(username, password):
        return jsonify({"error": "Authentification échouée"}), 401
    
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)