






import os
from Administrador.turmas import prompt_turmas
from Administrador.times import prompt_times
from Administrador.sprints import prompt_sprints
from Administrador.usuarios import prompt_usuarios

def promptMainAdm():
    os.system('cls' if os.name == 'nt' else 'clear')
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
            prompt_sprints.ctrl_sprints()
            
        
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("----------------------------------------------------")
        
