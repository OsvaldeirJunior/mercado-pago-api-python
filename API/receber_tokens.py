import json
from pathlib import Path

def receber_token(token):
    CAMINHO = Path(__file__).parent / "token.json"
    enviar_token = {"Token":token}
    try:
        with open(CAMINHO,"w") as arquivo:
            json.dump(enviar_token,arquivo, indent=4, ensure_ascii=False)
        print("Token salvo!")
        return True
    
    except Exception as e:
        print("Não foi possível salvar o Token, verifique o diretório de 'token.json'")
        print(f"CODIGO DO ERRO:{e}")
        return False
    
def receber_id(id):
    CAMINHO = Path(__file__).parent / "id.json"
    enviar_token = {"Id":id}
    try:
        with open(CAMINHO,"w") as arquivo:
            json.dump(enviar_token,arquivo, indent=4, ensure_ascii=False)
        print("Id salvo!")
        return True
    except Exception as e:
        print("Não foi possível salvar o Token, verifique o diretório de 'id.json'")
        print(f"CODIGO DO ERRO:{e}")
        return False

