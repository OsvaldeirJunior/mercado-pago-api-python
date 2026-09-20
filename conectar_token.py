from API.receber_tokens import receber_id, receber_token
from Verificadores import conectar_token_cod
import time

#Desenvolvido por Osvaldeir

TOKEN = input("Insira seu TOKEN: ")
receber_token(TOKEN)

ID = input("Insira o ID: ")
receber_id(ID)

conectar_token_cod()

print("Token e ID salvo com sucesso, agora crie sua Loja e POS!")
time.sleep(3)