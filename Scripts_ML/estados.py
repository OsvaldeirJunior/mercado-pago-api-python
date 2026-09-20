estados = [
    "Acre",
    "Alagoas",
    "Amapá",
    "Amazonas",
    "Bahia",
    "Ceará",
    "Distrito Federal",
    "Espírito Santo",
    "Goiás",
    "Maranhão",
    "Mato Grosso",
    "Mato Grosso do Sul",
    "Minas Gerais",
    "Pará",
    "Paraíba",
    "Paraná",
    "Pernambuco",
    "Piauí",
    "Rio de Janeiro",
    "Rio Grande do Norte",
    "Rio Grande do Sul",
    "Rondônia",
    "Roraima",
    "Santa Catarina",
    "São Paulo",
    "Sergipe",
    "Tocantins"
]

def exibir_estados():
    contador = 1
    for i in estados:
        print(f"{contador}-{i}")
        contador += 1

def escolher_estado(numero):
    try:
        numero -= 1
        return estados[numero]
    except:
        print(f"O Estado {numero+1} não está na lista!")
        print("Escolha um estado válido!")
        return False