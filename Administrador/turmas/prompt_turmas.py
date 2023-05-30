from Administrador.turmas.ctrl_turmas import Turmas
from time import sleep
import os

def ctrl_turmas():
    print("\033[32;1mCONTROLE DE TURMAS\033[m\n")
    while True:
        #print("\033[32;1mCONTROLE DE TURMAS\033[m")
        while True:
            try:
                print("\033[36;1m\nESCOLHA UMA OPÇÃO:\n\033[m \n\033[33;4m1\033[m - Criar Turma\n\033[33;4m2\033[m - Visualizar Turma\n\033[33;4m3\033[m - Editar Turma\n\033[33;4m4\033[m - Excluir Turma\n\033[33;4m0\033[m - Voltar\n")
                #print("\033[3mCerto, escolha uma opção\033[m:\n\n1 - Criar Turma\n2 - Visualizar Turma\n3 - Editar Turma\n4 - Excluir Turma\n0 - Voltar\n")
                op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
                #op = int(input("\033[3;33;1mDigite aqui\033[m: "))
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
                #print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
        
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE TURMAS\033[m\n")
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Criar Turma"\033[m\n')
            print(Turmas.createTurmas())
            os.system('cls' if os.name == 'nt' else 'clear')

        elif op == 2:
            print("\033[32;1mCONTROLE DE TURMAS\033[m\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE TURMAS\033[m\n")
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Visualizar Turma"\033[m\n')
            #print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Visualizar Turma"\033[m\n')
            Turmas.listAllTurmas()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE TURMAS\033[m\n")
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Editar Turma"\033[m\n')
            print(Turmas.editTurmas())
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\033[32;1mCONTROLE DE TURMAS\033[m\n")
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[33m"Excluír Turma"\033[m\n')
            print(Turmas.delTurma())
        
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
            
        else:
            print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m') 
