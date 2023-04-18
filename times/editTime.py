import json


# funcao para editar time
def editTime():
    arqv_turma = open("./data/turmas.json")
    ler_arqv_turma = json.load(arqv_turma)

    print("\nTurmas:")

    for turma in ler_arqv_turma:
        print(turma.get("id_turma"), "-", turma.get("identificacao"))

    id_turma = int(input("\nDigite qual turma deseja visualizar os times: "))

    arqv_time = open("data/times.json", encoding="UTF-8")
    ler_arqv_time = json.load(arqv_time)  # .load() - leitura do arqvo

    print("\nTimes:")
    x = False

    for time in ler_arqv_time:
        if time.get("id_turma") == id_turma:
            print(time.get("id_time"), "-", time.get("identificacao"))
            x = True

    if x == False:
        print("Turma inválida!")

    id_time = int(input("\nDigite qual time deseja editar: "))

    id_existentes = [
        time.get("id_time")
        for time in ler_arqv_time
        if time.get("id_turma") == id_turma
    ]
    if id_time not in id_existentes:
        print("Time inválido!")
        editTime()
    else:
        ind_time_alvo = id_existentes.index(id_time)
        print("\nInsira as novas informações\n")
        ler_arqv_time[ind_time_alvo]["identificacao"] = input("Nome do time: ")
        ler_arqv_time[ind_time_alvo]["nr_integrantes"] = input(
            "Número máximo de integrantes: "
        )
        print("\n--------------------------")
        print(
            ler_arqv_time[ind_time_alvo]["id_time"],
            "-",
            ler_arqv_time[ind_time_alvo]["identificacao"],
        )
        print("Máximo de integrantes: ", ler_arqv_time[ind_time_alvo]["nr_integrantes"])
        print("Turma: ", ler_arqv_time[ind_time_alvo]["id_turma"])
        print("--------------------------")
        print("\nEdição realizada com sucesso!")
    # elif time.get('id_time') :

    caminho = "./data/times.json"

    with open(caminho, "w") as output:
        json.dump(ler_arqv_time, output)

    output.close()
