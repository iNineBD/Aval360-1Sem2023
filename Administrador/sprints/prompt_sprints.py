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
            print('\nOpção inválida! Tente novamente!')
        print("")