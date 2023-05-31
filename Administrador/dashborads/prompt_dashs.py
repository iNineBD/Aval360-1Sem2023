from Administrador.dashborads.dash_time import visualizarDashTime
from Administrador.dashborads.dash_turma import dashturma
from Administrador.dashborads.dash_integrante import dash_integrante_adm

import os


def view_dashs():
    while True:
        print('')
        
        print("Vizualizção de Dashboards")
        print('')
        while True:
            try:
                print("Escolha um indicador: \n1 - Global\n2 - Turma\n3 - Time\n4 - Integrante\n0 - Voltar\n")
                op = int(input("Digite aqui: "))
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            pass
            
        elif op == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            dashturma()
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            visualizarDashTime()
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            dash_integrante_adm()
        
        elif op == 0:
            break
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("")