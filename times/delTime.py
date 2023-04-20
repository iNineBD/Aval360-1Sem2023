import json

def delTime():
        #Visualizar Turmas:
        arqvturmas = open('./data/turmas.json')
        read_arqv_turmas = json.load(arqvturmas) #load() - leitura do arquivo
        print("\nVisualizar Turmas:")
        for turma in read_arqv_turmas:
            print(turma.get('id_turma'), "-", turma.get('identificacao'))
        num_turmas = int(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro
        
        #Visualizar Times:
        arqvtimes = open('./data/times.json')
        read_arqv_times = json.load(arqvtimes)

        print("\nVisualizar Times:")
        for time in read_arqv_times:
            if time.get('id_turma') == num_turmas:
                    print(time.get('id_time'), '-', time.get('identificacao'))
        time_p_del = int(input('Digite o time que deseja excluir: '))

        indice = 0
        for time in read_arqv_times:
            if time.get('id_time') == time_p_del:
                del(read_arqv_times[indice])
                break
            indice += 1
            
        caminho = './data/times.json'

        with open(caminho, 'w') as output:
            json.dump(read_arqv_times, output)

        output.close()