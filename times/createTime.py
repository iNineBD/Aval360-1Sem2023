import json


#método para criar times
def createTime():
    
        arquivo_times = open("data/times.json")
        times= json.load (arquivo_times)

         #Visualizar Turmas:
        arqv_turmas = open('./data/turmas.json')
        read_arqv_turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        print("\nVisualizar Turmas:")
        x = 1
        for turma in read_arqv_turmas:
            print(f"{x} - {turma.get('identificacao')}")
            x = x+1
        while True:
            try:
                op = int(input('\nDigite qual turma deseja inserir um time: '))  #deixar apenas número inteiro
                if op < x -1:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')

        Identificacao_time = input(" Entre com a identificacao do time: ")
        
        for id_time in Identificacao_time:
                      
            while True:
                if id_time == Identificacao_time:
                    print ('Esse time já existe. Para prosseguir, selecione novamente a Turma.')
                    return createTime() 
                else:
                    break 
        numero_nr_integrantes_integrantes = input (" Entre com o numero maximo de pessoas no time: ")
        
        maior_id_time = 0
        for time in times:
            if maior_id_time < int(time['id_time']):
                maior_id_time = int(time['id_time'])

        novo_time = {
            'id_time': maior_id_time + 1,
            'identificacao': Identificacao_time,
            'nr_integrantes': numero_nr_integrantes_integrantes,
            'id_turma': op - 1
        }
        times.append(novo_time)

        with open('./data/times.json', 'w') as f:
            # Escrevendo os dados atualizados no arquivo
            json.dump(times, f)

            print('\nTime criado!')
createTime()