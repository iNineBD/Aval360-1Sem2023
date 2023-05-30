# from sprints.createSprint import 
# from sprints.editSprint import 
from Administrador.dashborads.dash_time import visualizarDashTime
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
            pass
            
        elif op == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            
            if visualizarDashTime() == True:
                
                opcao = int(input('\n0 - Voltar\n\nDigite aqui: '))
                if opcao == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return view_dashs()
            
        elif op == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            pass
        
        elif op == 0:
            break
            
        else:
            print('\nOpção inválida! Tente novamente!')
        print("")