import mysql.connector

from flask import Flask, make_response,  jsonify, request
from bd import Carros

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root1993',
    database = 'Pycoderbr'
)
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():
    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM carros')
    meus_carros = my_cursor.fetchall()
    print(meus_carros)
    return make_response(
        jsonify(Carros)
    )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            
            mensagem = 'Carro cadastrado com Sucesso',
            carro= carro
        )
    )

app.run()