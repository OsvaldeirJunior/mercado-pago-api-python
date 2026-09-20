from os import system
from datetime import datetime

def guardar_qr_code(imagem):
    agora = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    novo_nome = f"pago_{agora}.png"
    system(f"ren {imagem} {novo_nome}")
    system(f"move {novo_nome} Pago >nul")