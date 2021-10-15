import myMarvelKeys
import hashlib
import time
import requests


m_hash = hashlib.md5()  #função para criptografar - CHAMANDO
ts = str(time.time())   #coleta o tempo atual

#adicionando partes da criptografia na forma de bytes

m_hash.update(bytes(ts,'utf-8')) #tempo atual
m_hash.update(bytes(myMarvelKeys.apiKeyPrivate,'utf-8')) # a chave particular 
m_hash.update(bytes(myMarvelKeys.apiKeyPublic,'utf-8')) # a chave publica

hashf = m_hash.hexdigest() # cria o md5

#montando a url do request

base = "https://gateway.marvel.com" #pagina base para todos os requests
while True:
    marvel_char = input("What's the char that you want?:  \n ") #pede o personagem da marvel
    request_marvel  = "/v1/public/characters?name=" + marvel_char + "&orderBy=name&limit=1" ## o que quero do request

    #URL FINAL

    url_marvel = base + request_marvel + "&ts=" + ts + "&apikey=" + myMarvelKeys.apiKeyPublic + "&hash=" + hashf

    #fazendo  o request:

    dados = requests.get(url_marvel).json() # recebndo em json
    #verificandos dados
    try:
        descript = dados["data"]["results"][0]["description"]
        print(descript)
    except:
       print("Marvel char invalid")
    