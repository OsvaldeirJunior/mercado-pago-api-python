import json
from pathlib import Path


CAMINHO = Path(__file__).parent / "loja_criada.json"

def verificar_loja_criada():
    try:
        with open(CAMINHO,"r") as arquivo:
            verificar = json.load(arquivo)
        if verificar["loja_criada"]:
            return True
        else:
            return False
    except Exception as e:
        print("Não foi possivel ler o arquivo json, verifique o diretório e tente novamente!")
        print(f"CODIGO DO ERRO: {e}")
        
def loja_criada_true():
    try:
        with open(CAMINHO,"r") as arquivo:
            dados = json.load(arquivo)
            dados['loja_criada'] = True

        with open(CAMINHO,"w") as arquivo2:
            json.dump(dados, arquivo2, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Não foi possivel editar o arquivo JSON verificador, verifique o diretorio e tente novamente!")
        print(f"CODIGO DO ERRO:{e}")
        return False
