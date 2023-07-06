import logging
import requests
import random
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração do logger
logging.basicConfig(filename='api_logs.log', level=logging.INFO)

@app.route('/api_ibge', methods=['GET'])
def api_ibge():
    start_time = time.time()  # Tempo de início da execução

    uf = request.args.get('uf')
    info = request.args.get('info')

    # URL da API
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos"

    # Fazendo a chamada GET na API
    response = requests.get(url)
    data = response.json()

    if data:
        distrito = random.choice(data)  # Selecionando um registro aleatório
        microrregiao = distrito["municipio"]["microrregiao"]["nome"]
        mesorregiao = distrito["municipio"]["microrregiao"]["mesorregiao"]["nome"]
        municipio = distrito["municipio"]["nome"]
        distrito_nome = distrito["nome"]

        # Verificando a informação desejada
        result = {}
        if info == 'microrregioes':
            result = {"microrregioes": [microrregiao]}
        elif info == 'mesorregioes':
            result = {"mesorregioes": [mesorregiao]}
        elif info == 'municipios':
            result = {"municipios": [municipio]}
        elif info == 'distritos':
            result = {"distritos": [distrito_nome]}
        else:
            return jsonify({"message": "Informação inválida. Escolha entre microrregioes, mesorregioes, municipios ou distritos."})

        # Adicionando a UF ao resultado
        result["UF"] = uf

        end_time = time.time()  # Tempo de término da execução
        execution_time = (end_time - start_time) * 1000  # Tempo de execução em milissegundos

        # Registro da requisição e tempo de execução no arquivo de logs
        logging.info(f"Requisição - UF: {uf}, Info: {info}, Tempo de execução: {execution_time} ms")

        # Retornando a resposta como JSON
        return jsonify(result)
    else:
        return jsonify({"message": "Nenhum distrito encontrado para a UF especificada."})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
