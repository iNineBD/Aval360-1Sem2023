# #Importando módulos
# import json
# import os
# import random
# from Aluno.avaliacao.avaliacoes import autoAvaliacao, avaliacao,sprint_atual
# from emoji import emojize
# import shutil
# from time import sleep
# #Limpando a tela do terminal

# # Obtém o tamanho da largura da janela
# terminal_width = shutil.get_terminal_size().columns
# # Texto a ser centralizado
# texto = "\033[1;32mSISTEMA DE AVALIAÇÃO 360°\033[m"
# # Calcula o espaçamento antes e depois do texto
# espacos = (terminal_width - len(texto)) // 2
# # Imprime o texto centralizado
# print(" " * espacos + texto)
# sleep(1)

# #Definindo o caminho do arquivo "usuarios.json"

# local_identificacao = '././data/usuarios.json'
#Importando módulos
import json
import os
import random
from Aluno.avaliacao.avaliacoes import autoAvaliacao, avaliacao, sprint_atual
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
    print(f"\033[32;3;1mOlá \033[m\033[36;1m{usu['identificacao']}\033[m 😀. \033[32;3;1mSeja muito bem vindo (a)... para começar:\033[m")

    while True:
        entrada_avaliacao = input("\n\033[36;1m\nESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - Iniciar Avaliação\n\033[33;4m0\033[m - Sair\033[m\n\n\033[36;1mO QUE DESEJA FAZER?: \033[m")
        
        if entrada_avaliacao == '1':
            print("\nOpção 1 selecionada: 'Iniciar Avaliação'")
            os.system('cls' if os.name == 'nt' else 'clear')

            a = sprint_atual(usu['id_usuario'])
            if a is not None:
                autoAvaliacao(usu['id_usuario'])
                avaliacao(usu['id_usuario'], usu['id_time'])
        #Se o usuário escolher a opção "Sair", exibimos uma mensagem de despedida e definimos a variável "y" como False:    
        elif entrada_avaliacao == '0':
            print("\nOpção 0 selecionada: 'Sair'\n\nSaindo...\n")
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
