from Criar_LojaML import criar_loja_ml, criar_pos_ml
from Scripts_ML import exibir_estados, error_int,escolher_estado, op_invalida, limpar
from Verificadores import loja_criada_true, verificar_loja_criada, verificar_pos_criada, pos_criado_true, verificar_token_true
import time

#Desenvolvido por Osvaldeir

token_criado = verificar_token_true()
pos_criada = verificar_pos_criada()
loja_criada = verificar_loja_criada()

if token_criado:
    if loja_criada:
        print("Loja já está criada!")
    else:
        while True:
            print(f"{'='*15}SISTEMA PAGAMENTO MERCADO PAGO{'='*15}")
            print(f"{'='*5}Criar Loja{'='*5}")
            escolha_criar_loja = input("""1.Criar loja predefinida
2.Criar loja personalizada
Escolha: """)
            
            if escolha_criar_loja == "1":
                nome_loja = "Loja Python :)"
                cidade = "Imperatriz"
                estado = "Maranhão"
                numero_casa = "1234"
                nome_rua = "Rua Python"
                saida_criar_loja = criar_loja_ml(nome_loja,cidade,estado,numero_casa,nome_rua)
                if saida_criar_loja:
                    print("Loja criada com sucesso!")
                    loja_criada_true()
                    time.sleep(1)
                    break

            elif escolha_criar_loja == "2": 
                nome_loja = input("Insira o nome da sua loja: ")
                print("Nome escolhido!")
                time.sleep(0.5)

                exibir_estados()
                while True:
                    try:
                        estado = int(input("Insira o numero do estado desejado: "))
                        estado_escolhido = escolher_estado(estado)
                        if estado_escolhido:
                            print(f"Estado escolhido: {estado_escolhido}")
                            time.sleep(1)
                            break
                        else:
                            continue
                    except:
                        error_int()
                        time.sleep(0.5)
                        continue
                print("Obs: Insira um nome de cidade válida!")
                cidade = input("Insira sua cidade: ")
                numero_casa = input("Numero da casa: ")
                nome_rua = input("Rua: ")
                saida_criar_loja = criar_loja_ml(nome_loja,cidade.capitalize(),estado_escolhido,numero_casa,nome_rua)
                if saida_criar_loja:
                    print("Loja criada com sucesso!")
                    loja_criada_true()
                    time.sleep(1)
                    break
                else:
                    continue

            else:
                op_invalida()
                time.sleep(1)

    loja_criada_pos = verificar_loja_criada()
    if pos_criada:
        print("POS já está criada!")
    else:
        if loja_criada_pos:
            while True:
                print(f"{'='*15}SISTEMA PAGAMENTO MERCADO PAGO{'='*15}")
                print(f"{'='*5}Criar POS{'='*5}")
                escolha_criar_pos = input("""1.Criar POS predefinida
2.Criar POS personalizada
Escolha: """)
                if escolha_criar_pos == "1":
                    nome_pos = "Pos Python"
                    saida_pos = criar_pos_ml(nome_pos)
                    if saida_pos:
                        print("POS criada com sucesso!")
                        pos_criado_true()
                        time.sleep(1)
                        break
                    else:
                        time.sleep(2)
                        continue

                elif escolha_criar_pos == "2":
                    nome_pos = input("Insira o nome para sua POS: ")
                    saida_pos = criar_pos_ml(nome_pos)
                    if saida_pos:
                        print("POS criada com sucesso!")
                        pos_criado_true()
                        time.sleep(1)
                        break
                    else:
                        time.sleep(2)
                        continue
                else:
                    op_invalida()
                    time.sleep(1)
        else:
            print("A loja aindá não está criada!")
else:
    print("Realize a conexão do TOKEN, execute o arquivo 'Conectar_token'!")

