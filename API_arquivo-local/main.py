# pip install flask (Biblioteca do Pythin que permite a criação de APIs = Terminal>New Terminal>pip install flask)
#puxar a biblioteca Flask
from flask import Flask, request, make_response, jsonify

#Importação da base de dados desejada
from bd import Carros

#Esse módulo do Flask vai subir a nossa API localmente
#Vamos instalar o modulo Flask na nossa variável app
app = Flask('carros')

#Início da estruturação da API
#MÉTODO 1 - VISUALIZAÇÃO DOS DADOS (GET)
#1) O que esse método vai fazer?
#2) Onde esse método vai fazer? (ROUTE)

@app.route('/veiculos', methods=['GET'])
def get_carros():
    return Carros

#Para visualizar registros específicos
#MÉTODO 1.1 - VIZUALIZAÇÃO DE DADOS POR ID (GET)
@app.route('/veiculos/<int:id_pam>', methods=['GET'])
def get_carros_id(id_pam):
    for car in Carros:
        if car.get('id') == id_pam:
            return jsonify(car)

#MÉTODO 2 - CRIAR NOVOS REGISTROS (POST)
#Verifiar os dados que estão passados na requisição e armazenar na nossa base de dados
@app.route('/veiculos', methods=['POST'])
def criar_carro():
    car = request.get_json
    Carros.append(car)
    return make_response(
        jsonify(
            mensagem = 'Carro cadastrado com sucesso!!',
            veiculos = car
        )
    )

# MÉTODO 3 - DELETAR REGISTROS (DELETE)
# ENUMERATE vai percurrer a lista de acordo com os parâmetros pedidos 'indice' e 'carro'
@app.route('/veiculos/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify(
                {'mensagem': 'Carro excluído com sucesso!!'}
            )

# MÉTODO 4 - EDITAR OS REGISTROS (PUT)
@app.route('/veiculos/<int:id>', methods=['PUT'])
def editar_carro(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(
                Carros[indice]
                )



app.run(port=5000, host='localhost', debug=True)