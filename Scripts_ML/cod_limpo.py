from colorama import Fore, Back, Style
from os import system

def dev():
    print(Style.BRIGHT,Fore.GREEN +"Desenvolvido por Osvaldeir!")
    print(Style.RESET_ALL)

def error_int():
    print(Fore.RED+"Digite somente números!")
    print(Style.RESET_ALL)

def exemplo_float():
    print(f"Informe o valor que deseja receber",Fore.YELLOW +"(ex.: 50.00)")
    print(Style.RESET_ALL)

def limpar():
    system('cls')

def error_loja():
    print(Fore.RED+"Execute o código 'criar_loja' para continuar...")
    print(Style.RESET_ALL)

def op_invalida():
    print(Fore.RED+"Opção inválida!")
    print(Style.RESET_ALL)

def aguardando_pagamento():
    print(Fore.YELLOW+"Aguardando pagamento...")
    print(Style.RESET_ALL)

def pagamento_efetuado():
    print(Fore.GREEN+"Pagamento realizado!")
    print(Style.RESET_ALL)