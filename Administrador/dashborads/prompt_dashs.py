from Administrador.dashborads.global_grupo_avaliacao import visualizarDashGlobal
from Administrador.dashborads.dash_time import visualizarDashTime
from Administrador.dashborads.dash_turma import dashturma
from Administrador.dashborads.dash_integrante import dash_integrante_adm

import os


def view_dashs():
    print("\033[32;1mVISUALIZAÇÃO DE DASHBOARDS\033[m\n")
    while True:
        #print('')
        
        #print("Vizualizção de Dashboards")
        #print('')
        while True:
            try:
                print("\033[36;1m\nESCOLHA UM INDICADOR:\n\033[m  \n\033[33;4m1\033[m - Global\n\033[33;4m2\033[m - Turma\n\033[33;4m3\033[m - Time\n\033[33;4m4\033[m - Integrante\n\033[33;4m0\033[m - Voltar\033[m\n")
                #op = int(input("Digite aqui: "))
                op = int(input("\033[36;1mO QUE DESEJA FAZER?: \033[m"))
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
                #print('\nOpção inválida! Tente novamente!\n')
                
        if op == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if visualizarDashGlobal() == 0:
                return view_dashs()
        
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
            print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
            #print('\nOpção inválida! Tente novamente!')
        #print("")