#Importando módulos
import json
import os
import random
import avaliacoes

#Limpando a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

#Definindo o caminho do arquivo "usuarios.json"
local_identificacao = 'data/usuarios.json'

#Abrindo o arquivo JSON e carregando seus dados na variável "usuarios"
with open(local_identificacao, 'r', encoding="UTF-8") as arquivo:
    usuarios = json.load(arquivo)

#Buscando o nome, o id do usuário e o id do time do usuário com o id "Escolhido""
for usuario in usuarios:
    if usuario["id_usuario"] == 1:
        nome = usuario['identificacao']
        id_usuario = usuario["id_usuario"]
        id_time = usuario["id_time"]

#Exibindo uma mensagem de boas-vindas com o nome do usuário e pedindo que ele escolha uma opção:
print(f"Olá, {nome}!\nSeja muito bem vindo ao nosso Sistema de Avaliação 360º! O que deseja fazer?")

while True:
    entrada_avaliacao = input("\n1 - Responder Avaliação"
                                "\n"
                                "\n2 - Sair"
                                "\n"
                                "\n"
                                "Escolha uma opção: ")

    #Se o usuário escolher a opção "Responder Avaliação", limpamos a tela novamente e chamamos as funções "autoAvaliacao" e "avaliacao" do módulo "avaliacoes", passando o id do usuário e o id do time como parâmetros:
    if entrada_avaliacao == '1':
        print("\nOpção 1 selecionada: 'Responder avaliação'")
        os.system('cls' if os.name == 'nt' else 'clear')
        
        avaliacoes.autoAvaliacao(id_usuario)
        avaliacoes.avaliacao(id_usuario, id_time)
        break
    #Se o usuário escolher a opção "Sair", exibimos uma mensagem de despedida e definimos a variável "y" como False:    
    elif entrada_avaliacao == '2':
        print("\nOpção 2 selecionada: 'Sair'\n\nSaindo...\n")
        y = False
        break
    #Se o usuário escolher uma opção inválida, exibimos uma mensagem de erro:    
    else:
        print("\nOpção inválida.\nPor favor, escolha uma opção válida.\n")
    