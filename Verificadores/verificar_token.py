import json
from pathlib import Path

CAMINHO = Path(__file__).parent / "verificar_token.json"

def verificar_token_true():
    try:
        with open(CAMINHO,"r") as arquivo:
            dados_token = json.load(arquivo)
            return dados_token['token_conectado']
    except Exception as e:
        print("Não foi possivel carregar as informações do TOKEN, verifique o diretório!")
        print(f"CODIGO DO ERRO:{e}")

def conectar_token_cod():
    try:
        with open(CAMINHO,"r") as arquivo1:
            dados = json.load(arquivo1)
        dados["token_conectado"] = True
        with open(CAMINHO,"w") as arquivo:
            json.dump(dados,arquivo,indent=4,ensure_ascii=False)
    except Exception as e:
        print("Não foi possivel salvar as informações do TOKEN, verifique o diretório!")
        print(f"CODIGO DO ERRO:{e}")

