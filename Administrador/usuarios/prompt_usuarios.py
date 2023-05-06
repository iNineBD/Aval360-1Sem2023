from usuarios.visualizarusuarios import visualizarusuarios
from usuarios.editarusuarios import editarusuarios
from usuarios.excluirusuarios import excluirusuarios

import os

def ctrl_usuarios():
    condicao = True
    while condicao:
        print('')
        print("Controle de Usuários!!!")
        print('')
        while True:
            try:
                print("Escolha uma opção:\n1 - Visualizar Usuários\n2 - Editar Usuários\n3 - Excluir Usuários\n0 - Voltar\n")
                op = int(input("Digite aqui: "))
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            visualizarusuarios()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            editarusuarios()

        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            excluirusuarios()
            
        elif op == 0:
            condicao = False
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("")