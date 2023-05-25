# from sprints.createSprint import 
# from sprints.editSprint import 

from Administrador.sprints.delSprint import delSprint
from Administrador.sprints.createSprints import createSprints
from Administrador.sprints.editSprints import editSprints
from Administrador.sprints.visualizarSprint import visualizarSprint
import os


def ctrl_sprints():
    while True:
        print('')
        
        print("\033[32;1mControle de Sprints!!!\033[m")
        print('')
        while True:
            try:
                print("Escolha uma opção: \n\033[33;4m1\033[m - Criar nova Sprint\n\033[33;4m2\033[m - Visualizar Sprint\n\033[33;4m3\033[m - Editar Sprint\n\033[33;4m4\033[m - Excluir Sprint\n\033[33;4m0\033[m - Voltar\n")
                op = int(input("\033[36mDigite aqui:\033[m "))
                break
            except ValueError:
                print('\n\033[31;1mOpção inválida! Tente novamente!\033[m\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            createSprints()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            visualizarSprint()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            editSprints()
            
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            delSprint()
        
        elif op == 0:
            break
            
        else:
            print('\n\033[31;1mOpção inválida! Tente novamente!\033[m\n')
        print("")