import json

def visualizarTimes():
        #Visualizar Turmas:
        arqv_turmas = open('./data/turmas.json')
        read_arqv_turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        print("\nVisualizar Turmas:")
        for turma in read_arqv_turmas:
            print(turma.get('id_turma'), "-", turma.get('identificacao'))
        num_turmas = int(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro
        
        

        #Visualizar Times:
        arqv_times = open('./data/times.json')
        read_arqv_times = json.load(arqv_times) #load() - leitura do arquivo

        print("\nVisualizar Times:")
        x = 1
        for time in read_arqv_times:
            if time.get('id_turma') == num_turmas:
                    print(x, '-', time.get('identificacao'))
            x = x + 1