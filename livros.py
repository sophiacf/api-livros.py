from flask import Flask, jsonify
import os

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "O morro dos ventos uivantes", "autor": "Emily Brontë"},
    {"id": 2, "titulo": "Os 7 maridos de Evelyn Hugo", "autor": "Taylor Jenkins Reid"},
    {"id": 3, "titulo": "Pequeno Principe", "autor": "Antoine de Saint-Exupéry"},
    {"id": 4, "titulo": "O alienista", "autor": "Machado de Assis" },
    
]

@app.route("/livros", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de livros - Acesse /livros"})

@app.route("/", methods=["GET"])
def listar_livros():
    return jsonify(livros)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)
