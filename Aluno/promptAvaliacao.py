#Importando módulos
import json
import os
import random
from Aluno.avaliacao.avaliacoes import autoAvaliacao, avaliacao,sprint_atual
from emoji import emojize
import shutil
from time import sleep
#Limpando a tela do terminal

#Definindo o caminho do arquivo "usuarios.json"
local_identificacao = '././data/usuarios.json'


def prompt_avaliacao(id_usu):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    usu = getUsu(id_usu)
    print(f"Olá, {usu['identificacao']}! 😀\nSeja muito bem vindo ao nosso Sistema de Avaliação 360º! O que deseja fazer?")

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

            a = sprint_atual(usu['id_usuario'])
            if a is not None:
                autoAvaliacao(usu['id_usuario'])
                avaliacao(usu['id_usuario'], usu['id_time'])
        #Se o usuário escolher a opção "Sair", exibimos uma mensagem de despedida e definimos a variável "y" como False:    
        elif entrada_avaliacao == '2':
            print("\nOpção 2 selecionada: 'Sair'\n\nSaindo...\n")
            break
        #Se o usuário escolher uma opção inválida, exibimos uma mensagem de erro:    
        else:
            print("\nOpção inválida.\nPor favor, escolha uma opção válida.\n")
        
        
def getUsu(id_usu):
    #Abrindo o arquivo JSON e carregando seus dados na variável "usuarios"
    with open(local_identificacao, 'r', encoding="UTF-8") as arquivo:
        usuarios = json.load(arquivo)

    #Buscando o nome, o id do usuário e o id do time do usuário com o id "Escolhido""
    for usuario in usuarios:
        if usuario["id_usuario"] == id_usu:
            usu = {
                    'identificacao': usuario['identificacao'],
                    'id_usuario': usuario["id_usuario"],
                    'id_time': usuario["id_time"]
                    }
    return usu
