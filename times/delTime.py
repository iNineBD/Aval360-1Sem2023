import json

caminho_turma = './data/turmas.json'
caminho_time = './data/times.json'

def delTime():
        #Visualizar Turmas:
        arqvturmas = open(caminho_turma)
        read_arqv_turmas = json.load(arqvturmas) #load() - leitura do arquivo
        print("\nVisualizar Turmas:")
        x = 1
        for turma in read_arqv_turmas:
            print(x, "-", turma.get('identificacao'))
            x +=1
        while True:
            try:
                num_turmas = int(input('\nDigite qual turma deseja visualizar os times: '))  #deixar apenas número inteiro
                if num_turmas > x - 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Valor inválido\n')
                
        turma_escolhida = read_arqv_turmas[num_turmas - 1]
        id_turma = turma_escolhida['id_turma']

        #Visualizar Times:
        arqvtimes = open(caminho_time)
        read_arqv_times = json.load(arqvtimes)

        print("\nVisualizar Times:")
        times_turma = []
        for time in read_arqv_times:
            if time.get('id_turma') == id_turma:
                times_turma.append(time)

        y = 1
        for time in times_turma:
            print(f"{y} - {time['identificacao']}")
            y += 1


        while True:
            try:
                op_time_del = int(input('Digite o time que deseja excluir: '))
                if op_time_del > y - 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('Valor inválido\n')

        time_del = times_turma[op_time_del - 1]
        read_arqv_times.remove(time_del)

        with open(caminho_time, 'w') as output:
            json.dump(read_arqv_times, output)
        output.close()
        print('\nTurma excluída!!!\n')