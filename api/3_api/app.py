from flask import Flask

server = Flask(__name__)

@server.route('/pessoas')
def pegar_pessoas():
    return "Falando"

server.run()