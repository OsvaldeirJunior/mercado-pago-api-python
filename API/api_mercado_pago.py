import requests
import qrcode
import json
from uuid import uuid4
from datetime import datetime
from pathlib import Path
from random import randint

from Criar_LojaML.criar_pos import receber_external_id
from API.mp_token import TOKEN_API


URL = "https://api.mercadopago.com/v1/orders"
CAMINHO = Path(__file__).parent / "qr_code.json"

def gerar_qr_code(valor_int):
    external_id = str(receber_external_id())
    Cod_Verificar = str(uuid4())
    Headers = {"Authorization":f"Bearer {TOKEN_API}","X-Idempotency-Key":Cod_Verificar,"Content-Type":"application/json"}
    valor = str(valor_int)
    if not external_id:
        return False
    payload = { 
        "type":"qr",
        "total_amount": valor,
        "external_reference": "ext_ref_1234",
        "config":{
            "qr":{
                "external_pos_id": external_id,
                "mode": "dynamic"
                }
            },
        "transactions": {
            "payments": [
                {
                "amount": valor
                }
            ]
        },
        "items": [
            {
                "title":"Smartphone",
                "unit_price":valor,
                "quantity": 1,
                "unit_measure": "kg"
            }
        ]
        }
        
    try:
        api_comunicacao = requests.post(URL,headers=Headers,json=payload)
        if api_comunicacao.status_code == 201:
            saida_api = api_comunicacao.json()
            #print("QR CODE recebido!")
        elif api_comunicacao.status_code == 400:
            print("Requisição inválida!")
            print(api_comunicacao.json())
            return False
        elif api_comunicacao.status_code == 401:
            print("Não autorizado, verifique o TOKEN!")
            return False
        elif api_comunicacao.status_code == 500:
            print("Erro interno do servidor, verifique sua conexão e tente novamente!")
            return False
        else:
            print("Não foi possivel gerar o QRCode para pagamento, verifique o TOKEN e USER ID")
            return False

    except Exception as e:
        print(api_comunicacao.status_code)
        print("Não foi possivel comunicar com a API de geração de QRCODE, verifique o TOKEN!")
        print(f"CODIGO DO ERRO:{e}")
        return False
    
    try:
        with open(CAMINHO,"w") as arquivo:
            json.dump(saida_api, arquivo, indent=4, ensure_ascii=False)
            #print("Salvo como JSON!")
    except Exception as e:
        print("Não foi possivel salvar o pagamento em arquivo JSON, verifique o diretório!")
        return False
    
    try:
        imagem_qr_code = qrcode.make(api_comunicacao.json()['type_response']['qr_data'])
        agora = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        nome_arquivo = f"aguardando_pagamento_{agora}.png"
        imagem_qr_code.save(nome_arquivo)
        return nome_arquivo
    except Exception as e:
        print("Não foi possivel salvar a imagem do QRCODE!")
        print(e)
        return False

