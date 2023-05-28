from Administrador.times.createTime import createTime
from Administrador.times.visualizarTimes import visualizarTimes
from Administrador.times.editTime import editTime
from Administrador.times.getIntegrantes import getIntegrantes
from Administrador.times.delTime import delTime
import os


def ctrl_times():
    condicao = True
    while condicao:
        print("\n\033[32;1mCONTROLE DE TIMES\033[m\n")
        while True:
            try:
                print("\033[36;1mESCOLHA UMA OPÇÃO: \033[m\n\n\033[33;4m1\033[m - Criar Time\n\033[33;4m2\033[m - Visualizar Time\n\033[33;4m3\033[m - Editar Time\n\033[33;4m4\033[m - Excluir Time\n\033[33;4m5\033[m - Visualizar Integrantes\n\033[33;4m0\033[m - Voltar\n")
                op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
                break
            except ValueError:
                print('\n\033[31mOpção inválida! Tente novamente!\033[m\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[3;1mVocê escolheu a opção:\033[m \033[33m"Criar Time"\033[m\n')
            createTime()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[3;1mVocê escolheu a opção:\033[m \033[33m"Visualizar Time"\033[m\n')
            visualizarTimes()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[3;1mVocê escolheu a opção:\033[m \033[33m"Editar Time"\033[m\n')
            editTime()
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[3;1mVocê escolheu a opção:\033[m \033[33m"Excluir Time"\033[m\n')
            delTime()
        
        elif op == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[3;1mVocê escolheu a opção:\033[m \033[33m"Visualizar Integrantes"\033[m\n')
            getIntegrantes() 
        
        elif op == 0:
            condicao = False
            
        else:
            print('\n\033[31mOpção inválida! Tente novamente!\033[m\n')
        