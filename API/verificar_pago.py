import requests
import json
from API import TOKEN_API
from pathlib import Path

CAMINHO = Path(__file__).parent / "qr_code.json"

def consultar_id():
    try:
        with open(CAMINHO,"r") as arquivo:
            dados = json.load(arquivo)
            return dados['id']
    except Exception as e:
        print("Não foi possível consultar ID, verifique o diretório de 'qr_code.json'")
        print(f"CODIGO DO ERRO: {e}")
        return False

def verificar_pagamento():
    ID = consultar_id()
    URL = f"https://api.mercadopago.com/v1/orders/{ID}"
    Headers = {"Authorization": f"Bearer {TOKEN_API}"}

    try:
        consulta = requests.get(
            URL,
            headers=Headers
        )
        # print(consulta.json()['status'])
        # print(consulta.json()['status_detail'])
        saida_qr_code = consulta.json()
    except Exception as e:
        print("Não foi possível realizar a consulta do pagamento, verifique o Token e tente novamente!")
        print(f"CODIGO DO ERRO: {e}")
        return False
    
    try:
        if saida_qr_code['status_detail'] == "created":
            return False
        elif saida_qr_code['status_detail'] == "accredited":
            return True
        else:
            print("Verifique: ")
            print(saida_qr_code['status_detail'])
            return False
    except Exception as e:
        print("Não foi possível verificar o pagamento, gere outro QRCODE e tente novamente!")
        print(f"CODIGO DO ERRO: {e}")
        return False
    
