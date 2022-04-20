from flask import Flask, request
from flask import jsonify
from pymemcache.client import base

servico = Flask(__name__)

# "constantes"
IS_ALIVE = "yes"
VERSION = "0.0.1"
AUTHOR = "Yullo Costa Bomfim"
EMAIL = "yullo.bomfim@gmail.com"
BANCO_VOLATIL = "banco_volatil"

# rotas do meu servico
# rota de ping (o cliente deve perguntar se o servico estah atendendo)


@servico.route("/isalive/")
def is_alive():
    return IS_ALIVE

# rota que retorna informacoes basicas sobre o servico e o autor do servico


@servico.route("/info/")
def get_info():
    info = jsonify(
        version=VERSION,
        author=AUTHOR,
        email=EMAIL
    )

    return info


@servico.route("/gravar/", methods=["post", "get"])
def gravar():
    noticias = request.get_json()
    if noticias:
        cliente = base.Client((BANCO_VOLATIL, 11211))
        cliente.set("jogatina", noticias)
        cliente.close()

    return "OK"


# rota que retorna noticias sobre jogos eletronicos
@servico.route("/noticias/")
def get_jogatina():
    cliente = base.Client((BANCO_VOLATIL, 11211))
    noticias = cliente.get("jogatina")
    cliente.close()

    return noticias


if __name__ == "__main__":
    servico.run(
        host="0.0.0.0",
        debug=True
    )
