import json

from classes.ctrl_turmas import Turmas

#método para criar times
def createTime():
        arquivo_das_turmas = open("./data/turmas.json")
        turmas= json.load (arquivo_das_turmas)
        arquivo_times = open("data/times.json")
        times= json.load (arquivo_times)

        print('\nTurmas')

        for turma in turmas:
            print(turma['id_turma'], '-', turma['identificacao'])

        op = int(input("Selecione uma turma: "))

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
            'id_turma': op
        }
        times.append(novo_time)

        with open('./data/times.json', 'w') as f:
            # Escrevendo os dados atualizados no arquivo
            json.dump(times, f)

            print('\nTime criado!')