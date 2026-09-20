import requests
import json
from API import TOKEN_API, USER_ID
from pathlib import Path

CAMINHO = Path(__file__).parent / "loja.json"

def criar_loja_ml(nome_loja,cidade,estado,numero_casa,nome_rua):
    URL = f"https://api.mercadopago.com/users/{USER_ID}/stores"
    Headers = {
        "Authorization": f"Bearer {TOKEN_API}"
        }
    payload = {
        "name": nome_loja,
        "location": {
            "street_number": numero_casa,
            "street_name": nome_rua,
            "city_name": cidade,
            "state_name": estado,
            "latitude": -5.5256,
            "longitude": -47.4431,
            "reference": "Mercado Pago"
        }
    }
    try:
        loja = requests.post(
            URL,
            headers=Headers,
            json=payload
        )
        if loja.status_code == 201:
            saida_loja = loja.json()
            with open(CAMINHO,"w", encoding="utf-8") as arquivo:
                json.dump(saida_loja,arquivo, indent=4, ensure_ascii=False)
            return True
        else:
            print("Não foi possivel criar a loja!, verifique o TOKEN!")
            print(TOKEN_API)
            print(f"CODIGO DO ERRO: {loja.json()}")
            return False
        
    except Exception as e:
        print("Não foi possivel criar a loja, verifique o TOKEN ou conexão!")
        print(f"CODIGO DO ERRO: {e}")
        return False

def store_id():
    try:
        with open(CAMINHO,"r") as arquivo:
            dados = json.load(arquivo)
        id = dados["id"]
        return id
    except Exception as e:
        print("Não foi possivel encontrar o ID da loja, verifique o diretório do arquivo 'loja.json'!")
        print(f"CODIGO DO ERRO:{e}")
        return False
