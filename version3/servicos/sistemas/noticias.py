from flask import Flask
from flask import jsonify

noticia = Flask(__name__)

# "constantes"
IS_ALIVE = "yes"
VERSION = "0.0.1"
AUTHOR = "Yullo Costa Bomfim"
EMAIL = "yullo.bomfim@gmail.com"

SISTEMAS = [
    {
        "id": 1,
        "data": "22/05/2019",
        "titulo": "Estes são os 12 problemas já encontrados na atualização do Windows 10",
        "endereco": "https://olhardigital.com.br/noticia/microsoft-lista-todos-os-problemas-da-nova-atualizacao-do-windows-10/86052",
    },
    {
        "id": 2,
        "data": "10/05/2015",
        "titulo": "Atualização do Windows 10 está causando problemas para alguns usuários",
        "endereco": "https://canaltech.com.br/windows/atualizacao-do-windows-10-esta-causando-problemas-para-alguns-usuarios-46921/",
    },
    {
        "id": 3,
        "data": "04/05/2016",
        "titulo": "Top 5 distribuições Linux que podem substituir o Windows 10",
        "endereco": "https://pplware.sapo.pt/linux/top-5-distribuies-gnulinux-que-podem-substituir-o-windows-10/",
    }
]

# rotas do meu servico
# rota de ping (o cliente deve perguntar se o servico estah atendendo)
@noticia.route("/isalive/")
def is_alive():
    return IS_ALIVE

# rota que retorna informacoes basicas sobre o servico e o autor do servico
@noticia.route("/info/")
def get_info():
    info = jsonify(
        version = VERSION,
        author = AUTHOR,
        email = EMAIL
    )

    return info


# rota que retorna noticias sobre sistemas operacionais
@noticia.route("/sistemas/")
def get_sistemas():
    noticias = jsonify(
        SISTEMAS
    ) 

    return noticias

if __name__ == "__main__":
    noticia.run(
        host = "0.0.0.0",
        debug=True
    )