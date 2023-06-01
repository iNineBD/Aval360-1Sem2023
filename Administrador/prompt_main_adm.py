import os
from Administrador.turmas import prompt_turmas
from Administrador.times import prompt_times
from Administrador.sprints import prompt_sprints
from Administrador.usuarios import prompt_usuarios
from Administrador.dashborads import prompt_dashs
from time import sleep
import shutil

def promptMainAdm():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\033[1;3;32mOlá, seja muito bem vindo(a) à nossa \033[37;4mAvaliação 360º\033[m ",  end='')
        #print(emoji.emojize(':partying_face:'))
        print('')
        while True:
            try:
                print("\033[36;1mPara iniciarmos, escolha uma opção\033[m:\n\n\033[33;4m1\033[m - Controle de Turmas\n\033[33;4m2\033[m - Controle de Times\n\033[33;4m3\033[m - Controle de Usuários\n\033[33;4m4\033[m - Controle de Usuários\n\033[33;4m5\033[m - Visualizar Dashboards\n\033[33;4m0\033[m - Voltar\n\033")
                op = int(input("\033[3;33;1mDigite aqui\033[m: "))
                print('\n\033[32;3mACESSANDO NOSSO BANCO DE DADOS...\033[m')
                sleep(0.5)
                break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')   
        
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
        
        elif op == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            prompt_dashs.view_dashs()
                      
            
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
                
        else:
            print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
            print("----------------------------------------------------")
        
