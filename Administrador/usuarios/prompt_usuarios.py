from Administrador.usuarios.editusuarios import editusuarios
from Administrador.usuarios.excluirusuarios import excluirusuarios
from Administrador.usuarios.promoveusuarios import promoveusuarios
import os
from time import sleep

def ctrl_usuarios():
    print("\033[32;1mCONTROLE DE USUÁRIOS\033[m\n\n")
    condicao = True
    while condicao:
        while True:
            try:
                print("\033[36;1mESCOLHA UMA OPÇÃO:\033[m\n\n\033[33;4m1\033[m - Editar Usuário\n\033[33;4m2\033[m - Excluir Usuário\n\033[33;4m3\033[m - Promover Usuário á ADM\n\033[33;4m0\033[m - Voltar\n")
            
                op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE USUÁRIOS\033[m\n")
            print('\033[3;1mVocê escolheu a opção:\033[m \033[33m"Editar Usuário"\033[m\n')
            editusuarios()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE USUÁRIOS\033[m\n")
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Excluir Usuário"\033[m\n')
            excluirusuarios()

        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE USUÁRIOS\033[m\n")
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Promover Usuário á ADM"\033[m\n')
            promoveusuarios()
            
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            condicao = False
            
        else:
            print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')