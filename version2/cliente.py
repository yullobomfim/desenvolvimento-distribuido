import urllib.request, json, time
import pandas as pd

# rotas do servico de noticias
URL_SERVICO = "http://172.22.0.2:5000/"
IS_ALIVE = URL_SERVICO + "isalive/"
JOGATINA = URL_SERVICO + "jogatina/"
SISTEMAS = URL_SERVICO + "sistemas/"

def acessar(url):
    print("acessando a url:", url)

    response = urllib.request.urlopen(url)
    data = response.read()

    return data.decode("utf-8")

def is_alive():
    alive = False
    
    if acessar(IS_ALIVE) == "yes":
        alive = True

    return alive

def get_jogatina():
    data = acessar(JOGATINA)
    noticias = json.loads(data)

    return noticias

def get_sistemas():
    data = acessar(SISTEMAS)
    noticias = json.loads(data)

    return noticias

def imprimir_noticias(noticias):
    frame = pd.DataFrame(noticias)
    print(frame.T)

if __name__ == "__main__":
    while True:
        # verifica se o servico estah ativo (is alive?)
        alive = is_alive()

        # se o servico estiver vivo...
        if alive:
            print("servico está respondendo. Acessando notícias...")
            # acessa as noticias sobre jogos eletronicos
            noticias = get_jogatina()
            # print("noticias sobre jogos eletronicos:", noticias)
            # imprime as noticias
            imprimir_noticias(noticias)

            # acessa as noticias sobre sistemas operacionais
            noticias = get_sistemas()
            # print("noticias sobre sistemas:", noticias)
            # imprime as noticias
            imprimir_noticias(noticias)
        # do contrario, se o servico nao estiver ativo
        else:
            # imprime mensagem de inatividade
            print("serviço não está ativo!")

        time.sleep(5)