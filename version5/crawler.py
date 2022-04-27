import requests
import json
from time import sleep

NOTICIAS_JOGATINA = "/home/aluno/dev/desenvolvimento-distribuido/version4/noticias/jogatina.json"
NOTICIAS_SISTEMAS = "/home/aluno/dev/desenvolvimento-distribuido/version4/noticias/sistemas.json"

URL_JOGATINA = "http://localhost:5001/gravar/"
URL_SISTEMAS = "http://localhost:5002/gravar/"

def enviar(url, json_noticias):
    with open(json_noticias, "r") as arquivo:
        noticias = json.load(arquivo)
        arquivo.close()

        resposta = requests.post(url, json=json.dumps(noticias))
        if resposta.ok:
            resposta = "noticias enviadas"
        else:
            resposta = "erro no envio" + resposta.text

    return resposta

if __name__ == "__main__":
    resposta = enviar(URL_JOGATINA, NOTICIAS_JOGATINA)
    print(f"enviei jogatina. resultado: {resposta}")

    resposta = enviar(URL_SISTEMAS, NOTICIAS_SISTEMAS)
    print(f"enviei sistemas. resultado: {resposta}")

    sleep(10)