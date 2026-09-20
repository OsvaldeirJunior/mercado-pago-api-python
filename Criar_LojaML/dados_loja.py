import json
from pathlib import Path

CAMINHO = Path(__file__).parent / "loja.json"

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

