import json
import os

# Verifica se o arquivo JSON já existe
if os.path.exists("turmas.json"):
    # Se existir, carrega os usuários existentes
    with open("turmas.json", "r") as arquivo:
        turmas = json.load(arquivo)
else:
    # Se não existir, cria uma lista vazia
    turmas = []

# Pede para o usuário inserir os dados da turma
nome = input("Digite o nome da turma: ")

# Cria um dicionário com o nome e a data de nascimento
turma = {"nome": nome}

# Adiciona a pessoa à lista de usuários
turmas.append(turma)

# Abre o arquivo JSON em modo de escrita
with open("turmas.json", "w") as arquivo:
    # Escreve a lista de usuários no arquivo
    json.dump(turmas, arquivo)
