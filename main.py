import time
from Scripts_ML import dev, error_int, exemplo_float, limpar, error_loja, aguardando_pagamento, pagamento_efetuado, guardar_qr_code
from Verificadores import verificar_loja_criada, verificar_pos_criada
from API import gerar_qr_code, verificar_pagamento
from os import system

pos_criada = verificar_pos_criada()
loja_criada = verificar_loja_criada()

if pos_criada and loja_criada:
    while True:
        limpar()
        print(f"{'='*15}SISTEMA PAGAMENTO MERCADO PAGO{'='*15}")
        escolha_usuario = input("""1.Gerar QRCODE
2.Em desenvolvimento
0.Sair
Escolha: """)
        if escolha_usuario == "1":
            while True:
                limpar()
                print(f"{'='*15}SISTEMA PAGAMENTO MERCADO PAGO{'='*15}")
                try:
                    valor = float(input("Insira o valor: "))
                    break
                except:
                    error_int()
                    time.sleep(0.1)
                    exemplo_float()
                    time.sleep(2)
                    continue 
            print(f"Valor escolhido: {valor}")
            qr_code = gerar_qr_code(valor)
            system(qr_code)

            while True:
                verificar_pago = verificar_pagamento()
                if verificar_pago:
                    pagamento_efetuado()
                    time.sleep(2)
                    guardar_qr_code(qr_code)
                    time.sleep(3)
                    break
                else:
                    limpar()
                    aguardando_pagamento()
                    time.sleep(2)
                    continue

        elif escolha_usuario == "0":
            print("Até a próxima!")
            time.sleep(0.5)
            dev()
            time.sleep(1)
            break
else:
    error_loja()
    time.sleep(2)
