from times.createTime import createTime
from times.visualizarTimes import visualizarTimes
from times.editTime import editTime
from times.getIntegrantes import getIntegrantes
from times.delTime import delTime
import os


def ctrl_times():
    condicao = True
    while condicao:
        print('')
        print("Controle de Times!!!")
        print('')
        while True:
            try:
                print("Escolha uma opção: \n1 - Criar novo time\n2 - Visualizar times\n3 - Editar times\n4 - Excluir times\n5 - Visualizar integrantes\n0 - Voltar\n")
                op = int(input("Digite aqui: "))
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
                
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
            print('\nOpção inválida! Tente novamente!')
        print("")