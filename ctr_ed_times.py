import json

arqv_turma = open('C:/Users/biake/Downloads/turmas.json')
ler_arqv_turma = json.load(arqv_turma)

print('\nTurmas:')

for turma in ler_arqv_turma:
    print(turma.get('id_turma'), '-', turma.get('identificacao'))

id_turma = str(input('\nDigite qual turma deseja visualizar os times: '))

arqv_time = open('C:/Users/biake/Downloads/times.json')
ler_arqv_time = json.load(arqv_time)  # .load() - leitura do arqvo

print('\nTimes:')

for time in ler_arqv_time:

    if str(time.get('id_turma')) == id_turma:
        print(time.get('id_time'), '-', time.get('identificacao'))

        id_time = str(input('\nDigite qual time deseja editar: '))

    # elif time.get('id_turma') == False:
    #     print('Turma inválida!')

    for time in ler_arqv_time:
        if time.get('id_time') == id_time:  # get() - metododo p/ puxar o valor que eu quero
            print('\nInsira as novas informações\n')
            novo_nome_time = input('Nome do time: ')
            novo_num_intg = input('Número máximo de integrantes: ')

            time['identificacao'] = novo_nome_time
            time['max'] = novo_num_intg
            print('\n--------------------------')
            print(time.get('id_time'), '-', time.get('identificacao'))
            print('Máximo de integrantes: ', time.get('max'))
            print('Turma: ', time.get('id_turma'))
            print('--------------------------')
            print('\nEdição realizada com sucesso!')

        # elif time.get('id_time') :
        #     print('Time inválido!')

    caminho = 'C:/Users/biake/Downloads/times.json'

    with open(caminho, 'w') as output:
        json.dump(ler_arqv_time, output)

output.close()
