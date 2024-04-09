import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def online():
    return 'API está de pé'

@app.route('/totalvendas')
def totalvalor():
    tabela = pd.read_csv('carros.csv')
    total_valor = tabela['VALOR'].sum()
    resposta = {'total_valor': total_valor}
    return resposta
    


 
app.run(host='0.0.0.0')
