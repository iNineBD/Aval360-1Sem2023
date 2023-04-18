import json

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
        print("")

        x = 1
        for usuario in usuarios:
            if usuario.get ('id_time') == entrada_time:
                print(x, "-", usuario.get('identificacao'))
            x = x + 1
        print("")