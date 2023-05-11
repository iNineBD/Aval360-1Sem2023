import json

def visualizarTimes():
        #Visualizar Turmas:
        arqv_turmas = open('././data/turmas.json')
        read_arqv_turmas = json.load(arqv_turmas) #load() - leitura do arquivo
        print("Turmas:\n")
        x = 1
        for turma in read_arqv_turmas:
            print(f"{x} - {turma.get('identificacao')}")
            x = x+1
        while True:
            try:
                num_turmas = int(input('\nDigite qual turma deseja visualizar: '))  #deixar apenas número inteiro
                break
            except ValueError:
                print('\nOpção inválida! Tente novamente!\n')
        
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
                        print(f"{y} - {time.get('identificacao')}")
                        print(f"Código de acesso: {time.get('cod_acesso')}")
                        print("-----------------------------------")
                        y = y + 1
                break   
            else:
                print('\nValor inválido')
                return visualizarTimes()