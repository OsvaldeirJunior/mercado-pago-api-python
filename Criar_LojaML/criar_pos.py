import requests 
import json
from uuid import uuid4
from random import randint
from pathlib import Path

from API.mp_token import TOKEN_API
from .dados_loja import store_id


CAMINHO = Path(__file__).parent / "pos.json"

URL = "https://api.mercadopago.com/v2/pos"

def criar_pos_ml(nome_pos):
    loja_id = str(store_id())
    KEY = str(uuid4())
    Headers = {
        "Authorization": f"Bearer {TOKEN_API}",
        "X-Idempotency-Key" :KEY
    }

    ID = str(randint(1,100000))

    payload = {
        "name": nome_pos,
        "store_id": loja_id,
        "external_id": ID
    }

    try:
        criar_pdv = requests.post(
            URL,
            headers=Headers,
            json= payload
        )
        #print(criar_pdv.status_code)
        if criar_pdv.status_code == 201:
            saida_pos = criar_pdv.json()
            with open(CAMINHO,"w") as arquivo:
                json.dump(saida_pos,arquivo,indent=4, ensure_ascii=False)
            return True
        else:
            print("Não foi possivel criar o POS, verifique o TOKEN!")
            print(criar_pdv.status_code)
            print(criar_pdv.json())

    except Exception as e:
        print("Não foi possível criar o POS, verifique o TOKEN ou conexão!")
        print(f"ERRO: {e}")
        return False

def receber_external_id():
    try:
        with open(CAMINHO,"r") as arquivo:
            dados = json.load(arquivo)
        return dados['external_id']
    except Exception as e:
        print("Não foi possível rebert o External-ID do POS, verifique o diretório do arquivo 'pos.json'")
        print(f"CODIGO DO ERRO: {e}")
        return False

