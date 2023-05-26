import os
import pwinput
from Login.Login import Login
from Cadastro.prompt_cadastro import prompt_cadastro
import shutil
from time import sleep

os.system('cls' if os.name == 'nt' else 'clear')

while True:
# Obtém o tamanho da largura da janela
    terminal_width = shutil.get_terminal_size().columns
# Texto a ser centralizado
    texto = "\033[1;32mSISTEMA DE AVALIAÇÃO 360°\033[m"
# Calcula o espaçamento antes e depois do texto
    espacos = (terminal_width - len(texto)) // 2
# Imprime o texto centralizado
    print(" " * espacos + texto)
    # texto = 'sistema de avaliação 360º'
    # terminal_width = shutil.get_terminal_size().columns
    # espacos = (terminal_width - len(texto)) 
    # print("\033[1;32mSISTEMA DE AVALIAÇÃO 360°\033[m" * espacos)
    # print('')
    while True:
        try:
            print("\033[32;3;1mSeja muito bem vindo (a)... para começar:\033[m\n\033[36;1m\nESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - Logar\n\033[33;4m2\033[m - Cadastrar\n\033[33;4m0\033[m - Sair\n")
            op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
            break
        except ValueError:
            print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')   
        
    if op == 1:
        # Logar
        os.system('cls' if os.name == 'nt' else 'clear')
        
        cpf = input('\033[36mDigite o seu CPF: \033[m')
        senha = Login.criptografar_senha(pwinput.pwinput("\033[36mDigite a sua senha: \033[m"))
        Login.logar(cpf, senha)
            
    elif op == 2:
        # Cadastrar
        prompt_cadastro()
        
    elif op == 0:
        exit()
            
    else:
        print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')   
    #print("----------------------------------------------------")