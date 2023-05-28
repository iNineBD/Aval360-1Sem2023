import json
import os

def getIntegrantes():
        arqv_turma = open('././data/turmas.json')
        turmas = json.load(arqv_turma)

        arqv_time = open('././data/times.json')
        times = json.load(arqv_time)

        arqv_usuarios = open('./data/usuarios.json', encoding="UTF-8")
        usuarios = json.load(arqv_usuarios)
        
        x = 1
        for turma in turmas:
            print(f"\n\033[33;4m{x}\033[m - {turma.get('identificacao')}")
            x += 1
            
        while True:
            try:
                entrada_turma = int(input(str("\n\033[36;1mDigite qual turma acima deseja visualizar: \033[m")))
                if entrada_turma > x-1:
                    print ("\033[31mEssa turma não existe!\033[m")
                else: #
                    turma_escolhida = turmas[entrada_turma - 1]
                    id_turma = turma_escolhida['id_turma']
                    
                    print("\033[36;1mOpções de time:\033[m")
                    times_pertencentes_turma = []
                    for time in times:  
                        if time.get ('id_turma') == id_turma:
                            times_pertencentes_turma.append(time)
                    y = 1
                    for time in times_pertencentes_turma:
                        print(f"\033[33;4m{y}\033[m - {time['identificacao']}")
                        y += 1
                    break
            except ValueError:
                print('\033[31mValor inválido!\033[m')
        while True:
            try:  
                entrada_time = int(input(str("\033[36;1mDigite qual time deseja visualizar: \033[m")))
                if entrada_time > y-1:
                    print("\033[31mTime inválido!\033[m")
                else:
                    for time in times_pertencentes_turma:
                        if times_pertencentes_turma.index(time) == entrada_time - 1:
                            id_time = time['id_time']
                    break
            except ValueError:
                print('\033[31mValor inválido!\033[m')
                # print("")

        a = 1
        for usuario in usuarios:
            if usuario.get ('id_time') == id_time:
                print(a, "-", usuario.get('identificacao'))
                a +=1