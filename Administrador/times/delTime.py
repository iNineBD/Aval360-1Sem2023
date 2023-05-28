import json
import os

caminho_turma = '././data/turmas.json'
caminho_time = '././data/times.json'
caminho_usuarios = '././data/usuarios.json'

def delTime():
        #Visualizar Turmas:
        arqvturmas = open(caminho_turma)
        read_arqv_turmas = json.load(arqvturmas) #load() - leitura do arquivo
        print("\n\033[36;1mVisualizar Turmas:\033[m")
        x = 1
        for turma in read_arqv_turmas:
            print(f"\n\033[33;4m{x}\033[m - {turma.get('identificacao')}")
            x +=1
        while True:
            try:
                num_turmas = int(input('\n\033[36;1mDigite qual turma deseja visualizar os times: \033[m'))  #deixar apenas número inteiro
                if num_turmas > x - 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('\033[31mValor inválido\033[m\n')
                
        turma_escolhida = read_arqv_turmas[num_turmas - 1]
        id_turma = turma_escolhida['id_turma']

        #Visualizar Times:
        arqvtimes = open(caminho_time)
        read_arqv_times = json.load(arqvtimes)

        print("\n\033[36;1mVisualizar Times:\033[m")
        times_turma = []
        for time in read_arqv_times:
            if time.get('id_turma') == id_turma:
                times_turma.append(time)

        y = 1
        for time in times_turma:
            print(f"\033[33;4m{y}\033[m - {time['identificacao']}")
            y += 1


        while True:
            try:
                op_time_del = int(input('\033[36;1mDigite o time que deseja excluir: \033[m'))
                if op_time_del > y - 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print('\033[31mValor inválido\033[m\n')

        time_del = times_turma[op_time_del - 1]
        read_arqv_times.remove(time_del)

        arqv_usuarios = open(caminho_usuarios)
        read_arqv_usuario = json.load(arqv_usuarios)

        novo_id = ""

        for time in read_arqv_usuario:
            if time.get("id_time") == op_time_del:
                time["id_time"] = novo_id
                
                with open(caminho_usuarios, 'w') as output:
                    json.dump(read_arqv_usuario, output)
                output.close()        


        with open(caminho_time, 'w') as output:
            json.dump(read_arqv_times, output)
        output.close()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n\033[1;32mTurma excluída!!!\033[m\n')