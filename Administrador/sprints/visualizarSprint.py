import json
import os

def visualizarSprint():
        #Visualizar Turmas:
        arqvturmas = open('././data/turmas.json')
        read_arqv_turmas = json.load(arqvturmas) #load() - leitura do arquivo
        turmas = read_arqv_turmas

        print("\n\033[32;1mVisualizar Turmas:\033[m\n")
        x = 1
        for name in turmas:
            print(f"\033[33;4m{x}\033[m - {name['identificacao']}")
            x = x+1
        print('\033[33;4m0\033[m - Voltar')
        
        while True:
            try:
                num_turmas = int(input('\n\033[36mDigite qual turma deseja visualizar: \033[m'))  #deixar apenas número inteiro
                if num_turmas > x-1:
                    print('\n\033[31mEssa turma não existe\033[m')
                elif num_turmas == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 
                else:
                    break    
            except ValueError:
                print('\n\033[31mOpção inválida! Tente novamente!\033[m')

        os.system('cls' if os.name == 'nt' else 'clear')
        turma_escolhida = read_arqv_turmas[num_turmas - 1]
        id_turma = turma_escolhida['id_turma']
            
        
        #Visualizar Sprints:
        cond = True
        print("\n\033[32;1mVisualizar Sprints:\033[m")
        while cond:
            if num_turmas < x:
                #Visualizar Sprints:
                arqv_sprints = open('././data/sprint.json')
                read_arqv_sprints = json.load(arqv_sprints) #load() - leitura do arquivo
                
                sprint_turma = []
                for sprint in read_arqv_sprints:
                    if sprint.get('id_turma') == id_turma:
                        sprint_turma.append(sprint)
                
                
                y = 1
                for haha in sprint_turma:
                    print(f"\033[33;4m{y}\033[m - {haha['identificacao']}")
                    y = y + 1
        
                print('\033[33;4m0 - Voltar\033[m')
                while True:
                    try:
                        num_sprint = int(input('\n\033[32mDigite qual sprint deseja visualizar: \033[m'))  #deixar apenas número inteiro
                        if num_sprint > y-1:
                            print ("\033[31m\nEssa sprint não existe\033[m")
                        elif num_sprint == 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            cond = False
                            break  
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            sprint_escolhida = sprint_turma[num_sprint-1]
                            identificacao_sprint = sprint_escolhida['identificacao']
                            inicio_sprint = sprint_escolhida['inicio']
                            fim_sprint = sprint_escolhida['final']
                            print(f'\n{identificacao_sprint}')
                            print(f'Data de início: {inicio_sprint}\nData final: {fim_sprint}')
                            print('\n--------------------------')
                            return 

                            
                    except ValueError:
                        print('\033[31m\nOpção inválida! Tente novamente!\033[m')
            else:
                print('\033[31m\nValor inválido\033[m')
