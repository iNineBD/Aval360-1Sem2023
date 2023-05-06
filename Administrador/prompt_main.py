from turmas import prompt_turmas
from times import prompt_times
from usuarios import prompt_usuarios

import os



def promptMain():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print("Bem vindo!!!")
        print('')
        while True:
            try:
                print("Escolha uma opção: \n1 - Controle de turmas\n2 - Controle de times\n3 - Controle de Usuários\n4 - Controle de Sprints\n0 - Voltar\n")
                op = int(input("Digite aqui: "))
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')   
        
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
            pass
        
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("----------------------------------------------------")
        
promptMain()