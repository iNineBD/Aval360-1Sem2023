import json
import os

def visualizarSprint():
        #Visualizar Turmas:
        arqvturmas = open('././data/turmas.json')
        read_arqv_turmas = json.load(arqvturmas) #load() - leitura do arquivo
        turmas = read_arqv_turmas
        print("\nVisualizar Turmas:")
        x = 1
        for name in turmas:
            print(f"{x} - {name['identificacao']}")
            x = x+1
        print('0 - Voltar')
        
        while True:
            try:
                num_turmas = int(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro
                if num_turmas > x-1:
                    print('\nEssa turma não existe')
                elif num_turmas == 0:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return 
                else:
                    break    
            except ValueError:
                print('\nOpção inválida! Tente novamente!')

        os.system('cls' if os.name == 'nt' else 'clear')
        turma_escolhida = read_arqv_turmas[num_turmas - 1]
        id_turma = turma_escolhida['id_turma']
            
        
        #Visualizar Sprints:
        
        print("\nVisualizar Sprints:")
        while True:
            if num_turmas < x:
                #Visualizar Sprints:
                arqv_sprints = open('././data/sprint.json')
                read_arqv_sprints = json.load(arqv_sprints) #load() - leitura do arquivo
                
                y = 1
                for sprint in read_arqv_sprints:
                    if sprint.get('id_turma') == id_turma:
                        print(f"{y} - {sprint.get('identificacao')}")
                        y = y + 1
                print('0 - Voltar')
                while True:
                    try:
                        num_sprint = int(input('\nDigite qual sprint deseja visualizar: '))  #deixar apenas número inteiro
                        if num_sprint > y-1:
                            print ("\nEssa sprint não existe")
                        elif num_sprint == 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            return visualizarSprint()    
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            sprint_escolhida = read_arqv_sprints[num_sprint-1]
                            identificacao_sprint = sprint_escolhida['identificacao']
                            inicio_sprint = sprint_escolhida['inicio']
                            fim_sprint = sprint_escolhida['final']
                            print(f'\n{identificacao_sprint}')
                            print(f'Data de início: {inicio_sprint}\nData final: {fim_sprint}')
                            print('\n--------------------------')
                            return 

                            
                    except ValueError:
                        print('\nOpção inválida! Tente novamente!')
            else:
                print('\nValor inválido')
