from config import *
from modelo import Carro

@app.route("/")
def inicio():
    return 'Bem vindo ao sistema de cadastramento de automovéis. '+\
        '<a href="/listar_carros">Listar automovéis cadastrados</a>'

@app.route("/listar_carros")
def listar_carros():
    # Obter dados do BD
    carros = db.session.query(Carro).all()
    # Adicionar na lista em formato JSON
    carrosJson = [ x.json() for x in carros ]
    resposta = jsonify(carrosJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)