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
            print(f"\033[33;4m{x}\033[m - {turma.get('identificacao')}")
            x += 1
        
        if turmas == []:
                return print('\n\033[31mSEM TURMAS!\033[m\n\033[3mTente novamente!\033[m')
            
        while True:
            try:
                entrada_turma = int(input(str("\n\033[36;1mDigite qual turma acima deseja visualizar: \033[m")))
                if entrada_turma > x-1:
                    print('\n\033[31mTURMA NÃO EXISTE!\033[m\n\033[3mTente novamente!\033[m')
                else: 
                    turma_escolhida = turmas[entrada_turma - 1]
                    id_turma = turma_escolhida['id_turma']
                    
                    print("\n\033[36;1mOpções de time:\033[m\n")
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
                print('\n\033[31mVALOR INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m')
        while True:
            try:  
                entrada_time = int(input(str("\n\033[36;1mDigite qual time deseja visualizar os integrantes: \033[m\n")))
                if entrada_time > y-1:
                    print('\n\033[31mTIME INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m\n')
                else:
                    for time in times_pertencentes_turma:
                        if times_pertencentes_turma.index(time) == entrada_time - 1:
                            id_time = time['id_time']
                    break
            except ValueError:
                print('\n\033[31mVALOR INVÁLIDO!\033[m\n\033[3mTente novamente!\033[m\n')

        a = 1
        for usuario in usuarios:
            if usuario.get ('id_time') == id_time:
                print(f"\033[33;4m{a}\033[m - {usuario.get('identificacao')}")
                a +=1