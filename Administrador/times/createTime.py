import json
from random import randint
import os


#método para criar times
def createTime():
    
        arquivo_times = open("././data/times.json")
        times= json.load (arquivo_times)

         #Visualizar Turmas:
        arqv_turmas = open('././data/turmas.json')
        read_arqv_turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        print("\n\033[36;1mVisualizar Turmas: \033[m\n")
        x = 1
        for turma in read_arqv_turmas:
            print(f"\033[33;4m{x}\033[m - {turma.get('identificacao')}")
            x = x+1
            
        while True:
            try:
                print("\033[33;4m0\033[m - Voltar\033[m")
                op = int(input('\n\033[36;1mDigite qual turma deseja inserir um time: \033[m'))  #deixar apenas número inteiro
                if op < x:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\n\033[31mOpção inválida! Tente novamente!\033[m\n')
        
        turma_escolhida = read_arqv_turmas[op - 1]
        id_turma = turma_escolhida['id_turma']

        Identificacao_time = input("\n\033[36;1mEntre com a identificacao do Time: \033[m")
        while True:
            try:
                numero_nr_integrantes_integrantes = int(input ("\033[36;1mEntre com o numero maximo de Integrantes no Time: \033[m"))
                break
            except ValueError:
                print('\033[31mInsira um Valor Inteiro!\033[m')
        
        maior_id_time = 0
        for time in times:
            if maior_id_time < int(time['id_time']):
                maior_id_time = int(time['id_time'])
                
                
        cod_acesso = 'A' + str(randint(1, 100))

        novo_time = {
            'id_time': maior_id_time + 1,
            'identificacao': Identificacao_time,
            'nr_integrantes': numero_nr_integrantes_integrantes,
            'cod_acesso': cod_acesso,
            'id_turma': id_turma
        }
        times.append(novo_time)

        with open('././data/times.json', 'w') as f:
            # Escrevendo os dados atualizados no arquivo
            json.dump(times, f)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n\033[1;32mTime criado!\033[m')