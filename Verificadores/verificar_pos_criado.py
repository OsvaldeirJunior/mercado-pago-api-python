from pathlib import Path
import json

CAMINHO = Path(__file__).parent / "pos_criado.json"

def verificar_pos_criada():
    with open(CAMINHO,"r") as arquivo:
        verificar = json.load(arquivo)
    if verificar["pos_criado"]:
        return True
    else:
        return False

def pos_criado_true():
    try:
        with open(CAMINHO,"r") as arquivo:
            dados = json.load(arquivo)
            dados['pos_criado'] = True

        with open(CAMINHO,"w") as arquivo2:
            json.dump(dados, arquivo2, indent=4, ensure_ascii=False)

    except Exception as e:
        print("Não foi possivel editar o arquivo JSON verificador, verifique o diretorio e tente novamente!")
        print(f"CODIGO DO ERRO:{e}")
        return False
