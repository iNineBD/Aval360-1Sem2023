from usuarios.editarusuarios import editarusuarios
from usuarios.excluirusuarios import excluirusuarios
from usuarios.promoteusuarios import promoteusuarios
import os

def ctrl_usuarios():
    condicao = True
    while condicao:
        print('')
        print("Controle de Usuários!!!")
        print('')
        while True:
            try:
                print("Escolha uma opção:\n1 - Editar Usuários\n2 - Excluir Usuários do Time \n3 - Promover Usuário a ADM \n0 - Voltar\n")
                op = int(input("Digite aqui: "))
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            editarusuarios()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            excluirusuarios()

        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            promoteusuarios()
            
        elif op == 0:
            condicao = False
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("")