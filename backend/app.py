import psycopg2
from flask import Flask, request, jsonify
from psycopg2 import pool

app = Flask(__name__)

# Configuration de la connexion à la base de données avec un pool de connexions
db_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,  # Min et Max Connexions dans le pool
    host="todo-db",  # Le nom du service ou pod PostgreSQL
    database="todo_db",
    user="user",
    password="password"
)

# Fonction pour obtenir une connexion du pool
def get_db_connection():
    return db_pool.getconn()

@app.route("/todos", methods=["GET"])
def get_todos():
    conn = get_db_connection()  # Obtenir une connexion du pool
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM todos;")
    todos = cursor.fetchall()
    cursor.close()
    db_pool.putconn(conn)  # Retourner la connexion au pool
    return jsonify([{"task": todo[0]} for todo in todos])

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data["task"]
    
    conn = get_db_connection()  # Obtenir une connexion du pool
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (%s);", (task,))  # Utilisation de paramètres pour éviter l'injection SQL
    conn.commit()  # Sauvegarder dans la base de données
    cursor.close()
    db_pool.putconn(conn)  # Retourner la connexion au pool
    
    return jsonify({"message": "Task added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
