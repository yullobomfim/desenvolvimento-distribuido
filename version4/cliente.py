import json
import asyncio
import aiohttp

URL_SERVICO_JOGATINA = "http://localhost:5001/"
JOGATINA_IS_ALIVE = URL_SERVICO_JOGATINA + "is_alive/"
JOGATINA = URL_SERVICO_JOGATINA + "noticias/"

URL_SERVICO_SISTEMAS = "http://localhost:5002/"
SISTEMAS_IS_ALIVE = URL_SERVICO_SISTEMAS + "is_alive/"
SISTEMAS = URL_SERVICO_SISTEMAS + "noticias/"

async def acessar(url):
    dados = None

    async with aiohttp.ClientSession() as sessao:
        async with sessao.get(url) as resposta:
            dados = await resposta.text()

    return dados

async def jogatina_is_alive():
    alive= False
    if await acessar(JOGATINA_IS_ALIVE) == "yes":
        alive = True
    return alive

async def get_jogatina():
    dados = await acessar(JOGATINA)
    noticias = json.loads(dados)

    return noticias

async def sistemas_is_alive():
    alive= False
    if await acessar(SISTEMAS_IS_ALIVE) == "yes":
        alive = True

    return alive

async def get_sistemas():
    dados = await acessar(SISTEMAS)
    noticias = json.loads(dados)

    return noticias

def imprimir(tipo_noticia, noticias):
    print(f"*****ultimas noticias sobre {tipo_noticia}*****")
    for noticia in noticias:
        print(f"data: {noticia['data']}. Noticia: {noticia['titulo']}")


async def acessar_jogatina():
    while True:
        if await jogatina_is_alive():
            print(" notcias de jogos estao disponiveis")
            noticias = await get_jogatina()
            imprimir ("jogos eletronicos", noticias)
        else:
            print ("noticias de jogos indisponiveis")

        await asyncio.sleep(5)

async def acessar_sistemas():
    while True:
        if await sistemas_is_alive():
            print("notcias de sistemas estao disponiveis")
            noticias = await get_sistemas()
            imprimir ("sistemas operacionais", noticias)
        else:
            print("noticias de sistemas indisponiveis")

        await asyncio.sleep(5)

async def executar():
    await asyncio.gather(acessar_jogatina(), acessar_sistemas())

if __name__ == "__main__":
    asyncio.run(executar())