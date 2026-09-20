import json 
from pathlib import Path

CAMINHO_TOKEN = Path(__file__).parent / "token.json"
with open(CAMINHO_TOKEN,"r") as arquivo:
    dados_token = json.load(arquivo)

TOKEN_API = dados_token['Token']

CAMINHO_ID = Path(__file__).parent / "id.json"
with open(CAMINHO_ID,"r") as arquivo:
    dados_id = json.load(arquivo)

USER_ID = dados_id['Id']
