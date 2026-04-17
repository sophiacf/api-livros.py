from flask import Flask, jsonify
import os

app = Flask(__name__)

livros = [
    {"id": 1, "livros": "O morro dos ventos uivantes"},
    {"id": 2, "livros": "Os 7 maridos de Evelyn Hugo"},
    {"id": 3, "livros": "Pequeno Principe"},
    {"id": 4, "livros": "A Casa Verde"},
    
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