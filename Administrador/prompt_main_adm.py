import os
from Administrador.turmas.prompt_turmas import ctrl_turmas
from Administrador.times.prompt_times import ctrl_times

def promptMainAdm():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
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
            ctrl_turmas()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            ctrl_times()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            #AQUI ENTRA O CONTROLE DE USUÁRIOS
            pass
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            #AQUI ENTRA O CONTROLE DE USUÁRIOS
            pass
        
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("----------------------------------------------------")