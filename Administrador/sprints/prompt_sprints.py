# from sprints.createSprint import 
# from sprints.visualizarSprint import 
# from sprints.editSprint import 

from sprints.delSprint import delSprint
from sprints.createSprints import createSprints
import os


def ctrl_sprints():
    while True:
        print('')
        
        print("Controle de Sprints!!!")
        print('')
        while True:
            try:
                print("Escolha uma opção: \n1 - Criar nova Sprint\n2 - Visualizar Sprint\n3 - Editar Sprint\n4 - Excluir Sprint\n0 - Voltar\n")
                op = int(input("Digite aqui: "))
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            createSprints()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            pass
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nEdição de Times')
            pass
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            delSprint()
        
        elif op == 0:
            break
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("")