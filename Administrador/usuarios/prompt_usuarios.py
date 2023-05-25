from Administrador.usuarios.editusuarios import editusuarios
from Administrador.usuarios.excluirusuarios import excluirusuarios
from Administrador.usuarios.promoveusuarios import promoveusuarios
import os
from time import sleep

def ctrl_usuarios():
    condicao = True
    while condicao:
        print("\033[32;1;4mCONTROLE DE USUÁRIOS!!!\033[m")
        print('')
        while True:
            try:
                print("\033[36;1mESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - \033[33;4mEditar Usuário\033[m\n\033[33;4m2\033[m - \033[33;4mExcluir Usuário\033[33;4m\n\033[33;4m3\033[m - \033[33;4mPromover Usuário á ADM\033[m\n\033[33;4m0\033[m - \033[33;4mVoltar\n\033[m")
                
                op = int(input("\033[36;1mDigite aqui\033[m: "))
                break
            except ValueError:
                print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Editar Usuários"\033[m\n')
            editusuarios()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Excluir Usuários"\033[m\n')
            excluirusuarios()

        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Promover Usuários á ADM"\033[m\n')
            promoveusuarios()
            
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            condicao = False
            
        else:
            print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')

        print("")