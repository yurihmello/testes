import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():

    nome = input("digite seu nome: "
    if nome == "Ana" or nome == "ana" or nome == "Ana Luiza" or nome == "Ana Mignoli":
        frase = "amor eu te amo demais, obrigado por tudo, você é o amor da minha vida. Quero viver contigo para o resto da minha vida, você é linda, especial, tudo que eu poderia sonhar e mais do que eu poderia sonhar, lhe amo demais"

    return frase

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

