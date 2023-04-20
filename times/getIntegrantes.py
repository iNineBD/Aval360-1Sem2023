import json

def getIntegrantes():
        arqv_turma = open('./data/turmas.json')
        turmas = json.load(arqv_turma)

        arqv_time = open('./data/times.json')
        times = json.load(arqv_time)

        arqv_usuarios = open('./data/usuarios.json')
        usuarios = json.load(arqv_usuarios)
        
        x = 1
        for turma in turmas:
            print(f"{x} - {turma.get('identificacao')}")
            x += 1
            
        while True:
            try:
                entrada_turma = int(input(str("Digite qual turma acima deseja visualizar: ")))
                if entrada_turma > x-1:
                    print ("Essa turma não existe")
                else: #
                    print("Opções de time: ")
                    times_pertencentes_turma = []
                    for time in times:  
                        if time.get ('id_turma') == entrada_turma - 1:
                            times_pertencentes_turma.append(time)
                    y = 1
                    for time in times_pertencentes_turma:
                        print(f"{y} - {time['identificacao']}")
                        y += 1
                    break
            except ValueError:
                print('Valor inválido!')
        while True:
            try:  
                entrada_time = int(input(str("Digite qual time deseja visualizar: ")))
                if entrada_time > y-1:
                    print("Time inválido!")
                else:
                    for time in times_pertencentes_turma:
                        if times_pertencentes_turma.index(time) == entrada_time - 1:
                            id_time = time['id_time']
                    break
            except ValueError:
                print('Valor inválido!')
                # print("")

        a = 1
        for usuario in usuarios:
            if usuario.get ('id_time') == id_time:
                print(a, "-", usuario.get('identificacao'))
                a +=1