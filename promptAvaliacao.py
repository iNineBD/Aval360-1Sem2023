import json
import os
import random
import avaliacoes

os.system('cls' if os.name == 'nt' else 'clear')

local_identificacao = '1Sem2023/data/usuarios.json'

# abre o arquivo JSON
with open(local_identificacao, 'r', encoding="UTF-8") as arquivo:
    usuarios = json.load(arquivo)

# busca o nome e o id do usuario "logado"
for usuario in usuarios:
    if usuario["id_usuario"] == 0:
        nome = usuario['identificacao']
        id_usuario = usuario["id_usuario"]
        id_time = usuario["id_time"]

# exibe o nome do usuario
print(f"Olá, {nome}!\nSeja muito bem vindo ao nosso Sistema de Avaliação 360º! O que deseja fazer?")


entrada_avaliacao = input("\n1 - Responder Avaliação"
                              "\n"
                              "\n2 - Sair"
                              "\n"
                              "\n"
                              "Escolha uma opção: ")

if entrada_avaliacao == '1':
    print("\nOpção 1 selecionada: 'Responder avaliação'")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    avaliacoes.autoAvaliacao(id_usuario)
    avaliacoes.avaliacao(id_usuario, id_time)
    
elif entrada_avaliacao == '2':
    print("\nOpção 2 selecionada: 'Sair'\n\nSaindo...\n")
    y = False
else:
    print("\nOpção inválida.\nPor favor, escolha uma opção válida.\n")