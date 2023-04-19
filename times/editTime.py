import json


# funcao para editar time
def editTime():
    arqv_turma = open("./data/turmas.json", encoding="UTF-8")
    ler_arqv_turma = json.load(arqv_turma)

    print("\nTurmas:")

    # for turma in ler_arqv_turma:
    #     print(turma.get("id_turma"), "-", turma.get("identificacao"))
    i = 1
    indice_vs_turma_id = {}
    for Turma in ler_arqv_turma:
        print(i, "-", Turma.get("identificacao"))
        indice_vs_turma_id[f"{i}"] = Turma.get("id_turma")
        i = i + 1
    indice_turma = input("\nDigite qual turma deseja visualizar os times: ")
    if indice_turma not in indice_vs_turma_id:
        print("Turma inválida!")
        return
    id_turma = indice_vs_turma_id[indice_turma]

    arqv_time = open("data/times.json", encoding="UTF-8")
    ler_arqv_time = json.load(arqv_time)  # .load() - leitura do arqvo

    print("\nTimes:")
    x = False

    indice_vs_time_id = {}
    i = 1

    for time in ler_arqv_time:
        if time.get("id_turma") == id_turma:
            indice_vs_time_id[f"{i}"] = time.get("id_time")
            print(i, "-", time.get("identificacao"))
            i = i + 1
        x = True

    if x == False:
        print("Turma inválida!")

    indice_time = input("\nDigite qual time deseja editar: ")
    if indice_time not in indice_vs_time_id:
        print("Time inválido!")
        return
    id_time = indice_vs_time_id[indice_time]

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
