import json
import os

def visualizarTimes():
        #Visualizar Turmas:
        arqv_turmas = open('././data/turmas.json')
        read_arqv_turmas = json.load(arqv_turmas)
        
        if read_arqv_turmas == []:
                return print('\n\033[31mSEM TURMAS!\033[m\n\033[3mTente novamente!\033[m')
                
        print("\033[36;1mTurmas:\033[m\n")
        x = 1
        for turma in read_arqv_turmas:
            print(f"\033[33;4m{x}\033[m - {turma.get('identificacao')}")
            x = x+1
        while True:
            try:
                num_turmas = int(input('\n\033[36;1mDigite qual turma deseja visualizar: \033[m'))#deixar apenas número inteiro
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            except ValueError:
                print('\n\033[31mOPÇÃO INVÁLIDA!\033[m\n\033[3mTente novamente!\033[m')
        
        turma_escolhida = read_arqv_turmas[num_turmas - 1]
        id_turma = turma_escolhida['id_turma']
            
        while True:
            if num_turmas < x:
                #Visualizar Times:
                arqv_times = open('./data/times.json')
                read_arqv_times = json.load(arqv_times) #load() - leitura do arquivo
                        
                y = 1
                for time in read_arqv_times:
                    if time.get('id_turma') == id_turma:
                        print(f"\033[33;4m{y}\033[m - {time.get('identificacao')}")
                        print(f"\033[33;4mCódigo de acesso:\033[m {time.get('cod_acesso')}")
                        print("\033[33m-----------------------------------\033[m")
                        y = y + 1
                break   
            else:
                print('\n\033[31mValor inválido\033[m')