from Administrador.turmas.ctrl_turmas import Turmas
from time import sleep
import os

def ctrl_turmas():
    while True:
        print('')
        print("\033[32;1;4mCONTROLE DE TURMAS\033[m")
        print('')
        while True:
            try:
                print("\033[3mCerto, escolha uma opção\033[m:\n\n1 - Criar Turma\n2 - Visualizar Turma\n3 - Editar Turma\n4 - Excluir Turma\n0 - Voltar\n")
                op = int(input("\033[3;33;1mDigite aqui\033[m: "))
                break
            except ValueError:
                print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
        
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Criar Turma"\033[m\n')
            print(Turmas.createTurmas())
            
        elif op == 2:
            
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Visualizar Turma"\033[m\n')
            Turmas.listAllTurmas()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Editar Turma"\033[m\n')
            print(Turmas.editTurmas())
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[3;1mVocê escolheu a opção:\033[m \033[4;33m"Excluír Turma"\033[m\n')
            print(Turmas.delTurma())
        
        elif op == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
            
        else:
            print('\n\033[1;31mOPÇÃO INVÁLIDA!\nTente novamente...\033[m\n')
