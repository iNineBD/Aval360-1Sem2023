import os
from Administrador.turmas import prompt_turmas
from Administrador.times import prompt_times
from Administrador.sprints import prompt_sprints
from Administrador.usuarios import prompt_usuarios
from time import sleep
import shutil

def promptMainAdm():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
    #   Obtém o tamanho da largura da janela
        terminal_width = shutil.get_terminal_size().columns
    # Texto a ser centralizado
        texto = "\033[1;32mSISTEMA DE AVALIAÇÃO 360°\033[m"
    # Calcula o espaçamento antes e depois do texto
        espacos = (terminal_width - len(texto)) // 2
    # Imprime o texto centralizado
        print(" " * espacos + texto)
        sleep (1)
        # texto = 'sistema de avaliação 360º'
        # terminal_width = shutil.get_terminal_size().columns
        # espacos = (terminal_width - len(texto)) 
        # print("\033[1;32mSISTEMA DE AVALIAÇÃO 360°\033[m" * espacos)
        # print('')
            # print('')
            # print(f"\033[1;32mSISTEMA DE AVALIAÇÃO 360°\033[m",  end='')
            # #print(emoji.emojize(':partying_face:'))
            # print('')
            # sleep (1)
        while True:
            try:
                print("\033[32;3;1mPara iniciarmos::\033[m\n\033[36;1m\nESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - Controle de Turmas\n\033[33;4m2\033[m - Controle de Times\n\033[33;4m3\033[m - Controle de Usuários\n\033[33;4m4\033[m - Controle de Sprints\n\033[33;4m5\033[m - Visualizar Dashboards\n\033[33;4m0\033[m - Voltar\n")
                    #print("\033[3mPara iniciarmos, escolha uma opção\033[m:\n\n\033[4m1\033[m - Controle de Turmas\n\033[4m2\033[m - Controle de Times\n\033[4m3\033[m - Controle de Usuários\n\033[4m4\033[m - Controle de Sprints\n\033[4m0\033[m - Voltar\n\033[m")
                op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
                    
                print('\n\n\n\033[32;3mACESSANDO NOSSO BANCO DE DADOS...\033[m')
                print('\n')
                sleep(0.7)
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')     
            
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')

            prompt_turmas.ctrl_turmas()

        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            prompt_times.ctrl_times()

                
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            prompt_usuarios.ctrl_usuarios()
                
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            prompt_sprints.ctrl_sprints()          
            
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
                
        else:
            print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
            print("----------------------------------------------------")
        
