from Administrador.times.createTime import createTime
from Administrador.times.visualizarTimes import visualizarTimes
from Administrador.times.editTime import editTime
from Administrador.times.getIntegrantes import getIntegrantes
from Administrador.times.delTime import delTime
import os


def ctrl_times():
    condicao = True
    while condicao:
        print("\n\033[32;1;4mControle de Times!!!\033[m\n")
        while True:
            try:
                print("\033[36;1mEscolha uma opção: \033[m\n\033[33;4m1\033[m - Criar novo Time\n\033[33;4m2\033[m - Visualizar Times\n\033[33;4m3\033[m - Editar Times\n\033[33;4m4\033[m - Excluir Times\n\033[33;4m5\033[m - Visualizar Integrantes\n\033[33;4m0\033[m - Voltar\n")
                op = int(input("\033[36;1mDigite aqui: \033[m"))
                break
            except ValueError:
                print('\n\033[31mOpção inválida! Tente novamente!\033[m\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            createTime()
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            visualizarTimes()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\nEdição de Times')
            editTime()
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            delTime()
        
        elif op == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            getIntegrantes() 
        
        elif op == 0:
            condicao = False
            
        else:
            print('\n\033[31mOpção inválida! Tente novamente!\033[m\n')
        