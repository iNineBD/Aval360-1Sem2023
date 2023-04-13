import json

class Times:
    
    #método para criar times
    def createTime():
        arquivo_das_turmas = open("data/turmas.json")
        turmas= json.load (arquivo_das_turmas)
        arquivo_times = open("data/times.json")
        times= json.load (arquivo_times)

        print('\nTurmas')

        for turma in turmas:
            print(turma['id_turma'], '-', turma['identificacao'])

        op = int(input("Selecione uma turma: "))

        Identificacao_time = input(" Entre com a identificacao do time: ")
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

        with open('data/times.json', 'w') as f:
            # Escrevendo os dados atualizados no arquivo
            json.dump(times, f)

            print('Time criado!')
    
    #funcao para editar time
    def editTime():
        arqv_turma = open('./data/turmas.json')
        ler_arqv_turma = json.load(arqv_turma)

        print('\nTurmas:')

        for turma in ler_arqv_turma:
            print(turma.get('id_turma'), '-', turma.get('identificacao'))

        id_turma = int(input('\nDigite qual turma deseja visualizar os times: '))

        arqv_time = open('data/times.json')
        ler_arqv_time = json.load(arqv_time)  # .load() - leitura do arqvo

        print('\nTimes:')

        for time in ler_arqv_time:

            if time.get('id_turma') == id_turma:
                print(time.get('id_time'), '-', time.get('identificacao'))

        id_time = int(input('\nDigite qual time deseja editar: '))

            # elif time.get('id_turma') == False:
            #     print('Turma inválida!')

        for time in ler_arqv_time:
                if time.get('id_time') == id_time:  # get() - metododo p/ puxar o valor que eu quero
                    print('\nInsira as novas informações\n')
                    novo_nome_time = input('Nome do time: ')
                    novo_num_intg = input('Número máximo de integrantes: ')

                    time['identificacao'] = novo_nome_time
                    time['nr_integrantes'] = novo_num_intg
                    print('\n--------------------------')
                    print(time.get('id_time'), '-', time.get('identificacao'))
                    print('Máximo de integrantes: ', time.get('nr_integrantes'))
                    print('Turma: ', time.get('id_turma'))
                    print('--------------------------')
                    print('\nEdição realizada com sucesso!')

                # elif time.get('id_time') :
                #     print('Time inválido!')

        caminho = './data/times.json'

        with open(caminho, 'w') as output:
            json.dump(ler_arqv_time, output)

        output.close()

    def getIntegrantes():
        arqv_turma = open('./data/turmas.json')
        turmas = json.load(arqv_turma)

        arqv_time = open('./data/times.json')
        times = json.load(arqv_time)

        arqv_usuarios = open('./data/usuarios.json')
        usuarios = json.load(arqv_usuarios)

        for turma in turmas:
            print(turma.get('id_turma'), "-", turma.get('identificacao'))
        print("")
        entrada_turma = int(input(str("Digite qual turma deseja visualizar: ")))
        print(turmas[entrada_turma].get('id_turma'), "-", turmas[entrada_turma].get('identificacao'))
        print("")

        print("Opções de time: ")
        for time in times:  
            if time.get ('id_turma') == entrada_turma:
                print(time.get('id_time'), "-", time.get('identificacao'))
        print("")        
        entrada_time = int(input(str("Digite qual time deseja visualizar: ")))
        print(times[entrada_time].get('identificacao'))
        print("")

        for usuario in usuarios:
            if usuario.get ('id_time') == entrada_time:
                print(usuario.get('identificacao'), "-", usuario.get('id_usuario'))
        print("")
