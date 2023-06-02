import json
import os
import random
from Aluno.avaliacao.avaliacoes import autoAvaliacao, avaliacao, sprint_atual
from Aluno.dashboards.prompt_dashs_integrante import ctrl_dashs
from Aluno.int_feed import feed_integrante
from emoji import emojize
import shutil
from time import sleep

# Limpando a tela do terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Resto do código...

#Definindo o caminho do arquivo "usuarios.json"
local_identificacao = '././data/usuarios.json'

# Resto do código...

def prompt_avaliacao(id_usu):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    usu = getUsu(id_usu)
    print(f"\033[32;3;1mOlá \033[m\033[36;1m{usu['identificacao']}\033[m 😀. \033[32;3;1mSeja muito bem vindo (a)!\033[m")

    while True:
        entrada_avaliacao = input("\033[36;1m\nESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - Iniciar Avaliação\n\033[33;4m2\033[m - Dashboards\n\033[33;4m3\033[m - Feedbacks\033[m\n\033[33;4m0\033[m - Sair\033[m\n\n\033[36;1mO QUE DESEJA FAZER?: \033[m")
        
        if entrada_avaliacao == '1':
            print("\nOpção 1 selecionada: 'Iniciar Avaliação'")
            a = sprint_atual(usu['id_usuario'])
            if a is not None:
                autoAvaliacao(usu['id_usuario'])
                avaliacao(usu['id_usuario'], usu['id_time'])
        elif entrada_avaliacao == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            ctrl_dashs(int(usu['id_usuario']), int(usu['id_time']))
        elif entrada_avaliacao == '3':
            os.system('cls' if os.name =='nt' else 'clear')
            feed_integrante(int(usu['id_usuario']))
        elif entrada_avaliacao == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\033[36;3mVOCÊ OPTOU POR SAIR DO PROGRAMA\033[m\n\033[32;3;1mOBRIGADO PELA PARTICIPAÇÃO!\033[m")
            break
        #Se o usuário escolher uma opção inválida, exibimos uma mensagem de erro:    
        else:
            print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
        
        
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
