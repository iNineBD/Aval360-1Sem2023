import json

arqv = open('C:/Users/biake/Downloads/times.json')
read_arqv = json.load(arqv) #.load() - leitura do arqvo

print('\nTimes:')

for time in read_arqv:
    print(time.get('id_time'), '-', time.get('identificacao'))

num_time = str(input('\nDigite qual time deseja editar: '))
print('\nInsira as novas informações\n')
novo_nome_time = input('Nome do time: ')
novo_num_intg = input('Número máximo de integrantes: ')

for time in read_arqv:
    if time.get('id_time') == num_time: #get() - metododo p/ puxar o valor que eu quero
        time['identificacao'] = novo_nome_time
        time['max'] = novo_num_intg
        print('\n-----------------------------')
        print(time.get('id_time'), '-', time.get('identificacao'))
        print('Máximo de integrantes: ', time.get('max'))
        print('Turma: ', time.get('id_turma'))
        print('-----------------------------')
        print('\nEdição realizada com sucesso!')

    caminho = 'C:/Users/biake/Downloads/times.json'

    with open(caminho, 'w') as output:
        json.dump(read_arqv, output)

output.close()